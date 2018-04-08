import csv
import pprint
from twitter import *
import MySQLdb

'''
****************************************************************************************
** Twitter App for pbskidd                                                            ** 
** 1. Takes an input from user                                                        **
** 2. Searches for the input value in a column in csv file                            **
** 3. Gives user back result if found - asks to make a selection of id from result    **
** 4. Searches Twitter Search from Twitter API for the value provided as user         **
** 5. Collects tweets for screen name                                                 **
** 6. Puts collected tweets in MySQL db                                               **
****************************************************************************************

'''

# Fill inn your Twitter App credentials from dev.twitter.com under "My Apps"    
access_key = ''
access_secret = ''
consumer_key = ''
consumer_secret = ''

# Pretty printing for selction results
pp = pprint.PrettyPrinter(indent=4)

# Get value to to search for in csv file
match = input("Enter value to be searched in csv file: ")

# Dictionary for storing result match from csv file
matched_results = {}

# Dictionary for storing results from Twitter Search API
searched_users = {}

# Open the file to be used in this script - change file name if needed
with open('tweeters.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        # If match found in a row. Change column if the value to be searched for is in different column
        if match in row[1]:
            matched_results[reader.line_num] = row

    # Print the results of match in pretty format
    pp.pprint(matched_results)


# If the match result in not empty:
if matched_results != None:
    
    # Get user input of which id as value to be searched for
    selection = input("Make a selection from list:")

    # Put matched result in search_user variable
    search_user = matched_results[int(selection)][1]

    # Start the Twitter auth api
    twitter = Twitter(
            auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

    # Use Twitter Search Api with value from search_user variable
    results = twitter.users.search(q = search_user)

    # Print all the results found from Twitter Search API 
    for index, user in enumerate(results, start = 1):
        searched_users[index] = user["screen_name"], user["name"], user["location"]
        print("Id: {0:4} Screen Name: {1:30} User :{2:30} Location: {3:20}".format(index, user["screen_name"], user["name"], user["location"]))
      
    # Make a selection from Twitter Search API result - list
    selected_user = int(input("Select id from list: "))

    # Put selected id in user variable
    user = searched_users[selected_user][0]

    # Use user variable to search for user time line in Twitter API
    status_results = twitter.statuses.user_timeline(screen_name = user, count=200)

else:
    
    # If no match in result - print message
    print("No results found!")

# If there are no tweets
if status_results == "":
    
    print("No tweets for user found!")

# If there are tweets
else:

    # MySQL initialization - create a MySql db 
    connection =  MySQLdb.connect(host= "127.0.0.1",
        user="",
        passwd="",
        db="")
    cursor = connection.cursor()

    # Loop over tweets found and store in db
    for s in status_results:
        # To remove duplicate entries
        cursor.execute("SELECT id FROM tweets WHERE tweet_text = %s;", [s["text"].encode("ascii", "ignore")])
        if cursor.rowcount == 0:
            cursor.execute("INSERT INTO tweets (tweet_text) VALUES (%s);", ([s["text"].encode("ascii", "ignore")]))
            connection.commit()
        

    cursor.close()
    connection.close()       
