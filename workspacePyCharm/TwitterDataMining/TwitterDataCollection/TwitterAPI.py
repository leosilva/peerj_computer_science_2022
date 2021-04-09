import json
import tweepy
import csv
from TwitterDataCollection.api_key import key
import re

# Twitter only allows access to a users most recent 3240 tweets with this method

# authorize twitter, initialize tweepy
auth = tweepy.AppAuthHandler(key["consumer_key"], key['consumer_secret'])
api = tweepy.API(auth)

def get_tweet_content(tweet):
    status = api.get_status(tweet['id_str_twitter'], tweet_mode="extended", wait_on_rate_limit=True)
    try:
        text = re.search(r"RT @[\w]*:", tweet['text']).group(0) + " "
        tweet['text'] = text + status.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        tweet['text'] = status.full_text
    return tweet

def get_all_tweets(screen_name):

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")

    return alltweets