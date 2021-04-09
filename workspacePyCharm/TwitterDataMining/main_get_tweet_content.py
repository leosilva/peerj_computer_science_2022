import database.MySQLConnect as db
import TwitterDataCollection.TwitterAPI as tdc
import time

if __name__ == '__main__':
    print("Starting script...")
    (allusers, tweets) = db.get_all_tweets()
    for u in tweets:
        t_user = tweets[u]
        count = 1
        for t in t_user:
            if count % 100 == 0:
                print("Sleeping 60 seconds...")
                time.sleep(60)  # Sleep for 60 seconds

            tweet = {
                "id": t[0],
                "id_str_twitter": t[1],
                "text": t[2],
                "created_at": t[3],
                "favorite_count": t[4],
                "retweet_count": t[5],
                "lang": t[6],
                "id_user": t[7]
            }
            print("Nº {}. Getting full content of tweet {}".format(count, tweet['id']))
            tweet = tdc.get_tweet_content(tweet)
            db.update_tweet_text(tweet)
            count+=1
    print("Ending script...")