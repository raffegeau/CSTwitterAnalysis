from tweet_collection.Tweet_Collection import *
from twitter_collect.twitter_connection_setup import *
import pandas
import json


def create_data():
    api = twitter_setup()

    tweets_macron = api.search("@EmmanuelMacron",language="french",rpp=100)
    tweets_lepen = api.search("@MarineLepen",language="french",rpp=100)
    status=tweets_macron[0]

    store_tweets(tweets_macron,"macron.json")
    store_tweets_exploitable("macron.json","macron_clean.json")
    store_tweets(tweets_lepen,"lepen.json")
    store_tweets_exploitable("lepen.json","lepen_clean.json")
    data1 = dataframe_exploitable("macron_clean.json",["text","retweet_count","favorite_count","created_at"])
    data2 = dataframe_exploitable("lepen_clean.json",["text","retweet_count","favorite_count","created_at"])
    data=pandas.concat([data1,data2])
    return data



