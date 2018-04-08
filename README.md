# Twitter app with Python and MySQL

This app will use Python, MySQL and csv

1. Takes an input from user                                                        
2. Searches for the input value in a column in csv file                            
3. Gives user back result if found - asks to make a selection of id from result    
4. Searches Twitter Search from Twitter API for the value provided as user         
5. Collects tweets for screen name                                                 
6. Puts collected tweets in MySQL db        

Pbskidd Twitter App – Set up

## 1	SETTING UP MYSQL DATABASE AND RUNNING THE SCRIPT

Before you can run the script you need to do the following:

1.	Create a connection in MySQL db
2.	Create a user, password (you can use root + password)
3.	Run the script called “pbskidd_create_tweet_table2.sql” in MySQL admin toll of your choice
4.	Check if the table and db has been created
5.	Get the credentials from dev.twitter.com for your app under “My Apps” and put them under:
access_key = ''
access_secret = ''
consumer_key = ''
consumer_secret = ''

in the script.

6.	Select the csv file in the following line in the script:
with open('tweeters.csv', newline='') as f:
7.	Select the column you want to be searched for the value in csv file:
if match in row[1]:
Index starts from 0 (0= first column in csv file, 1= second column, etc.)
8.	If you don’t have twitter library installed from before – run “pip install twitter” from command line
9.	For installing the Python MySQL connector use: “pip install MySQL-python” from command line
10.	Put in credentials for MySql db in script by updating the following section:

## MySQL initialization - create a MySql db 

connection =  MySQLdb.connect(host= "127.0.0.1",
user="",
passwd="",
db="")
cursor = connection.cursor()


Run the script from command line: python pbskidd_twitter_app_final.py






