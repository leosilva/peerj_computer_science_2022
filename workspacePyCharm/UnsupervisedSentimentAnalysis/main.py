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
import emoticon_analysis as ea


analysis_results_for_summary = []

def vader_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using VADER lexicon"""

    print("analyzing tweets with vader...")

    columns = [0, 1, 2, 8, 9]
    #convert array to dataframe
    df = pd.DataFrame.from_dict(tweets)
    for col in list(df.columns):
        if col not in columns:
            del df[col]
    df.columns = ["id", "id_str_twitter", "text", "vader_sentiment_analysis_score", "vader_sentiment_analysis_polarity"]
    df['text'] = ut.clean_tweets(df['text'])

    for i in range(df['text'].shape[0]):
        is_already_analyzed = True
        if pd.isnull(df['vader_sentiment_analysis_score'][i]):
            is_already_analyzed = False
        if is_already_analyzed == False:
            analysis_result = va.perform_vader_analysis(df['text'][i])
            l_sentiment = ea.emoji_score(df['text'][i])
            compound = analysis_result["compound"]

            if len(l_sentiment) > 0:
                score_sum = compound + sum(l_sentiment)
                size = len(l_sentiment) + 1
                compound = score_sum / size

            if float(compound) > 1.0:
                compound = 1.0
            elif float(compound) < -1.0:
                compound = -1.0

            analysis_results_for_summary.append(analysis_result)

            polarity = ''
            if compound == 0.0:
                polarity = constant.NEUTRAL_POLARITY
            elif compound > 0.0:
                polarity = constant.POSITIVE_POLARITY
            elif compound < 0.0:
                polarity = constant.NEGATIVE_POLARITY

            if is_no_storage == False or is_no_storage == None:
                db.update_scores_tweet(df['id'][i], compound, polarity, constant.VADER_ALGORITHM)

    # va.print_summary_analysis(analysis_results_for_summary)


def oplexicon_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using OPLEXICON lexicon"""

    print("analyzing tweets with oplexicon...")

    op.create_dictionary()

    for t in tweets:
        is_already_analyzed = t[10] is not None
        if is_already_analyzed == False:
            tweet = t[2]
            tweet = ut.clean_tweets(tweet)
            tweet = np.array2string(tweet)
            tweet = ut.remove_stop_words(tweet)
            tweet = op.remove_repeated_letters(tweet)
            # tweet = ut.stemming(tweet)

            oplexicon_analysis = op.sentiment_score(tweet)
            l_sentiment = ea.emoji_score(tweet)
            oplexicon_analysis = ut.normalize(oplexicon_analysis)

            if len(l_sentiment) > 0:
                score_sum = oplexicon_analysis + sum(l_sentiment)
                size = len(l_sentiment) + 1
                oplexicon_analysis = score_sum / size

            if float(oplexicon_analysis) > 1.0:
                oplexicon_analysis = 1.0
            elif float(oplexicon_analysis) < -1.0:
                oplexicon_analysis = -1.0
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

    # ut.print_summary_analysis(analysis_results_for_summary)


def sentistrength_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using SENTISTRENGTH lexicon"""

    print("analyzing tweets with sentistrength...")

    count = 1
    tweets_to_update = []
    for t in tweets:
        is_already_analyzed = t[12] is not None
        if is_already_analyzed == False:
            tweet = t[2]
            tweet = ut.clean_tweets(tweet)
            tweet = np.array2string(tweet)
            tweet = ut.remove_stop_words(tweet)
            tweet = ut.remove_repeated_letters(tweet)
            # tweet = ut.stemming(tweet)

            sentistrenth_analysis = sa.perform_sentistrength_analysis(tweet)
            l_sentiment = ea.emoji_score(tweet)
            sentistrenth_analysis = ut.normalize(sentistrenth_analysis)

            if len(l_sentiment) > 0:
                score_sum = sentistrenth_analysis + sum(l_sentiment)
                size = len(l_sentiment) + 1
                sentistrenth_analysis = score_sum / size

            if float(sentistrenth_analysis) > 1.0:
                sentistrenth_analysis = 1.0
            elif float(sentistrenth_analysis) < -1.0:
                sentistrenth_analysis = -1.0
            analysis_results_for_summary.append(sentistrenth_analysis)

            polarity = ''
            if sentistrenth_analysis == 0.0:
                polarity = constant.NEUTRAL_POLARITY
            elif sentistrenth_analysis > 0.0:
                polarity = constant.POSITIVE_POLARITY
            elif sentistrenth_analysis < 0.0:
                polarity = constant.NEGATIVE_POLARITY

            if is_no_storage == False or is_no_storage == None:
                tweets_to_update.append((sentistrenth_analysis, polarity, t[0]))
                # db.update_scores_tweet(t[0], sentistrenth_analysis, polarity, constant.SENTISTRENGTH_ALGORITHM)
            count += 1

    db.update_scores_tweet_batch(tweets_to_update, constant.SENTISTRENGTH_ALGORITHM)

    # ut.print_summary_analysis(analysis_results_for_summary)


def sentilexpt_analysis(tweets, is_no_storage = False):
    """Function that runs and stores tweets sentiment analysis using SENTILEX_PT lexicon"""

    print("analyzing tweets with sentilex-pt...")

    sl.create_dictionaries()

    for t in tweets:
        is_already_analyzed = t[14] is not None
        if is_already_analyzed == False:
            tweet = t[2]
            tweet = ut.clean_tweets(tweet)
            tweet = np.array2string(tweet)
            tweet = ut.remove_stop_words(tweet)
            tweet = sl.remove_repeated_letters(tweet)
            # tweet = ut.stemming(tweet)

            sentilexpt_analysis = sl.sentiment_score(tweet)
            l_sentiment = ea.emoji_score(tweet)
            sentilexpt_analysis = ut.normalize(sentilexpt_analysis)

            if len(l_sentiment) > 0:
                score_sum = sentilexpt_analysis + sum(l_sentiment)
                size = len(l_sentiment) + 1
                sentilexpt_analysis = score_sum / size

            if float(sentilexpt_analysis) > 1.0:
                sentilexpt_analysis = 1.0
            elif float(sentilexpt_analysis) < -1.0:
                sentilexpt_analysis = -1.0
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

    # ut.print_summary_analysis(analysis_results_for_summary)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py", usage="python3 %(prog)s [options]")
    parser.add_argument("--nostorage")
    parser.add_argument("-alg", "--algorithm", required=True, choices=[constant.VADER_ALGORITHM,
                                                                       constant.OPLEXICON_ALGORITHM,
                                                                       constant.SENTISTRENGTH_ALGORITHM,
                                                                       constant.SENTILEXPT_ALGORITHM,
                                                                       constant.ALL_ALGORITHMS])
    args = parser.parse_args()
    is_no_storage = args.nostorage

    print("starting analysis...")
    print("----------")
    print("algorithm: {}".format(args.algorithm))
    print("is no storage? {}".format(is_no_storage))
    print("----------")

    tweets = db.get_all_tweets()

    if args.algorithm == constant.ALL_ALGORITHMS:
        vader_analysis(tweets, is_no_storage)
        oplexicon_analysis(tweets, is_no_storage)
        sentistrength_analysis(tweets, is_no_storage)
        sentilexpt_analysis(tweets, is_no_storage)
        db.update_overall_scores_and_polarities()
    elif args.algorithm == constant.VADER_ALGORITHM:
        vader_analysis(tweets, is_no_storage)
        db.update_overall_scores_and_polarities()
    elif args.algorithm == constant.OPLEXICON_ALGORITHM:
        oplexicon_analysis(tweets, is_no_storage)
        db.update_overall_scores_and_polarities()
    elif args.algorithm == constant.SENTISTRENGTH_ALGORITHM:
        sentistrength_analysis(tweets, is_no_storage)
        db.update_overall_scores_and_polarities()
    elif args.algorithm == constant.SENTILEXPT_ALGORITHM:
        sentilexpt_analysis(tweets, is_no_storage)
        db.update_overall_scores_and_polarities()

    print("finished")