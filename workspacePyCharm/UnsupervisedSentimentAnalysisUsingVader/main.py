# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in
import pandas as pd
import database.MySQLConnect as db
import utils as ut
import vader_analysis as va
import argparse


tweets = db.get_all_tweets()
analysis_results_for_summary = []


def vader_analysis():
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

        db.update_scores_tweet(df['id'][i], compound, polarity)

    va.print_summary_analysis(analysis_results_for_summary)
    print("finished")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py", usage="python3 %(prog)s [options]")
    parser.add_argument("-alg", "--algorithm", required=True, choices='vader, oplexicon')
    args = parser.parse_args()
    if args.algorithm == 'vader':
        vader_analysis()