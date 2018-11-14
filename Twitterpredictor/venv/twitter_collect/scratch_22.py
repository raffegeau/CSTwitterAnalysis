import tweepy
from credentials import *

def collect():
    connexion=connect.twitter_setup()
    tweets=connexion.search("Emmanuel Macron")
    for tweet in tweets :
        print(tweet.text)

collect()
