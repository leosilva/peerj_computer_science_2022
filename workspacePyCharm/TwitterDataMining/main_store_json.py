#!/usr/bin/env python3

import TwitterDataCollection.TwitterAPI as tdc
import TwitterDataCollection.TwitterScraper as scraper
import database.MySQLConnect as db
from datetime import datetime
import argparse
import json


def prepare_scrapped_tweets_to_insert(tweets):
    ids_twitter = []
    for tweet in tweets:
        ids_twitter.append(tweets[tweet]["id_str"])
    if ids_twitter:
        existing_ids = db.get_existings_tweets_by_ids_twitter(ids_twitter)
        if existing_ids:
            tweets_to_insert = [tweets[tweet] for tweet in tweets if tweets[tweet]["id_str"] not in existing_ids[0]]
        else:
            tweets_to_insert = tweets
    else:
        tweets_to_insert = tweets
    for t in tweets_to_insert:
        t["text"] = t["full_text"]
    return tweets_to_insert


def remove_tweets_containing_media(tweets):
    for t in tweets:
        # images are in "entities" key
        # if type is dict it came from scraper
        if type(t) is dict:
            entities = t["entities"]
        # if not, it came from api
        else:
            entities = t._json["entities"]
        if "media" in entities:
            # remove tweets that has any media (gif, video or photo)
            tweets.remove(t)
    return tweets


if __name__ == '__main__':
    with open("json/psanrosa13.json", "r") as read_file:
        data = json.load(read_file)
        tweets_to_insert = prepare_scrapped_tweets_to_insert(data)
        tweets_to_insert = remove_tweets_containing_media(tweets_to_insert)
        db.store_tweets_for_existing_user(tweets_to_insert)
        # for d in data:
        #     json = data[d]
        #     print(json["created_at"])
    # tweets_to_insert = prepare_scrapped_tweets_to_insert(tweets)
    # tweets_to_insert = remove_tweets_containing_media(tweets_to_insert)
    # db.store_tweets(tweets_to_insert)