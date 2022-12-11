import tweepy
from TwitterDataCollection.api_key import key
import TwitterDataCollection.TwitterAPI as tdc
import database.MySQLConnect as db


# authorize twitter, initialize tweepy
auth = tweepy.AppAuthHandler(key["consumer_key"], key['consumer_secret'])
api = tweepy.API(auth)


if __name__ == '__main__':
    print("Starting script...")
    (allusers, tweets, bigfive) = db.get_all_tweets()
    count = 1
    for u in tweets:
        t_user = tweets[u]
        for t in t_user:
            tweet = {
                "id": t[0],
                "id_str_twitter": t[1],
                "text": t[2],
                "created_at": t[3],
                "favorite_count": t[4],
                "retweet_count": t[5],
                "lang": t[6],
                "id_user": t[7],
                "text_updated": t[18]
            }
            if tweet['text'].startswith('RT @AndrewBrobston'):
                print("Nº {}. Fixing tweet text for {}".format(count, tweet['id']))
                (is_to_update, tweet) = tdc.fix_tweet_text(tweet)
                if is_to_update == True:
                    db.update_tweet_text(tweet)
                count+=1
    print("Ending script...")