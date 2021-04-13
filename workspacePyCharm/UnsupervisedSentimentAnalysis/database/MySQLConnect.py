import mysql.connector
import constant


def __get_connection():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="root", db="TwitterDataMining")
    cursor = connection.cursor(buffered=True)
    return [connection, cursor]


def get_all_tweets():
    connection, cursor = __get_connection()
    cursor.execute("SELECT t.*, u.screen_name FROM Tweet t INNER JOIN User u ON t.id_user = u.id")
    tweets = cursor.fetchall()

    return tweets


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

    cursor.execute(sql)
    connection.commit()