#!/usr/bin/env python3

import TwitterDataCollection.TwitterAPI as tdc
import TwitterDataCollection.TwitterScraper as scraper
import database.MySQLConnect as db
from datetime import datetime
import argparse
import json


def verify_necessity_more_tweets(screen_name, year, month, day):
    last_date = db.get_last_date(screen_name)
    base_date = datetime(year, month, day)
    if last_date > base_date:
        return True
    else:
        return False


def scrap_tweets(screen_name, since_date, until, isFromApi):
    if isFromApi:
        last_date = db.get_last_date(screen_name)
    else:
        last_date = until
    sc = scraper.Scraper(screen_name)
    sc.scrape(since_date, last_date, 7, 3)
    return sc.tweets


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


def fetch_tweets_by_screen_name(screen_name, since_date, until, isFromApi):
    if isFromApi == "True":
        print("fetching tweets from api...")
        alltweets = tdc.get_all_tweets(screen_name)
        alltweets = remove_tweets_containing_media(alltweets)
        # for a in alltweets:
        #     a._json = tdc.get_tweet_content(a._json)
        db.store_tweets([tweet._json for tweet in alltweets])
        # is_need_more_tweets = verify_necessity_more_tweets(screen_name, int(since_date.year), int(since_date.month), int(since_date.day))
        # is_need_more_tweets = True
        # if is_need_more_tweets:
        #     print("scrapping more tweets...")
        #     tweets = scrap_tweets(screen_name, since_date, until, isFromApi)
        #     tweets_to_insert = prepare_scrapped_tweets_to_insert(tweets)
        #     tweets_to_insert = remove_tweets_containing_media(tweets_to_insert)
        #     db.store_tweets(tweets_to_insert)
    else:
        print("scrapping tweets...")
        tweets = scrap_tweets(screen_name, since_date, until, isFromApi)
        tweets_to_insert = prepare_scrapped_tweets_to_insert(tweets)
        tweets_to_insert = remove_tweets_containing_media(tweets_to_insert)
        db.store_tweets(tweets_to_insert)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py", usage="python3 %(prog)s [options]")
    parser.add_argument("-u", "--username", required=True)
    parser.add_argument("--api", required=True, help="Get Tweets from api? True or False")
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", help="Get Tweets before this date (Example: 2018-12-07).", required=True)
    args = parser.parse_args()

    since = datetime.strptime(args.since, '%Y-%m-%d')
    until = datetime.strptime(args.until, '%Y-%m-%d')
    fetch_tweets_by_screen_name(args.username, since, until, args.api)