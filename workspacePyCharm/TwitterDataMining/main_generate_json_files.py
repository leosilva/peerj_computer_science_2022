import database.MySQLConnect as db
import json
from datetime import date, datetime
import os
import argparse


def flatten(t):
    """
    Generator flattening the structure

    >>> list(flatten([2, [2, "test", (4, 5, [7], [2, [6, 2, 6, [6], 4]], 6)]]))
    [2, 2, "test", 4, 5, 7, 2, 6, 2, 6, 6, 4, 6]
    """
    from collections.abc import Iterable
    for x in t:
        if isinstance(x, str) or not isinstance(x, Iterable):
            yield x
        else:
            yield from flatten(x)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="main.py", usage="python3 %(prog)s [options]")
    parser.add_argument("--all_tweets", required=True)
    args = parser.parse_args()
    file = "/Users/leosilva/development/thesis/workspacePyCharm/TwitterDataMining/alldata.json"
    print("Starting script...")
    if args.all_tweets == 'True':
        (allusers, tweets, bigfive) = db.get_all_tweets()
    elif args.all_tweets == 'False':
        (allusers, tweets, bigfive) = db.get_tweets_by_retweet(0)
    result_dict = {}
    for user in allusers:
        filtered_tweets = []
        for t in tweets[user[0]]:
            temp_list = [t[0], t[2], t[3], t[7]]
            temp_list.append(t[8:30])
            filtered_tweets.append(list(flatten(temp_list)))
        result_dict[user[0]] = {
            # "id_str_twitter": user[1],
            "participant_id": user[2],
            # "name" : user[3],
            # "screen_name" : user[4],
            # "location" : user[5],
            # "url" : user[6],
            "created_at": str(user[7]),
            "tweets" : filtered_tweets,
            "bigfive" : bigfive[user[0]]
        }

    if os.path.exists(file):
        print("Removing existing file...")
        os.remove(file)
    with open(file, 'w') as outfile:
        json.dump(result_dict, outfile, default=json_serial)

    print("Ending script...")