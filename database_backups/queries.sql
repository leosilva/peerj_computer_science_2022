use TwitterDataMining;

select * from User;
select * from Tweet where lang = "pt" order by rand() limit 20;
select count(*) from Tweet t where t.text_updated = 0 or t.retweet_updated = 0;
select * from BigFiveResult;


select count(t.id)
from Tweet t inner join User U on t.id_user = U.id inner join BigFiveResult BFR on U.id = BFR.id_user;



select count(*) from Tweet t where t.retweet_updated = 0;
select count(*) from Tweet t where t.text_updated = 0;


select
       u.id as id_user,
       u.screen_name,
       (select count(*) from Tweet tw where tw.id_user = u.id) as total_tweets,
       count(t.id) as retweets
from Tweet t inner join User u on t.id_user = u.id
where t.is_retweet = 1
group by u.screen_name;


select count(*) from Tweet t where t.is_retweet = 1;


# SELECAO ALEATORIA DE TWEETS POR DETERMINADO TRIMESTRE, USUARIO E POLARIDADE
select * from Tweet t INNER JOIN User u on t.id_user = u.id
where t.created_at between "2018-03-31 23:59:59" and "2018-07-01 23:59:59"
and u.id = 26
and t.final_polarity = 'pos'
order by rand() LIMIT 10;

# QTD TWEETS DOS USUARIOS QUE POSSUEM BIG FIVE RESPONDIDO: 46165
select count(*) from Tweet t inner join User u on t.id_user = u.id
inner join BigFiveResult bf on u.id = bf.id_user;

# QTD TWEETS DOS USUARIOS QUE NÃO POSSUEM BIG FIVE RESPONDIDO: 15322
select count(*) from Tweet t inner join User u on t.id_user = u.id
left join BigFiveResult bf on u.id = bf.id_user where bf.id_user is null;


SELECT u.id,
       u.screen_name,
       count(*) as total,
       (select count(*) from Tweet t where t.vader_sentiment_analysis_polarity = 'pos' and t.id_user = u.id) as pos_vad,
       (select count(*) from Tweet t where t.vader_sentiment_analysis_polarity = 'neg' and t.id_user = u.id) as neg_vad,
       (select count(*) from Tweet t where t.vader_sentiment_analysis_polarity = 'neu' and t.id_user = u.id) as neu_vad,
       (select count(*) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'pos' and t.id_user = u.id) as pos_opl,
       (select count(*) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neg' and t.id_user = u.id) as neg_opl,
       (select count(*) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neu' and t.id_user = u.id) as neu_opl,
       (select count(*) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'pos' and t.id_user = u.id) as pos_str,
       (select count(*) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'neg' and t.id_user = u.id) as neg_str,
       (select count(*) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'neu' and t.id_user = u.id) as neu_str,
       (select count(*) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'pos' and t.id_user = u.id) as pos_stl,
       (select count(*) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'neg' and t.id_user = u.id) as neg_stl,
       (select count(*) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'neu' and t.id_user = u.id) as neu_stl,
       (select count(*) from Tweet t where t.final_polarity = 'pos' and t.id_user = u.id) as fin_pos,
       (select count(*) from Tweet t where t.final_polarity = 'neg' and t.id_user = u.id) as fin_neg,
       (select count(*) from Tweet t where t.final_polarity = 'neu' and t.id_user = u.id) as fin_neu,
       (select count(*) from Tweet t where t.is_retweet = 1 and t.id_user = u.id) as is_retweet
FROM User u INNER JOIN Tweet t ON u.id = t.id_user GROUP BY u.screen_name;



select
       count(*) total,
       (select te.vader_sentiment_analysis_polarity from Tweet te where te.id = t.id) as pol
from Tweet t
where t.vader_sentiment_analysis_score between -0.05 and 0.05
group by pol;

select
       count(*) total,
       (select te.oplexicon_sentiment_analysis_polarity from Tweet te where te.id = t.id) as pol
from Tweet t
where t.oplexicon_sentiment_analysis_score between -0.05 and 0.05
group by pol;


select
       count(*) total,
       (select te.sentistrength_sentiment_analysis_polarity from Tweet te where te.id = t.id) as pol
from Tweet t
where t.sentistrength_sentiment_analysis_score between -0.05 and 0.05
group by pol;


select
       count(*) total,
       (select te.sentilexpt_sentiment_analysis_polarity from Tweet te where te.id = t.id) as pol
from Tweet t
where t.sentilexpt_sentiment_analysis_polarity between -0.05 and 0.05
group by pol;


# Tweets positivos, negativos e neutros analisados com o VADER
select distinct
    (select count(t.id) from Tweet t where t.vader_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.vader_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.vader_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;
# pos: 15740, neg: 16504, neu:11907



# Tweets positivos, negativos e neutros analisados com o Oplexicon
select distinct
    (select count(t.id) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;
# pos: 20393, neg: 8536, neu: 15222


# Tweets positivos, negativos e neutros analisados com o Sentistrength
select distinct
    (select count(t.id) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;
# pos: 14066, neg: 9546, neu: 20539



# Tweets positivos, negativos e neutros analisados com o SentilexPT
select distinct
    (select count(t.id) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;
# pos: 14212, neg: 10992, neu: 18947


select * from Tweet tw where tw.text like '%Learned this morning that today is my -- and many others';


select * from Tweet t where t.text like 'RT @AndrewBrobston%';


update Tweet t SET t.retweet_updated = 1;


update Tweet t SET
 t.vader_sentiment_analysis_polarity = null,
 t.vader_sentiment_analysis_score = null,
 t.oplexicon_sentiment_analysis_polarity = null,
 t.oplexicon_sentiment_analysis_score = null,
 t.sentistrength_sentiment_analysis_polarity = null,
 t.sentistrength_sentiment_analysis_score = null,
 t.sentilexpt_sentiment_analysis_polarity = null,
 t.sentilexpt_sentiment_analysis_score = null,
 t.final_score = null,
 t.final_polarity = null
WHERE t.id in (104438,
110584,
113522,
120400,
124944,
127591,
128162,
129215,
142894,
145035,
153560
);

       (select count(*) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'neu' and t.id_user = u.id) as neu_stl
FROM User u INNER JOIN Tweet t ON u.id = t.id_user GROUP BY u.screen_name;


select count(*) from Tweet t where t.text_updated = 0;


select * from Tweet t inner join User U on t.id_user = U.id where u.screen_name = 'thamyk';


update Tweet t SET
 t.oplexicon_sentiment_analysis_polarity = null,
 t.oplexicon_sentiment_analysis_score = null,
#  t.sentistrength_sentiment_analysis_polarity = null,
#  t.sentistrength_sentiment_analysis_score = null,
#  t.sentilexpt_sentiment_analysis_polarity = null,
#  t.sentilexpt_sentiment_analysis_score = null,
 t.final_score = null,
 t.final_polarity = null;


SELECT id FROM User u WHERE u.id_str_twitter = '10384742';


select count(*) from Tweet t where t.vader_sentiment_analysis_score is null;
select count(*) from Tweet t where t.oplexicon_sentiment_analysis_score is null;
select count(*) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'pos'; # 1282
select count(*) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neg'; # 583
select count(*) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neu'; # 42286
select count(*) from Tweet t where t.sentistrength_sentiment_analysis_score is null;
select count(*) from Tweet t where t.sentilexpt_sentiment_analysis_score is null;
select count(*) from Tweet t where t.final_score is null;

select count(*) from Tweet t where t.final_polarity = 'pos'; # 15630
select count(*) from Tweet t where t.final_polarity = 'neg'; # 16042
select count(*) from Tweet t where t.final_polarity = 'neu'; # 12479


select t.created_at from Tweet t
inner join User u on t.id_user = u.id
where u.screen_name = "rla4"
order by t.created_at desc;

SHOW ENGINE INNODB STATUS;

show open tables where in_use>0;

# ERASE DATABASE
delete from Tweet t;
delete from BigFiveResult b;
delete from User u;

delete from Tweet t
where t.id_user in (select u.id from User u where u.screen_name = 'nannoka');

delete from User u where u.screen_name = 'nannoka';

ALTER TABLE User AUTO_INCREMENT = 1;

SELECT count(*) FROM Tweet t
WHERE t.created_at > "2021-03-31 23:59:59";


SELECT count(*) FROM Tweet t where t.lang = 'pt';

SELECT t.* FROM Tweet t inner join User u on t.id_user = u.id WHERE u.id = 15
ORDER BY t.created_at desc;

# NECESSARY DELETES
delete from Tweet t where t.lang <> 'pt';
select * from Tweet t where t.lang <> 'pt';
delete from Tweet t where t.created_at < "2018-04-01 00:00:00";
select * from Tweet t where t.created_at < "2018-04-01 00:00:00";
delete from Tweet t where t.created_at > "2021-03-31 23:59:59";
select * from Tweet t where t.created_at > "2021-03-31 23:59:59";

INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (22, 33, 31, 20, 8, (SELECT u.id from User u where u.screen_name = 'rponte'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (43, 46, 31, 24, 15, (SELECT u.id from User u where u.screen_name = 'FelippeRegazio'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (41, 43, 34, 22, 23, (SELECT u.id from User u where u.screen_name = 'Guilh_rm_'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (37, 43, 36, 24, 26, (SELECT u.id from User u where u.screen_name = 'rebelatto'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (29, 45, 34, 35, 29, (SELECT u.id from User u where u.screen_name = 'Gabrielathalita'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (35, 35, 32, 26, 16, (SELECT u.id from User u where u.screen_name = 'rla4'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (40, 46, 38, 22, 21, (SELECT u.id from User u where u.screen_name = 'felipefialho_'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (17,	33,	33,	22,	39, (SELECT u.id from User u where u.screen_name = 'psanrosa13'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (32,	46,	19,	18,	28, (SELECT u.id from User u where u.screen_name = 'juanplopes'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (31,	36,	25,	33,	21, (SELECT u.id from User u where u.screen_name = 'RaffaelDantass'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (36,	45,	31,	31,	19, (SELECT u.id from User u where u.screen_name = 'Iagor51'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (29,	41,	28,	22,	28, (SELECT u.id from User u where u.screen_name = 'RafaelMansilha'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (39,	49,	39,	28,	15, (SELECT u.id from User u where u.screen_name = 'dev_jessi'));




select u.screen_name,
       count(t.id) as total,
       (select * from Tweet tw where tw.id_user = u.id order by rand() limit 20) as limite
from Tweet t
    inner join User u on t.id_user = u.id
    inner join BigFiveResult b on u.id = b.id_user
group by u.screen_name;


(select
       t.id,
       t.text
from Tweet t
where t.id_user = 26
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 27
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 28
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 30
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 31
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 34
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 35
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 37
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 38
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 39
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 40
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 41
group by t.id
order by rand() limit 35)
union
(select
       t.id,
       t.text
from Tweet t
where t.id_user = 42
group by t.id
order by rand() limit 35)


select distinct b.*, u.screen_name, u.id
from BigFiveResult b inner join user u on u.id = b.id_user;



