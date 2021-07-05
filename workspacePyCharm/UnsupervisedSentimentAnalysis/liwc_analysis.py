import pandas as pd
import numpy as np
import math
import emoticon_analysis as ea
import constant


def normalize(score, minimum, maximum):
    y = (score - minimum) / (maximum - minimum)
    return y


def read_file():
    data = pd.read_csv(r'/Users/leosilva/Documents/Estudo/Doutorado/Coimbra/2019-2020/Disciplinas/Thesis/LIWC2015_Results_for_Tweets.csv', decimal=',')
    data.columns = ['id', 'text', 'posemo', 'negemo']
    return data


def normalize_emotion_score(data):
    minimum = min(data['posemo'])
    maximum = max(data['posemo'])
    data['posemo_normalized'] = [normalize(float(d), minimum, maximum) for d in data['posemo']]
    minimum = min(data['negemo'])
    maximum = max(data['negemo'])
    data['negemo_normalized'] = [normalize(float(d), minimum, maximum) for d in data['negemo']]
    return data


def calculate_final_score(data):
    for i in data.index:
        pos_score = data.iloc[i]['posemo_normalized']
        neg_score = data.iloc[i]['negemo_normalized']
        text = data.iloc[i]['text']
        final_score = pos_score - neg_score
        l_sentiment = ea.emoji_score(text)

        if len(l_sentiment) > 0:
            score_sum = final_score + sum(l_sentiment)
            size = len(l_sentiment) + 1
            final_score = score_sum / size

        if float(final_score) > 1.0:
            final_score = 1.0
        elif float(final_score) < -1.0:
            final_score = -1.0

        data.at[i, 'final_score'] = final_score

    return data


def calculate_polarities(data):
    # create a list of our conditions
    conditions = [
        (data['final_score'] < 0.0),
        (data['final_score'] == 0.0),
        (data['final_score'] > 0.0)
        ]

    # create a list of the values we want to assign for each condition
    values = [constant.NEGATIVE_POLARITY,
              constant.NEUTRAL_POLARITY,
              constant.POSITIVE_POLARITY]

    # create a new column and use np.select to assign values to it using our lists as arguments
    data['final_polarity'] = np.select(conditions, values)

    return data


def run_liwc_analysis():
    data = read_file()
    data = normalize_emotion_score(data)
    data = calculate_final_score(data)
    data = calculate_polarities(data)
    return data

# [OK] 1 - FAZER A CONTAGEM DAS POLARIDADES CONSIDERANDO OS EMOTICONS
# 2 - SALVAR AS POLARIDADES NO BANCO DE DADOS