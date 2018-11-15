import tweepy
import numpy as np


CONSUMER_KEY ='p8jTNzQpOcOW9LpRmTvmDbdOJ'

CONSUMER_SECRET = 'IZfmkxtnZXy6UFakChupNWmdxfRPTNfHJB9UCSYYN4hjEOZQ3Z'

# Access:
ACCESS_TOKEN  = '2217276213-uB9hP30sFPU7mw1yiPCzePGTlgk56B49wpLJFI2'
ACCESS_SECRET = '2DUUfIUkiAwqpN8kC7ZBDtMpmM5CahWRAjVI9E9CcyMlU'


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


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



from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])


def test_collect():
    tweets=tweets
rt_max  = np.max(data['RTs'])
rt  = data[data.RTs == rt_max].index[0]

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))

likes_max  = np.max(data['Likes'])
likes = data[data.Likes == rt_max].index[0]
print("The tweet with most like: \n{}".format(data['tweet_textual_content'][likes]))
print("Number of retweets: {}".format(likes))
print("{} characters.\n".format(data['len'][rt]))

len_min  = np.min(data['RTs'])
len  = data[data.len == len_min].index[0]
print("The smallest tweet is: \n{}".format(data['tweet_textual_content'][likes]))
print("Number of retweets: {}".format(likes))
print("{} characters.\n".format(data['len'][rt]))

len_max  = np.max(data['RTs'])
len  = data[data.len == len_max].index[0]
print("The longest tweet is: \n{}".format(data['tweet_textual_content'][likes]))
print("Number of retweets: {}".format(likes))
print("{} characters.\n".format(data['len'][rt]))
