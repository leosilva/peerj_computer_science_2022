#!/usr/bin/env python3

import TwitterDataCollection.TwitterAPI as tdc
import TwitterDataCollection.TwitterScraper as scraper
import database.MySQLConnect as db
from datetime import datetime
import argparse


def verify_necessity_more_tweets(screen_name, year, month, day):
    last_date = db.get_last_date(screen_name)
    base_date = datetime(year, month, day)
    if last_date > base_date:
        return True
    else:
        return False


def scrap_tweets(screen_name, since_date):
    last_date = db.get_last_date(screen_name)
    sc = scraper.Scraper(screen_name)
    sc.scrape(since_date, last_date, 7, 3)
    return sc.tweets


def prepare_scrapped_tweets_to_insert(tweets):
    ids_twitter = []
    for tweet in tweets:
        ids_twitter.append(tweets[tweet]["id_str"])
    existing_ids = db.get_existings_tweets_by_ids_twitter(ids_twitter)
    if existing_ids:
        tweets_to_insert = [tweets[tweet] for tweet in tweets if tweets[tweet]["id_str"] not in existing_ids[0]]
    else:
        tweets_to_insert = tweets
    for t in tweets_to_insert:
        t["text"] = t["full_text"]
    return tweets_to_insert


def fetch_tweets_by_screen_name(screen_name, since_date):
    alltweets = tdc.get_all_tweets(screen_name)
    db.store_tweets([tweet._json for tweet in alltweets])
    is_need_more_tweets = verify_necessity_more_tweets(screen_name, int(since_date.year), int(since_date.month), int(since_date.day))
    if is_need_more_tweets:
        print("scrapping more tweets...")
        tweets = scrap_tweets(screen_name, since_date)
        tweets_to_insert = prepare_scrapped_tweets_to_insert(tweets)
        db.store_tweets(tweets_to_insert)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py", usage="python3 %(prog)s [options]")
    parser.add_argument("-u", "--username", required=True)
    parser.add_argument("--since", required=True)
    args = parser.parse_args()

    since = datetime.strptime(args.since, '%Y-%m-%d')
    fetch_tweets_by_screen_name(args.username, since)