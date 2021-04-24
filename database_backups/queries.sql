use TwitterDataMining;

select * from User;
select * from Tweet where lang = "pt" order by rand() limit 20;
select * from BigFiveResult;





SELECT u.screen_name,
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
       (select count(*) from Tweet t where t.final_polarity = 'pos' and t.id_user = u.id) as fim_pos,
       (select count(*) from Tweet t where t.final_polarity = 'neg' and t.id_user = u.id) as fim_neg,
       (select count(*) from Tweet t where t.final_polarity = 'neu' and t.id_user = u.id) as fim_neu
FROM User u INNER JOIN Tweet t ON u.id = t.id_user GROUP BY u.screen_name;



# Tweets positivos, negativos e neutros analisados com o VADER
select distinct
    (select count(t.id) from Tweet t where t.vader_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.vader_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.vader_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;



# Tweets positivos, negativos e neutros analisados com o Oplexicon
select distinct
    (select count(t.id) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.oplexicon_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;



# Tweets positivos, negativos e neutros analisados com o Sentistrength
select distinct
    (select count(t.id) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.sentistrength_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;



# Tweets positivos, negativos e neutros analisados com o SentilexPT
select distinct
    (select count(t.id) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'pos') as pos,
    (select count(t.id) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'neg') as neg,
    (select count(t.id) from Tweet t where t.sentilexpt_sentiment_analysis_polarity = 'neu') as neu
from Tweet t;



select count(*) from Tweet t where t.text = 'RT @AndrewBrobston: Learned this morning that today is my -- and many others';


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
 t.final_polarity = null;


select count(*) from Tweet t where t.text_updated = 0;


select * from Tweet t;


SELECT id FROM User u WHERE u.id_str_twitter = '10384742';


select count(*) from Tweet t where t.vader_sentiment_analysis_score is null;
select count(*) from Tweet t where t.oplexicon_sentiment_analysis_score is null;
select count(*) from Tweet t where t.sentistrength_sentiment_analysis_score is null;
select count(*) from Tweet t where t.sentilexpt_sentiment_analysis_score is null;
select count(*) from Tweet t where t.final_score is null;


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

select * from BigFiveResult b;
