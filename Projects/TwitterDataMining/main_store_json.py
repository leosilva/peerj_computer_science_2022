#!/usr/bin/env python3

import database.MySQLConnect as db
import json
import utils as ut


if __name__ == '__main__':
    users = [
        # 'felipperegazio',
        # 'guilh_rm_',
        # 'rponte',
        # 'nannoka',
        # 'rebelatto',
        # 'psanrosa13',
        # 'dev_jessi'
        # 'riquettinha',
        # 'Gabrielathalita'
        # 'riquettinha',
        # 'rla4'
        # 'thamyk'
        # 'felipefialho_'
        # 'juanplopes'
        # 'RaffaelDantass',
        # 'Iagor51'
        # 'RafaelMansilha'
        # 'esdras_xavieer'
        'Willian_justen'
    ]


    for u in users:
        with open("/Users/leosilva/Documents/Estudo/Doutorado/Coimbra/2019-2020/Disciplinas/Thesis/json/{}.json".format(u), "r") as read_file:
            data = json.load(read_file)
            tweets_to_insert = ut.prepare_scrapped_tweets_to_insert(data)
            tweets_to_insert = ut.remove_tweets_containing_media(tweets_to_insert)
            db.store_tweets(tweets_to_insert)
            # for d in data:
            #     json = data[d]
            #     print(json["created_at"])
        # tweets_to_insert = prepare_scrapped_tweets_to_insert(tweets)
        # tweets_to_insert = remove_tweets_containing_media(tweets_to_insert)
        # db.store_tweets(tweets_to_insert)