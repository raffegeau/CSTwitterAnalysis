from tweet_collection.Tweet_Collection import *
from twitter_collect.twitter_connection_setup import *
import json

api = twitter_setup()

tweets = api.search("@EmmanuelMacron",language="french",rpp=100)
status=tweets[0]

store_tweets(tweets,"macron.json")
store_tweets_exploitable("macron.json","macron_clean.json")
print(dataframe_exploitable("macron_clean.json",["text","retweet_count","favorite_count"])["text"])

