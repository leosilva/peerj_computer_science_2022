# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in
import pandas as pd
import database.MySQLConnect as db
import utils as ut
import argparse
import numpy as np

import vader_analysis as va
import oplexicon_analysis as op


analysis_results_for_summary = []


def vader_analysis(tweets):
    #convert array to dataframe
    df = pd.DataFrame.from_dict(tweets)
    del df[9]
    df.columns = ["id", "id_str_twitter", "text", "created_at", "favorite_count", "retweet_count", "lang", "id_user", "vader_sentiment_analysis_score", "vader_sentiment_analysis_polarity", "screen_name"]
    df['text'] = ut.clean_tweets(df['text'])

    print("analyzing tweets with vader...")

    for i in range(df['text'].shape[0]):
        analysis_result = va.perform_vader_analysis(df['text'][i])
        analysis_results_for_summary.append(analysis_result)
        compound = analysis_result["compound"]
        polarity = ''
        if compound == 0.0:
            polarity = 'neu'
        elif compound > 0.0:
            polarity = 'pos'
        elif compound < 0.0:
            polarity = 'neg'

        db.update_scores_tweet(df['id'][i], compound, polarity, 'vader')

    va.print_summary_analysis(analysis_results_for_summary)
    print("finished")


def oplexicon_analysis(tweets):
    print("analyzing tweets with oplexicon...")

    for t in tweets:
        tweet = t[2]
        tweet = ut.clean_tweets(tweet)
        tweet = np.array2string(tweet)
        tweet = op.remove_stop_words(tweet)
        tweet = op.remove_repeated_letters(tweet)
        # tweet = op.stemming(tweet)
        oplexicon_analysis = op.score_sentimento(tweet)
        oplexicon_analysis = op.normalize(oplexicon_analysis)
        analysis_results_for_summary.append(oplexicon_analysis)

        polarity = ''
        if oplexicon_analysis == 0.0:
            polarity = 'neu'
        elif oplexicon_analysis > 0.0:
            polarity = 'pos'
        elif oplexicon_analysis < 0.0:
            polarity = 'neg'

        db.update_scores_tweet(t[0], oplexicon_analysis, polarity, 'oplexicon')

    op.print_summary_analysis(analysis_results_for_summary)
    print("finished")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py", usage="python3 %(prog)s [options]")
    parser.add_argument("-alg", "--algorithm", required=True, choices='vader, oplexicon')
    args = parser.parse_args()

    tweets = db.get_all_tweets()
    if args.algorithm == 'vader':
        vader_analysis(tweets)
    elif args.algorithm == 'oplexicon':
        oplexicon_analysis(tweets)