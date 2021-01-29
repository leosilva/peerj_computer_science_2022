import mysql.connector


def __get_connection():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="root", db="TwitterDataMining")
    cursor = connection.cursor(buffered=True)
    return [connection, cursor]

def get_all_tweets():
    connection, cursor = __get_connection()
    cursor.execute("SELECT t.* FROM Tweet t")
    tweets = cursor.fetchmany()

    return tweets