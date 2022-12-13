import database.MySQLConnect as db
import datetime

(allusers, tweets, bigfive) = db.get_all_tweets()

is_work_time = {
    1: [],
    0: []
}
for u in tweets:
    if bigfive[u]:
        t_user = tweets[u]
        for t in t_user:
            d = t[3]
            date_from = datetime.datetime(year=d.year, month=d.month, day=d.day, hour=9)
            date_to = datetime.datetime(year=d.year, month=d.month, day=d.day, hour=18)
            if date_from <= d <= date_to and d.weekday() in [0, 1, 2, 3, 4]:
                is_work_time[1].append(t)
            else:
                is_work_time[0].append(t)
            # print(t[3])
            # break

print(len(is_work_time[1]))
print(len(is_work_time[0]))