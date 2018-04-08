# You need to run this sql script in MySql database admin tool
# before you run the script pbskidd_twitter_app_final.py


create database if not exists pbskidd;

use pbskidd;

drop table if exists tweets;

CREATE TABLE tweets (id INT PRIMARY KEY AUTO_INCREMENT, 
tweet_text VARCHAR(160) NOT NULL);
