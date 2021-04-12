import re
from spacy.lang.pt import Portuguese


dic_palavra_polaridade = {}
oplexicon = open('oplexicon_v3.0/lexico_v3.0.txt', 'r')
nlp = Portuguese()


for i in oplexicon.readlines():
    linha_splitted = i.split(',')
    palavra = linha_splitted[0]
    polaridade = linha_splitted[2]
    dic_palavra_polaridade['{}'.format(palavra)] = polaridade


def score_sentimento(frase):
    frase = frase.lower()
    l_sentimento = []
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