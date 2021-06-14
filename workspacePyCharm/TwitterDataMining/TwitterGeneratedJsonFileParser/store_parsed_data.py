import json
from datetime import datetime
import utils as ut
import database.MySQLConnect as db


username = 'bellesamways'


with open("json/tweet.json", "r", encoding='utf-8') as read_file:
    print("starting script...")
    user_id = db.get_user_id_str_twitter_by_screen_name(username)
    s = read_file.readlines()
    tweets = {}
    for t in s:
        j = json.loads(t)
        if not "media" in j['tweet']['entities']:
            lower_margin = datetime(2018, 3, 31)
            upper_margin = datetime(2021, 3, 31)

            date_time_obj = datetime.strptime(j['tweet']['created_at'], '%a %b %d %H:%M:%S %z %Y')
            if date_time_obj.replace(tzinfo=None) > lower_margin and date_time_obj.replace(tzinfo=None) < upper_margin:
                tweet = {}
                user = {}

                user['screen_name'] = username
                user['id_str'] = user_id

                tweet['created_at'] = j['tweet']['created_at']
                tweet['full_text'] = j['tweet']['full_text']
                tweet['favorite_count'] = j['tweet']['favorite_count']
                tweet['retweet_count'] = j['tweet']['retweet_count']
                tweet['lang'] = j['tweet']['lang']
                tweet['id_str'] = j['tweet']['id_str']

                tweet['user'] = user

                tweets[tweet['id_str']] = tweet

    tweets = ut.prepare_scrapped_tweets_to_insert(tweets)

    db.store_tweets(tweets)