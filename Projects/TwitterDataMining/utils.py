import database.MySQLConnect as db


def prepare_scrapped_tweets_to_insert(tweets):
    print("preparing tweets to insert...")
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
    new_tweets_to_insert = []
    for t in tweets_to_insert:
        tweet = {}
        if type(t) is str:
            tweet = tweets_to_insert[t]
        else:
            tweet = t
        tweet["text"] = tweet["full_text"]
        new_tweets_to_insert.append(tweet)
    return new_tweets_to_insert


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