import emosent as em


em.EMOJI_SENTIMENT_DICT['❤️'] = {'unicode_codepoint': '0x2764', 'occurrences': 8050, 'position': 0.746943086, 'negative': 355.0, 'neutral': 1334.0, 'positive': 6361.0, 'unicode_name': 'HEAVY BLACK HEART', 'unicode_block': 'Dingbats', 'sentiment_score': 0.746}

emoji_list = list(em.EMOJI_SENTIMENT_DICT.keys())

def emoji_score(text):
    l_sentiment = []
    word_list = text.split(' ')
    for w in word_list:
        if w in emoji_list:
            l_sentiment.append(em.get_emoji_sentiment_rank(w)['sentiment_score'])

    # score = 0
    # if len(l_sentiment) > 1:
    #     score = sum(l_sentiment) / len(l_sentiment)
    # else:
    #     score = sum(l_sentiment)

    return l_sentiment