from nrclex import NRCLex
import text2emotion as te
from translate import Translator


text = "NOVA ANTECIPAÇÃO Boa tarde, pessoal! Por uma questão logística, estamos antecipando mais uma vez a faixa de vacinação. Nesta quinta, já vacinaremos quem tem 70 anos. Com a abertura de novos postos de vacinação, temos percebido a capacidade do sistema de vacinar mais pessoas..."

translator= Translator(to_lang="en")
print(translator.available_providers)
result = translator.translate(text)

print("NRCLEX")
print('----------')
text_object = NRCLex(result)

print(text_object.words)
print(text_object.sentences)
print(text_object.affect_list)
print(text_object.affect_dict)
print(text_object.raw_emotion_scores)
print(text_object.top_emotions)
print(text_object.affect_frequencies)

print("text2emotion")
print('----------')

print(te.get_emotion(result))