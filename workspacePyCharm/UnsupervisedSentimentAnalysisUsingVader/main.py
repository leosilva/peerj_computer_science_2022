# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in
import json
from urllib.error import HTTPError

import numpy as np
import pandas as pd
import re
import database.MySQLConnect as db
from leia.leia import SentimentIntensityAnalyzer
import time


# cleaning the tweets
def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt


def clean_tweets(tweets):
    # remove twitter Return handles (RT @xxx:)
    tweets = np.vectorize(remove_pattern)(tweets, "RT @[\w]*:")

    # remove twitter handles (@xxx)
    tweets = np.vectorize(remove_pattern)(tweets, "@[\w]*")

    # remove URL links (httpxxx)
    tweets = np.vectorize(remove_pattern)(tweets, "https?://[A-Za-z0-9./]*")

    # remove special characters, numbers, punctuations (except for #)
    # tweets = np.core.defchararray.replace(tweets, "[^a-zA-Z]", " ")

    return tweets


def perform_vader_analysis(i):
    print(df['id'][i])
    print(df['text'][i])
    vader_analysis = {"vader": analyzer.polarity_scores(df['text'][i])}
    compound = analyzer.polarity_scores(df['text'][i])["compound"]
    pos = analyzer.polarity_scores(df['text'][i])["pos"]
    neu = analyzer.polarity_scores(df['text'][i])["neu"]
    neg = analyzer.polarity_scores(df['text'][i])["neg"]
    scores.append(vader_analysis)
    if compound == 0.0:
        neutral_list.append(neu)
    elif compound > 0.0:
        positive_list.append(pos)
    elif compound < 0.0:
        negative_list.append(neg)

    # compound_list.append(compound)

    # db.update_scores_tweet(df['id'][i], str(vader_analysis))


analyzer = SentimentIntensityAnalyzer()
tweets = db.get_all_tweets()


#convert array to dataframe
df = pd.DataFrame.from_dict(tweets)
df.columns = ["id", "id_str_twitter", "text", "created_at", "favorite_count", "retweet_count", "lang", "id_user", "sentiment_analysis", "screen_name"]
df['text'] = clean_tweets(df['text'])

scores = []

# Declare variables for scores
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

print("analyzing tweets with vader...")
try:
    for i in range(df['text'].shape[0]):
        # perform_vader_analysis(i)
        json_str = df['sentiment_analysis'][i]
        if json_str:
            json_str = json_str.replace("\'", "\"")
            sentiment_json = json.loads(json_str)
            if not sentiment_json['vader']:
                print(f"analysing the {i+1}º tweet")
                perform_vader_analysis(i)
        else:
            print(f"analysing the {i + 1}º tweet")
            perform_vader_analysis(i)
except HTTPError as exception:
    print(exception)
    print(exception.headers)


print("finished")
sentiments_score = pd.DataFrame.from_dict(scores)
df = df.join(sentiments_score)
print(f"Positive: {len(positive_list)}")
print(f"Negative: {len(negative_list)}")
print(f"Neutral: {len(neutral_list)}")