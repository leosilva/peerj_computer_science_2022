# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
str = "VADER é esperto, bonito, e engraçado."
print(f"{str} -> {analyzer.polarity_scores(str)}")

str = "Eu estou feliz"
print(f"{str} -> {analyzer.polarity_scores(str)}")

str = "Eu estou feliz :)"
print(f"{str} -> {analyzer.polarity_scores(str)}")

str = "Eu estou feliz!"
print(f"{str} -> {analyzer.polarity_scores(str)}")

str = "Eu não estou feliz!"
print(f"{str} -> {analyzer.polarity_scores(str)}")

str = "Eu estou 😄"
print(f"{str} -> {analyzer.polarity_scores(str)}")