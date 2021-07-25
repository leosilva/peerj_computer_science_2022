import mysql.connector
import constant


def __get_connection():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="!@R00tP@ssW0rd", db="TwitterDataMining")
    cursor = connection.cursor(buffered=True)
    return [connection, cursor]


def get_all_tweets():
    connection, cursor = __get_connection()
    cursor.execute("SELECT t.*, u.screen_name FROM Tweet t INNER JOIN User u ON t.id_user = u.id")
    tweets = cursor.fetchall()

    return tweets


def update_scores_tweet_batch(parameters, algorithm):
    connection, cursor = __get_connection()
    sql = ""

    if algorithm == constant.VADER_ALGORITHM:
        sql = "UPDATE Tweet t SET t.vader_sentiment_analysis_score = %s, t.vader_sentiment_analysis_polarity = %s WHERE t.id = %s"
    elif algorithm == constant.OPLEXICON_ALGORITHM:
        sql = "UPDATE Tweet t SET t.oplexicon_sentiment_analysis_score = %s, t.oplexicon_sentiment_analysis_polarity = %s WHERE t.id = %s"
    elif algorithm == constant.SENTISTRENGTH_ALGORITHM:
        sql = "UPDATE Tweet t SET t.sentistrength_sentiment_analysis_score = %s, t.sentistrength_sentiment_analysis_polarity = %s WHERE t.id = %s"
    elif algorithm == constant.SENTILEXPT_ALGORITHM:
        sql = "UPDATE Tweet t SET t.sentilexpt_sentiment_analysis_score = %s, t.sentilexpt_sentiment_analysis_polarity = %s WHERE t.id = %s"

    cursor.executemany(sql, parameters)
    connection.commit()

def update_scores_tweet(id, score, polarity, algorithm):
    connection, cursor = __get_connection()
    sql = ""

    if algorithm == constant.VADER_ALGORITHM:
        sql = "UPDATE Tweet t SET t.vader_sentiment_analysis_score = {}, t.vader_sentiment_analysis_polarity = '{}' WHERE t.id = {}".format(score, polarity, id)
    elif algorithm == constant.OPLEXICON_ALGORITHM:
        sql = "UPDATE Tweet t SET t.oplexicon_sentiment_analysis_score = {}, t.oplexicon_sentiment_analysis_polarity = '{}' WHERE t.id = {}".format(
            score, polarity, id)
    elif algorithm == constant.SENTISTRENGTH_ALGORITHM:
        sql = "UPDATE Tweet t SET t.sentistrength_sentiment_analysis_score = {}, t.sentistrength_sentiment_analysis_polarity = '{}' WHERE t.id = {}".format(
            score, polarity, id)
    elif algorithm == constant.SENTILEXPT_ALGORITHM:
        sql = "UPDATE Tweet t SET t.sentilexpt_sentiment_analysis_score = {}, t.sentilexpt_sentiment_analysis_polarity = '{}' WHERE t.id = {}".format(
            score, polarity, id)
    elif algorithm == constant.LIWC_ALGORITHM:
        sql = "UPDATE Tweet t SET t.liwc_sentiment_analysis_score = {}, t.liwc_sentiment_analysis_polarity = '{}' WHERE t.id = {}".format(
            score, polarity, id)

    cursor.execute(sql)
    connection.commit()


def update_overall_scores_and_polarities():
    print("updating overall scores and polarities...")
    connection, cursor = __get_connection()
    algorithm_scores = ['vader_sentiment_analysis_score',
                        'oplexicon_sentiment_analysis_score',
                        'sentistrength_sentiment_analysis_score',
                        'sentilexpt_sentiment_analysis_score',
                        'liwc_sentiment_analysis_score']

    cursor.execute('SELECT id, {} FROM Tweet'.format(",".join(algorithm_scores)))
    tweets = cursor.fetchall()

    batch_update = "UPDATE Tweet t SET t.final_score = %s, t.final_polarity = %s WHERE t.id = %s"
    parameters = []

    for t in tweets:
        id = t[0]
        scores = t[1:]
        # removing None values
        scores = [s for s in scores if s is not None]
        final_score = sum(list(map(lambda x:float(x), scores))) / len(scores)

        polarity = ''
        if final_score > 0:
            polarity = constant.POSITIVE_POLARITY
        elif final_score < 0:
            polarity = constant.NEGATIVE_POLARITY
        else:
            polarity = constant.NEUTRAL_POLARITY

        parameters.append((final_score, polarity, id))

    cursor.executemany(batch_update, parameters)
    connection.commit()


def update_ensemble_scores_and_polarities():
    print("updating ensemble scores and polarities...")
    connection, cursor = __get_connection()
    algorithm_scores = ['sentistrength_sentiment_analysis_score',
                        'sentilexpt_sentiment_analysis_score']

    cursor.execute('SELECT id, {} FROM Tweet'.format(",".join(algorithm_scores)))
    tweets = cursor.fetchall()

    batch_update = "UPDATE Tweet t SET t.final_score_ensemble = %s, t.final_polarity_ensemble = %s WHERE t.id = %s"
    parameters = []

    for t in tweets:
        id = t[0]
        scores = t[1:]
        # removing None values
        scores = [s for s in scores if s is not None]
        final_score = sum(list(map(lambda x: float(x), scores))) / len(scores)

        polarity = ''
        if final_score > 0:
            polarity = constant.POSITIVE_POLARITY
        elif final_score < 0:
            polarity = constant.NEGATIVE_POLARITY
        else:
            polarity = constant.NEUTRAL_POLARITY

        parameters.append((final_score, polarity, id))

    cursor.executemany(batch_update, parameters)
    connection.commit()