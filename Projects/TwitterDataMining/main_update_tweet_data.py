import database.MySQLConnect as db
import TwitterDataCollection.TwitterAPI as tdc
import time

if __name__ == '__main__':
    print("Starting script...")
    (allusers, tweets, bigfive) = db.get_all_tweets()
    for u in tweets:
        t_user = tweets[u]
        count = 1
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
                "text_updated": t[18],
                "retweet_updated": t[20]
            }
            if tweet['text_updated'] == 0 or tweet['retweet_updated'] == 0:
                print("Nº {}. Getting full content of tweet {}".format(count, tweet['id']))
                (tweet, is_retweet) = tdc.update_tweet_data(tweet)
                tweet['text'] = tweet['text'].replace("'", "''")
                db.update_tweet_text(tweet)
                db.update_retweet_status(tweet, is_retweet)
                count+=1
    print("Ending script...")