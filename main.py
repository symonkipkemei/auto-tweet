
import tweepy
import os
import random
import json
from datetime import datetime


consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_KEY_SECRET")
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret =os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# load tweets from json file
file = open("tweets.json")
data = json.load(file)
tweets = data["tweets"]
tweet = random.choice(tweets)

# add date at the end of the tweet to make each entry unique
daytime = datetime.now()
message = tweet["text"] + "~" + daytime.strftime("%m/%d/%Y, %H:%M:%S")
print(message)

client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)
response = client.create_tweet(text=message)

print("successfully printed")


