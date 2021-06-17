import database.MySQLConnect as db
import json
from datetime import date, datetime
import os
import argparse

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
        result_dict[user[0]] = {
            "id_str_twitter": user[1],
            "name" : user[2],
            "screen_name" : user[3],
            "location" : user[4],
            "url" : user[5],
            "created_at": str(user[6]),
            "tweets" : tweets[user[0]],
            "bigfive" : bigfive[user[0]]
        }

    if os.path.exists(file):
        print("Removing existing file...")
        os.remove(file)
    with open(file, 'w') as outfile:
        json.dump(result_dict, outfile, default=json_serial)

    print("Ending script...")