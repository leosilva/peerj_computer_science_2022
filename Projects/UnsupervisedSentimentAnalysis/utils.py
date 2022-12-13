from nltk.stem import RSLPStemmer
import numpy as np
import re
import math
from nltk.corpus import stopwords
from string import punctuation
from spacy.lang.pt import Portuguese


pos_scores = []
neg_scores = []
neu_scores = []
nlp = Portuguese()


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
    tweets = np.core.defchararray.replace(tweets, "[^a-zA-Z]", " ")

    return tweets


def normalize(score, alpha=15):
    """
    Normalize the score to be between -1 and 1 using an alpha that
    approximates the max expected value
    """
    norm_score = score/math.sqrt((score*score) + alpha)
    return norm_score


def print_summary_analysis(analysis_results_for_summary):
    for analysis in analysis_results_for_summary:
        print(analysis)
        if analysis > 0:
            pos_scores.append(analysis)
        elif analysis == 0:
            neu_scores.append(analysis)
        else:
            neg_scores.append(analysis)

    print('Positivos: {}'.format(len(pos_scores)))
    print('Negativos: {}'.format(len(neg_scores)))
    print('Neutros: {}'.format(len(neu_scores)))



def stemming(tweet_text):
    stemmer = RSLPStemmer()
    tweet_splitted = tweet_text.split(' ')
    phrase = []
    for word in tweet_splitted:
        if word is not '':
            phrase.append(stemmer.stem(word.lower()))
    return (" ".join(phrase))


def remove_stop_words(tweet_text):
    '''Função para remover stopwords e pontuações'''

    stop_words = stopwords.words('portuguese')

    pontuacao = list()
    for ponto in punctuation:
        pontuacao.append(ponto)

    tweet_text = nlp(tweet_text)
    palavras = [palavra.text for palavra in tweet_text if palavra.text not in stop_words and palavra.text not in pontuacao]
    return " ".join(palavras)


def remove_repeated_letters(tweet_text): # Função para remover letras repetidas
    tweet_text = nlp(tweet_text)
    palavras = list()
    for palavra in tweet_text:
        palavras.append(re.compile(r'(.)\1{1,}', re.IGNORECASE).sub(r'\1', palavra.text))
    return (" ".join(palavras))