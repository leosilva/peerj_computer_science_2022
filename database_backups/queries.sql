select * from User;
select * from Tweet where lang = "pt" order by rand() limit 20;
select * from BigFiveResult;


select u.screen_name, count(t.id) from User u inner JOIN Tweet t on u.id = t.id_user group by u.screen_name;

select * from Tweet t;

SELECT id FROM User u WHERE u.id_str_twitter = '10384742';


SHOW VARIABLES LIKE 'innodb_autoinc_lock_mode';


SET innodb_autoinc_lock_mode = 0;
SET mysqlx_wait_timeout = 1000000;
SET wait_timeout = 1000000;

select t.created_at from Tweet t
inner join User u on t.id_user = u.id
where u.screen_name = "psanrosa13"
order by t.created_at;

SHOW ENGINE INNODB STATUS;

show open tables where in_use>0;

show full processlist;

show variables like '%wait_timeout%';
show variables like '%_isolation%';

SHOW VARIABLES LIKE '%access_mode%';

delete from Tweet t
where t.id_user in (select u.id from User u where u.screen_name = 'nannoka');

delete from User u where u.screen_name = 'nannoka';

ALTER TABLE User AUTO_INCREMENT = 1;

SELECT count(*) FROM Tweet t
WHERE t.created_at > "2021-03-31 23:59:59";


SELECT count(*) FROM Tweet t where t.lang = 'pt';

SELECT t.* FROM Tweet t inner join User u on t.id_user = u.id WHERE u.id = 15
ORDER BY t.created_at desc;

select count(*) from Tweet t where t.lang <> 'pt';

delete from Tweet t where t.lang <> 'pt';
delete from Tweet t where t.created_at > "2021-03-31 23:59:59";

INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (22, 33, 31, 20, 8, (SELECT u.id from User u where u.screen_name = 'rponte'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (43, 46, 31, 24, 15, (SELECT u.id from User u where u.screen_name = 'FelippeRegazio'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (41, 43, 34, 22, 23, (SELECT u.id from User u where u.screen_name = 'Guilh_rm_'));
INSERT INTO BigFiveResult (o_score, c_score, e_score, a_score, n_score, id_user)
VALUES (37, 43, 36, 24, 26, (SELECT u.id from User u where u.screen_name = 'rebelatto'));