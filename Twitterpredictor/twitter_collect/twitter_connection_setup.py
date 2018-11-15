import tweepy
# We import our access keys:
import twitter_collect.credential
from twitter_collect.twitterconnect import twitter_setup


def collect():
    #renvoi 100 tweet avec @EmmanuelMacron
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)



def collect_by_user(user_id,count):
    #renvoie un nombre count de tweets de l'user référencé par son id
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, c= count)
    for status in statuses:
        print(status.text)
    return statuses




