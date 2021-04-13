import re
from spacy.lang.pt import Portuguese
from nltk import word_tokenize
from nltk.util import ngrams
# import nltk
# nltk.download('punkt')


dic_palavra_polaridade = {}
dic_flex_polaridade = {}

sentilex_pt_lem = open('sentilex-pt/SentiLex-lem-PT02.txt', 'r')
sentilex_pt_flex = open('sentilex-pt/SentiLex-flex-PT02.txt', 'r')
nlp = Portuguese()


def create_dictionaries():
    print("creating dictionaries...")

    for i in sentilex_pt_lem.readlines():
        linha_splitted = i.split('.')
        options = linha_splitted[1].split(';')
        polaridade = options[2].split('=')[1]
        palavra = linha_splitted[0]
        dic_palavra_polaridade['{}'.format(palavra)] = polaridade

    for i in sentilex_pt_flex.readlines():
        linha_splitted = i.split('.')
        options = linha_splitted[1].split(';')
        polaridade = options[3].split('=')[1]
        palavras = linha_splitted[0].split(',')
        for p in palavras:
            expressoes = p.split(' ')
            if len(expressoes) == 1 and p not in dic_palavra_polaridade:
                dic_palavra_polaridade['{}'.format(p)] = polaridade
            elif len(expressoes) > 1:
                dic_flex_polaridade['{}'.format(p)] = polaridade


def sentiment_score(frase):
    frase = frase.lower()
    l_sentimento = []

    for d in dic_flex_polaridade:
        if d in frase:
            d_splitted = d.split(' ')
            token = word_tokenize(frase)
            bigram = list(ngrams(token, len(d_splitted)))
            for b in bigram:
                t = ' '.join(b)
                if t == d:
                    l_sentimento.append(int(dic_flex_polaridade.get(d, 0)))
                    frase = frase.replace(d, '')

    for p in frase.split():
        l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))

    score = sum(l_sentimento)
    return score


def remove_repeated_letters(tweet_text): # Função para remover letras repetidas
    tweet_text = nlp(tweet_text)
    palavras = list()
    for palavra in tweet_text:
        if palavra.text not in list(dic_palavra_polaridade.keys()):
            palavras.append(re.compile(r'(.)\1{1,}', re.IGNORECASE).sub(r'\1', palavra.text))
        else:
            palavras.append(palavra.text)
    return (" ".join(palavras))