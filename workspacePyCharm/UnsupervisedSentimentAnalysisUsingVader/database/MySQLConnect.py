import mysql.connector


def __get_connection():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="root", db="TwitterDataMining")
    cursor = connection.cursor(buffered=True)
    return [connection, cursor]


def get_all_tweets():
    connection, cursor = __get_connection()
    cursor.execute("SELECT t.*, u.screen_name FROM Tweet t INNER JOIN User u ON t.id_user = u.id")
    tweets = cursor.fetchall()

    return tweets


def update_scores_tweet(id, score):
    connection, cursor = __get_connection()
    sql = "UPDATE Tweet t SET t.sentiment_analysis = %s WHERE t.id = %s"
    val = (score, int(id))
    cursor.execute(sql, val)
    connection.commit()