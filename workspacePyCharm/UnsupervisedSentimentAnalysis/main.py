import pandas as pd
import database.MySQLConnect as db
import utils as ut
import argparse
import numpy as np
import constant

import vader_analysis as va
import oplexicon_analysis as op
import sentistrength_analysis as sa
import sentilexpt_analysis as sl


analysis_results_for_summary = []


def vader_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using VADER lexicon"""

    columns = [0, 1, 2]
    #convert array to dataframe
    df = pd.DataFrame.from_dict(tweets)
    for col in list(df.columns):
        if col not in columns:
            del df[col]
    df.columns = ["id", "id_str_twitter", "text"]
    df['text'] = ut.clean_tweets(df['text'])

    print("analyzing tweets with vader...")

    for i in range(df['text'].shape[0]):
        analysis_result = va.perform_vader_analysis(df['text'][i])
        analysis_results_for_summary.append(analysis_result)
        compound = analysis_result["compound"]
        polarity = ''
        if compound == 0.0:
            polarity = constant.NEUTRAL_POLARITY
        elif compound > 0.0:
            polarity = constant.POSITIVE_POLARITY
        elif compound < 0.0:
            polarity = constant.NEGATIVE_POLARITY

        if is_no_storage == False or is_no_storage == None:
            db.update_scores_tweet(df['id'][i], compound, polarity, constant.VADER_ALGORITHM)

    va.print_summary_analysis(analysis_results_for_summary)
    print("finished")


def oplexicon_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using OPLEXICON lexicon"""

    op.create_dictionary()

    print("analyzing tweets with oplexicon...")

    for t in tweets:
        tweet = t[2]
        tweet = ut.clean_tweets(tweet)
        tweet = np.array2string(tweet)
        tweet = ut.remove_stop_words(tweet)
        tweet = op.remove_repeated_letters(tweet)
        # tweet = op.stemming(tweet)
        oplexicon_analysis = op.sentiment_score(tweet)
        oplexicon_analysis = ut.normalize(oplexicon_analysis)
        analysis_results_for_summary.append(oplexicon_analysis)

        polarity = ''
        if oplexicon_analysis == 0.0:
            polarity = constant.NEUTRAL_POLARITY
        elif oplexicon_analysis > 0.0:
            polarity = constant.POSITIVE_POLARITY
        elif oplexicon_analysis < 0.0:
            polarity = constant.NEGATIVE_POLARITY

        if is_no_storage == False or is_no_storage == None:
            db.update_scores_tweet(t[0], oplexicon_analysis, polarity, constant.OPLEXICON_ALGORITHM)

    ut.print_summary_analysis(analysis_results_for_summary)
    print("finished")


def sentistrength_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using SENTISTRENGTH lexicon"""

    print("analyzing tweets with sentistrength...")

    for t in tweets:
        tweet = t[2]
        tweet = ut.clean_tweets(tweet)
        tweet = np.array2string(tweet)
        tweet = ut.remove_stop_words(tweet)
        tweet = ut.remove_repeated_letters(tweet)
        # tweet = op.stemming(tweet)
        sentistrenth_analysis = sa.perform_sentistrength_analysis(tweet)
        sentistrenth_analysis = ut.normalize(sentistrenth_analysis)
        analysis_results_for_summary.append(sentistrenth_analysis)

        polarity = ''
        if sentistrenth_analysis == 0.0:
            polarity = constant.NEUTRAL_POLARITY
        elif sentistrenth_analysis > 0.0:
            polarity = constant.POSITIVE_POLARITY
        elif sentistrenth_analysis < 0.0:
            polarity = constant.NEGATIVE_POLARITY

        if is_no_storage == False or is_no_storage == None:
            db.update_scores_tweet(t[0], sentistrenth_analysis, polarity, constant.SENTISTRENGTH_ALGORITHM)

    ut.print_summary_analysis(analysis_results_for_summary)
    print("finished")


def sentilexpt_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using SENTILEX_PT lexicon"""

    sl.create_dictionaries()

    print("analyzing tweets with sentilex_pt...")

    for t in tweets:
        tweet = t[2]
        tweet = ut.clean_tweets(tweet)
        tweet = np.array2string(tweet)
        tweet = ut.remove_stop_words(tweet)
        tweet = sl.remove_repeated_letters(tweet)
        # tweet = op.stemming(tweet)
        sentilexpt_analysis = sl.sentiment_score(tweet)
        sentilexpt_analysis = ut.normalize(sentilexpt_analysis)
        analysis_results_for_summary.append(sentilexpt_analysis)

        polarity = ''
        if sentilexpt_analysis == 0.0:
            polarity = constant.NEUTRAL_POLARITY
        elif sentilexpt_analysis > 0.0:
            polarity = constant.POSITIVE_POLARITY
        elif sentilexpt_analysis < 0.0:
            polarity = constant.NEGATIVE_POLARITY

        if is_no_storage == False or is_no_storage == None:
            db.update_scores_tweet(t[0], sentilexpt_analysis, polarity, constant.SENTILEXPT_ALGORITHM)

    ut.print_summary_analysis(analysis_results_for_summary)
    print("finished")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py", usage="python3 %(prog)s [options]")
    parser.add_argument("--nostorage")
    parser.add_argument("-alg", "--algorithm", required=True, choices=[constant.VADER_ALGORITHM,
                                                                       constant.OPLEXICON_ALGORITHM,
                                                                       constant.SENTISTRENGTH_ALGORITHM,
                                                                       constant.SENTILEXPT_ALGORITHM])
    args = parser.parse_args()
    is_no_storage = args.nostorage

    tweets = db.get_all_tweets()
    if args.algorithm == constant.VADER_ALGORITHM:
        vader_analysis(tweets, is_no_storage)
    elif args.algorithm == constant.OPLEXICON_ALGORITHM:
        oplexicon_analysis(tweets, is_no_storage)
    elif args.algorithm == constant.SENTISTRENGTH_ALGORITHM:
        sentistrength_analysis(tweets, is_no_storage)
    elif args.algorithm == constant.SENTILEXPT_ALGORITHM:
        sentilexpt_analysis(tweets, is_no_storage)