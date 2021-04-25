import mysql.connector
from datetime import datetime
import json

def __get_connection():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="root", db="TwitterDataMining")
    cursor = connection.cursor(buffered=True)
    return [connection, cursor]


def get_last_date(screen_name):
    connection, cursor = __get_connection()

    cursor.execute("SELECT id FROM User u WHERE u.screen_name = '{}'".format(screen_name))
    id_user = cursor.fetchone()

    cursor.execute("SELECT created_at FROM Tweet t WHERE t.id_user = '{}' ORDER BY created_at".format(id_user[0]))
    last_date = cursor.fetchone()
    return last_date[0]


def update_tweet_text(tweet):
    # print("init of update tweet")
    connection, cursor = __get_connection()
    try:
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cursor.close()
        connection.close()

    try:
        query = "UPDATE Tweet t SET t.text = '{}', t.text_updated = {} WHERE id = {}".format(tweet['text'], 1, tweet['id'])
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        print("Query", query)
        cursor.close()
        connection.close()


def store_tweets_for_existing_user(alltweets):
    print("init of store tweets existing user function")
    connection, cursor = __get_connection()
    try:
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cursor.close()
        connection.close()

    for tweet in alltweets:
        # tweet = alltweets[tweet]
        id_str_tweet = tweet['id_str']

        id_str_user = tweet['user']['id_str']
        user = None
        id_user = 0
        try:
            cursor.execute("SELECT id FROM User u WHERE u.id_str_twitter = '{}'".format(id_str_user))
            user = cursor.fetchone()
            id_user = int(user[0])
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cursor.close()
            connection.close()

        try:
            cursor.execute("SELECT id FROM Tweet t WHERE t.id_str_twitter = '{}'".format(id_str_tweet))
            existing_tweet = cursor.fetchone()
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cursor.close()
            connection.close()
            break

        if existing_tweet is None:
            text = tweet['text'].replace("\'", "\"")
            text = " {} ".format(text)
            created_at = tweet['created_at']
            date_time_obj = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
            favorite_count = int(tweet['favorite_count'])
            retweet_count = int(tweet['retweet_count'])
            lang = tweet['lang']
            try:
                query = "INSERT INTO Tweet (id_str_twitter, text, created_at, favorite_count, retweet_count, lang, id_user) VALUES ('{}', '{}', '{}', {}, {}, '{}', {})".format(id_str_tweet, text, date_time_obj, favorite_count, retweet_count, lang, id_user)
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
                print("Query", query)
                cursor.close()
                connection.close()
                break

    connection.commit()
    cursor.close()
    connection.close()
    print("end of store tweets existing user function")


def store_tweets(alltweets):
    print("init of store tweets function")
    connection, cursor = __get_connection()
    try:
        cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cursor.close()
        connection.close()

    id_user = 0
    user = None

    some_tweet = alltweets[0]

    id_str_user = some_tweet['user']['id_str']
    try:
        cursor.execute("SELECT id FROM User u WHERE u.id_str_twitter = '{}'".format(id_str_user))
        user = cursor.fetchone()
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cursor.close()
        connection.close()

    if user is None:
        name = some_tweet['user']['name']
        screen_name = some_tweet['user']['screen_name']
        created_at = some_tweet['user']['created_at']
        date_time_obj = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
        url = some_tweet['user']['url']
        location = some_tweet['user']['location']
        try:
            cursor.execute("INSERT INTO User (id_str_twitter, name, screen_name, location, url, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(id_str_user, name, screen_name, location, url, date_time_obj))
            cursor.execute('SELECT last_insert_id()')
            id_user = int(cursor.fetchone()[0])
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cursor.close()
            connection.close()
    else:
        id_user = int(user[0])

    for tweet in alltweets:
        id_str_tweet = tweet['id_str']
        try:
            cursor.execute("SELECT id FROM Tweet t WHERE t.id_str_twitter = '{}'".format(id_str_tweet))
            existing_tweet = cursor.fetchone()
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cursor.close()
            connection.close()
            break

        if existing_tweet is None:
            text = tweet['text'].replace("\'", "\"")
            text = " {} ".format(text)
            created_at = tweet['created_at']
            date_time_obj = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
            favorite_count = int(tweet['favorite_count'])
            retweet_count = int(tweet['retweet_count'])
            lang = tweet['lang']
            try:
                query = "INSERT INTO Tweet (id_str_twitter, text, created_at, favorite_count, retweet_count, lang, id_user) VALUES ('{}', '{}', '{}', {}, {}, '{}', {})".format(id_str_tweet, text, date_time_obj, favorite_count, retweet_count, lang, id_user)
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
                print("Query", query)
                cursor.close()
                connection.close()
                break

    connection.commit()
    cursor.close()
    connection.close()
    print("end of store tweets function")


def get_existings_tweets_by_ids_twitter(ids_twitter):
    ids_twitter_tuple = tuple(ids_twitter)
    connection, cursor = __get_connection()

    cursor.execute("SELECT t.id_str_twitter FROM Tweet t WHERE t.id_str_twitter IN {}".format(ids_twitter_tuple))
    ids = cursor.fetchmany()

    return ids

def get_all_tweets():
    connection, cursor = __get_connection()

    cursor.execute("SELECT * FROM User u")
    allusers = cursor.fetchall()
    tweets = {}
    bigfive = {}

    for user in allusers:
        cursor.execute("SELECT * FROM Tweet t WHERE t.id_user = '{}'".format(user[0]))
        tweets[user[0]] = cursor.fetchall()

        cursor.execute("SELECT * FROM BigFiveResult b WHERE b.id_user = '{}'".format(user[0]))
        bigfive[user[0]] = cursor.fetchall()

    return (allusers, tweets, bigfive)