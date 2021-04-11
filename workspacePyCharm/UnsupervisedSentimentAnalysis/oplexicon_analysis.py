# nltk.download('stopwords')
# nltk.download('rslp')
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import re
import math
from string import punctuation
from spacy.lang.pt import Portuguese


pos_scores = []
norm_pos_scores = []
neg_scores = []
norm_neg_scores = []
neu_scores = []


dic_palavra_polaridade = {}
oplexicon = open('oplexicon_v3.0/lexico_v3.0.txt', 'r')
nlp = Portuguese()


for i in oplexicon.readlines():
    linha_splitted = i.split(',')
    palavra = linha_splitted[0]
    polaridade = linha_splitted[2]
    dic_palavra_polaridade['{}'.format(palavra)] = polaridade


def normalize(score, alpha=15):
    """
    Normalize the score to be between -1 and 1 using an alpha that
    approximates the max expected value
    """
    norm_score = score/math.sqrt((score*score) + alpha)
    return norm_score


def score_sentimento(frase):
    frase = frase.lower()
    l_sentimento = []
    for p in frase.split():
        l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))
    score = sum(l_sentimento)
    return score


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
        if palavra.text not in list(dic_palavra_polaridade.keys()):
            palavras.append(re.compile(r'(.)\1{1,}', re.IGNORECASE).sub(r'\1', palavra.text))
        else:
            palavras.append(palavra.text)
    return (" ".join(palavras))


def stemming(tweet_text):
    stemmer = RSLPStemmer()
    tweet_splitted = tweet_text.split(' ')
    phrase = []
    for word in tweet_splitted:
        if word is not '':
            phrase.append(stemmer.stem(word.lower()))
    return (" ".join(phrase))


def print_summary_analysis(analysis_results_for_summary):
    for oplexicon_analysis in analysis_results_for_summary:
        if oplexicon_analysis > 0:
            pos_scores.append(oplexicon_analysis)
            oplexicon_analysis = round(normalize(oplexicon_analysis))
            norm_pos_scores.append(oplexicon_analysis)
        elif oplexicon_analysis == 0:
            neu_scores.append(oplexicon_analysis)
        else:
            neg_scores.append(oplexicon_analysis)
            oplexicon_analysis = round(normalize(oplexicon_analysis))
            norm_neg_scores.append(oplexicon_analysis)

    print('Positivos: {}'.format(len(pos_scores)))
    print('Negativos: {}'.format(len(neg_scores)))
    print('Neutros: {}'.format(len(neu_scores)))