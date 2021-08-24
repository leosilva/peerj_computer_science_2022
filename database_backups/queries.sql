use TwitterDataMining;

select * from User;
select * from Tweet t where id = 102566;

update User u set u.participant_id = null;
update User u set u.participant_id = 1 where u.id = 26;
update User u set u.participant_id = 2 where u.id = 27;
update User u set u.participant_id = 3 where u.id = 28;
update User u set u.participant_id = 4 where u.id = 30;
update User u set u.participant_id = 5 where u.id = 31;
update User u set u.participant_id = 6 where u.id = 32;
update User u set u.participant_id = 7 where u.id = 34;
update User u set u.participant_id = 8 where u.id = 35;
update User u set u.participant_id = 9 where u.id = 37;
update User u set u.participant_id = 10 where u.id = 38;
update User u set u.participant_id = 11 where u.id = 39;
update User u set u.participant_id = 12 where u.id = 40;
update User u set u.participant_id = 13 where u.id = 41;
update User u set u.participant_id = 14 where u.id = 42;
update User u set u.participant_id = 15 where u.id = 43;
update User u set u.participant_id = 16 where u.id = 44;

-- UPDATES FOR VADER 5 CATEGORIES
update Tweet t
set t.vader_sentiment_analysis_polarity_5_cat = 's_pos'
WHERE vader_sentiment_analysis_score > 0.5;
update Tweet t
set t.vader_sentiment_analysis_polarity_5_cat = 'w_pos'
WHERE t.vader_sentiment_analysis_score BETWEEN 0.0001 AND 0.5;
update Tweet t
set t.vader_sentiment_analysis_polarity_5_cat = 'neu'
WHERE t.vader_sentiment_analysis_score = 0.0;
update Tweet t
set t.vader_sentiment_analysis_polarity_5_cat = 'w_neg'
WHERE t.vader_sentiment_analysis_score BETWEEN -0.5 AND -0.0001;
update Tweet t
set t.vader_sentiment_analysis_polarity_5_cat = 's_neg'
WHERE t.vader_sentiment_analysis_score < -0.5;

-- UPDATE FOR OPLEXICON 5 CATEGORIES
update Tweet t
set t.oplexicon_sentiment_analysis_polarity_5_cat = 's_pos'
WHERE oplexicon_sentiment_analysis_score > 0.5;
update Tweet t
set t.oplexicon_sentiment_analysis_polarity_5_cat = 'w_pos'
WHERE t.oplexicon_sentiment_analysis_score BETWEEN 0.0001 AND 0.5;
update Tweet t
set t.oplexicon_sentiment_analysis_polarity_5_cat = 'neu'
WHERE t.oplexicon_sentiment_analysis_score = 0.0;
update Tweet t
set t.oplexicon_sentiment_analysis_polarity_5_cat = 'w_neg'
WHERE t.oplexicon_sentiment_analysis_score BETWEEN -0.5 AND -0.0001;
update Tweet t
set t.oplexicon_sentiment_analysis_polarity_5_cat = 's_neg'
WHERE t.oplexicon_sentiment_analysis_score < -0.5;


-- UPDATE FOR SENTISTRENGTH 5 CATEGORIES
update Tweet t
set t.sentistrength_sentiment_analysis_polarity_5_cat = 's_pos'
WHERE t.sentistrength_sentiment_analysis_score > 0.5;
update Tweet t
set t.sentistrength_sentiment_analysis_polarity_5_cat = 'w_pos'
WHERE t.sentistrength_sentiment_analysis_score BETWEEN 0.0001 AND 0.5;
update Tweet t
set t.sentistrength_sentiment_analysis_polarity_5_cat = 'neu'
WHERE t.sentistrength_sentiment_analysis_score = 0.0;
update Tweet t
set t.sentistrength_sentiment_analysis_polarity_5_cat = 'w_neg'
WHERE t.sentistrength_sentiment_analysis_score BETWEEN -0.5 AND -0.0001;
update Tweet t
set t.sentistrength_sentiment_analysis_polarity_5_cat = 's_neg'
WHERE t.sentistrength_sentiment_analysis_score < -0.5;


-- UPDATE FOR SENTILEXPT 5 CATEGORIES
update Tweet t
set t.sentilexpt_sentiment_analysis_polarity_5_cat = 's_pos'
WHERE t.sentilexpt_sentiment_analysis_score > 0.5;
update Tweet t
set t.sentilexpt_sentiment_analysis_polarity_5_cat = 'w_pos'
WHERE t.sentilexpt_sentiment_analysis_score BETWEEN 0.0001 AND 0.5;
update Tweet t
set t.sentilexpt_sentiment_analysis_polarity_5_cat = 'neu'
WHERE t.sentilexpt_sentiment_analysis_score = 0.0;
update Tweet t
set t.sentilexpt_sentiment_analysis_polarity_5_cat = 'w_neg'
WHERE t.sentilexpt_sentiment_analysis_score BETWEEN -0.5 AND -0.0001;
update Tweet t
set t.sentilexpt_sentiment_analysis_polarity_5_cat = 's_neg'
WHERE t.sentilexpt_sentiment_analysis_score < -0.5;


-- UPDATE FOR LIWC 5 CATEGORIES
update Tweet t
set t.liwc_sentiment_analysis_polarity_5_cat = 's_pos'
WHERE t.liwc_sentiment_analysis_score > 0.5;
update Tweet t
set t.liwc_sentiment_analysis_polarity_5_cat = 'w_pos'
WHERE t.liwc_sentiment_analysis_score BETWEEN 0.0001 AND 0.5;
update Tweet t
set t.liwc_sentiment_analysis_polarity_5_cat = 'neu'
WHERE t.liwc_sentiment_analysis_score = 0.0;
update Tweet t
set t.liwc_sentiment_analysis_polarity_5_cat = 'w_neg'
WHERE t.liwc_sentiment_analysis_score BETWEEN -0.5 AND -0.0001;
update Tweet t
set t.liwc_sentiment_analysis_polarity_5_cat = 's_neg'
WHERE t.liwc_sentiment_analysis_score < -0.5;


select count(*) from Tweet t where t.text_updated = 0 or t.retweet_updated = 0;
select * from BigFiveResult;

select * from Tweet t;

select *
from Tweet t inner join User U on t.id_user = U.id inner join BigFiveResult BFR on U.id = BFR.id_user
where t.liwc_sentiment_analysis_polarity is null;

select count(t.id) as qtd_tweets
from Tweet t inner join User U on t.id_user = U.id inner join BigFiveResult BFR on U.id = BFR.id_user
where t.is_retweet = 1;

select count(t.id) as qtd_tweets, u.participant_id
from Tweet t inner join User U on t.id_user = U.id inner join BigFiveResult BFR on U.id = BFR.id_user
group by u.participant_id;

select u.participant_id,
       (select count(*) from Tweet t where t.is_retweet = 0 and t.id_user = u.id) as qtd_original,
       (select count(*) from Tweet t where t.is_retweet = 1 and t.id_user = u.id) as qtd_retweets,
       count(t.id) as qtd_tweets
from Tweet t inner join User U on t.id_user = U.id inner join BigFiveResult BFR on U.id = BFR.id_user
group by u.participant_id, u.id order by participant_id;


select count(*) from Tweet t where t.retweet_updated = 0;
select count(*) from Tweet t where t.text_updated = 0;

select * from Tweet t where t.id in (
102600,
102895,
103085,
103092,
103200,
103241,
103440,
103530,
103546,
103629,
103823,
103875,
104002,
104229,
104323,
104337,
104395,
104751,
104770,
104958,
105218,
105373,
105757,
105868,
106127,
106368,
106399,
107050,
107051,
107092,
107249,
107654,
107710,
107765,
107823,
108216,
108233,
108260,
108269,
108452,
108544,
108609,
108628,
108644,
108743,
109252,
109365,
109441,
109590,
109665,
109675,
109876,
109909,
110077,
110409,
110666,
110709,
111087,
111131,
111248,
111856,
112071,
112279,
112599,
112701,
112731,
112849,
113313,
113356,
113410,
113751,
113983,
114184,
114444,
114466,
114815,
114973,
115288,
115783,
115911,
116167,
116582,
116971,
117089,
117401,
117637,
117742,
117955,
118247,
118277,
118339,
118533,
118550,
118650,
118896,
119137,
119369,
119409,
119512,
123647,
123728,
123790,
123968,
124184,
124194,
124365,
124387,
124464,
124489,
124495,
124828,
125041,
125061,
125062,
125126,
125341,
125447,
125503,
125522,
125635,
125757,
126174,
126353,
126467,
127125,
127477,
127524,
127870,
128199,
128586,
128643,
128983,
129033,
129080,
129311,
129327,
129827,
129944,
129995,
130079,
130597,
130628,
130653,
130787,
131047,
131213,
131364,
131734,
131788,
132453,
133208,
133291,
133329,
133430,
133738,
133948,
133959,
134009,
134110,
134111,
134158,
134398,
134432,
134444,
134510,
135397,
135641,
135814,
138363,
138474,
138553,
139282,
145991,
146055,
146065,
154031,
154072,
154089,
154156,
154234,
154277,
154435,
154683,
154709,
154711,
154795,
154818,
154856,
154888,
154952,
155065,
155199,
155234,
155260,
155296,
155315,
155417,
155420,
155443,
155476,
155526,
155603,
155801,
155950,
156008,
156132,
156185,
156331,
156399,
156496,
157276,
157299,
157393,
157459,
157622,
157638,
157859,
157882,
158084,
158183,
158222,
158315,
158388,
158456,
158470,
158539,
158623,
158667,
158699,
158737,
158787,
158869,
158873,
158943,
158953,
159009,
159183,
159216,
159280,
159342,
159405,
159433,
159722,
159774,
159913,
163697,
163719,
164171,
164494,
165188,
165219,
165339,
165491,
165927,
166123,
166369,
166376,
166503,
166819,
167118,
167138,
167174,
167282,
167867,
167872,
168149,
168267,
168290,
168389,
168458,
168581,
168639,
168694,
168990,
169648,
169650,
169950,
170427,
170757,
170776,
171269,
171619,
171630,
171993,
172307,
172378,
172442,
172647,
172949,
172976,
173040,
173073,
173337,
173387,
173536,
173553,
173583,
173585,
173656,
173995,
174112,
174221,
174249,
174298,
174302,
174374,
174871,
175081,
175124,
175143,
175384,
175658,
175985,
176014,
176280,
176769,
176856,
176909,
177086,
177122,
177268,
177419,
177467,
177475,
177586,
177650,
177831,
177839,
177971,
177985,
178128,
178213,
178275,
178441,
178741,
178755,
178770,
178861,
179120,
179137,
179212,
179410,
179689,
179701,
179748,
179886,
179917,
179938,
179975,
180006,
180044,
180055,
180099,
180335,
180340,
180691,
180769,
181008,
181138,
181225,
181322,
181507,
181604,
181647,
181800,
181910,
181991,
182023,
182038,
182049,
182122,
182201,
182296,
182614,
182811,
182825,
183005,
183098,
183282,
183441,
183699,
184085,
184156,
184250,
184262,
184860,
184924,
185204,
185239,
185373,
185448,
185789,
185904,
186458,
186683,
186751,
186768,
188134,
188158,
188298,
188405,
189178,
189208,
189376,
189516,
189649,
189716,
189757,
189870,
189886,
190038,
190157,
190253,
190430,
190594,
190686,
190818,
190846,
191019,
191159,
191600,
191731,
191749,
191779,
191826,
191850,
191859,
191966,
192003,
192073,
192286,
192527,
192604,
192775,
192929,
193013,
193066,
193201,
193354,
193444,
193467,
193520,
193524,
193748,
193852,
193854,
194028,
194061,
194067,
194129,
194153,
194416,
194647,
194664,
194717,
229895,
229855,
229783,
229722,
229638,
229565,
229430,
229327,
229108,
229059,
228830,
228761,
228751,
228638,
228575,
228461,
228277,
228168,
228043,
227630,
227253,
226542,
226498,
226454,
226299,
225649,
225643,
225519,
225363,
225232,
225088,
224687,
224535,
224525,
224488,
223131,
222083,
221851,
221551,
221550,
220001,
219597,
218252,
217878,
216626,
216317,
215839,
214182,
213854,
211601,
209598,
209540,
207889,
207339,
204399,
204373,
204298,
203925,
203238,
202992,
202680,
202014,
201933,
201677,
200879,
200645,
200154,
198955,
197097,
197052,
153219,
152838,
152660,
151966,
151829,
151443,
151359,
151110,
150933,
150655,
150153,
149819,
149545,
149391,
149363,
148849,
147950,
147540,
147361,
147248,
146957,
146941,
146672,
142599,
142522,
142511,
142459,
142400,
142160,
141745,
141162,
140710,
140622,
140363,
140009
)
-- and t.id_user = 32;
-- and t.id_user = 43;
and t.id_user = 44;

select * from Tweet t where t.id in (
102600,
103241,
103875,
104229,
104337,
105218,
109365,
109876,
114815,
117089,
118533,
118896,
125061,
127870,
129827,
131788,
154711,
154795,
155443,
155603,
158388,
158699,
159405,
159722,
165219,
171630,
172976,
173040,
173073,
174249,
177086,
177586,
177971,
178770,
180006,
180691,
180769,
181647,
181800,
182296,
186768,
189208,
190430,
191019,
193354,
193852,
194664
    )
and t.is_retweet = 1;

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
FROM User u INNER JOIN Tweet t ON u.id = t.id_user
INNER JOIN BigFiveResult b on u.id = b.id_user
GROUP BY u.screen_name;



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
 t.vader_sentiment_analysis_score = null
#  t.oplexicon_sentiment_analysis_polarity = null,
#  t.oplexicon_sentiment_analysis_score = null,
#  t.sentistrength_sentiment_analysis_polarity = null,
#  t.sentistrength_sentiment_analysis_score = null,
#  t.sentilexpt_sentiment_analysis_polarity = null,
#  t.sentilexpt_sentiment_analysis_score = null,
#  t.final_score = null,
#  t.final_polarity = null
WHERE t.id in (
102600,
102895,
103085,
103092,
103200,
103241,
103440,
103530,
103546,
103629,
103823,
103875,
104002,
104229,
104323,
104337,
104395,
104751,
104770,
104958,
105218,
105373,
105757,
105868,
106127,
106368,
106399,
107050,
107051,
107092,
107249,
107654,
107710,
107765,
107823,
108216,
108233,
108260,
108269,
108452,
108544,
108609,
108628,
108644,
108743,
109252,
109365,
109441,
109590,
109665,
109675,
109876,
109909,
110077,
110409,
110666,
110709,
111087,
111131,
111248,
111856,
112071,
112279,
112599,
112701,
112731,
112849,
113313,
113356,
113410,
113751,
113983,
114184,
114444,
114466,
114815,
114973,
115288,
115783,
115911,
116167,
116582,
116971,
117089,
117401,
117637,
117742,
117955,
118247,
118277,
118339,
118533,
118550,
118650,
118896,
119137,
119369,
119409,
119512,
123647,
123728,
123790,
123968,
124184,
124194,
124365,
124387,
124464,
124489,
124495,
124828,
125041,
125061,
125062,
125126,
125341,
125447,
125503,
125522,
125635,
125757,
126174,
126353,
126467,
127125,
127477,
127524,
127870,
128199,
128586,
128643,
128983,
129033,
129080,
129311,
129327,
129827,
129944,
129995,
130079,
130597,
130628,
130653,
130787,
131047,
131213,
131364,
131734,
131788,
132453,
133208,
133291,
133329,
133430,
133738,
133948,
133959,
134009,
134110,
134111,
134158,
134398,
134432,
134444,
134510,
135397,
135641,
135814,
138363,
138474,
138553,
139282,
145991,
146055,
146065,
154031,
154072,
154089,
154156,
154234,
154277,
154435,
154683,
154709,
154711,
154795,
154818,
154856,
154888,
154952,
155065,
155199,
155234,
155260,
155296,
155315,
155417,
155420,
155443,
155476,
155526,
155603,
155801,
155950,
156008,
156132,
156185,
156331,
156399,
156496,
157276,
157299,
157393,
157459,
157622,
157638,
157859,
157882,
158084,
158183,
158222,
158315,
158388,
158456,
158470,
158539,
158623,
158667,
158699,
158737,
158787,
158869,
158873,
158943,
158953,
159009,
159183,
159216,
159280,
159342,
159405,
159433,
159722,
159774,
159913,
163697,
163719,
164171,
164494,
165188,
165219,
165339,
165491,
165927,
166123,
166369,
166376,
166503,
166819,
167118,
167138,
167174,
167282,
167867,
167872,
168149,
168267,
168290,
168389,
168458,
168581,
168639,
168694,
168990,
169648,
169650,
169950,
170427,
170757,
170776,
171269,
171619,
171630,
171993,
172307,
172378,
172442,
172647,
172949,
172976,
173040,
173073,
173337,
173387,
173536,
173553,
173583,
173585,
173656,
173995,
174112,
174221,
174249,
174298,
174302,
174374,
174871,
175081,
175124,
175143,
175384,
175658,
175985,
176014,
176280,
176769,
176856,
176909,
177086,
177122,
177268,
177419,
177467,
177475,
177586,
177650,
177831,
177839,
177971,
177985,
178128,
178213,
178275,
178441,
178741,
178755,
178770,
178861,
179120,
179137,
179212,
179410,
179689,
179701,
179748,
179886,
179917,
179938,
179975,
180006,
180044,
180055,
180099,
180335,
180340,
180691,
180769,
181008,
181138,
181225,
181322,
181507,
181604,
181647,
181800,
181910,
181991,
182023,
182038,
182049,
182122,
182201,
182296,
182614,
182811,
182825,
183005,
183098,
183282,
183441,
183699,
184085,
184156,
184250,
184262,
184860,
184924,
185204,
185239,
185373,
185448,
185789,
185904,
186458,
186683,
186751,
186768,
188134,
188158,
188298,
188405,
189178,
189208,
189376,
189516,
189649,
189716,
189757,
189870,
189886,
190038,
190157,
190253,
190430,
190594,
190686,
190818,
190846,
191019,
191159,
191600,
191731,
191749,
191779,
191826,
191850,
191859,
191966,
192003,
192073,
192286,
192527,
192604,
192775,
192929,
193013,
193066,
193201,
193354,
193444,
193467,
193520,
193524,
193748,
193852,
193854,
194028,
194061,
194067,
194129,
194153,
194416,
194647,
194664,
194717);

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
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (29,	45,	36,	27,	32, (SELECT u.id from User u where u.screen_name = 'bellesamways'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (30,	35,	24,	20,	32, (SELECT u.id from User u where u.screen_name = 'Willian_justen'));



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

select * from User

select distinct b.*, u.participant_id
from BigFiveResult b inner join user u on u.id = b.id_user;