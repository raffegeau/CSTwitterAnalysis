import csv
import tweepy


def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        path=type+"_"+file_path+"_"+num_candidate+".txt"
        q=[] #liste des requêtes
        with open (path) as csvfile:
            for line in csvfile:
                q.append(line)
        return q

    except IOError:
        print("le fichier ne peut pas être lu")

def get_tweets_from_candidates_search_queries(queries,twitter_api):
    from tweepy import RateLimitError
    from tweepy import TweepError
    try:
        for q in queries:
            tweets = twitter_api.search(q,language="french",rpp=100)
            for tweet in tweets:
                print(tweet.text)

    except TweepError:
        print("veillez revérifier l'api")
    except RateLimitError:
        print ("le débit maximal de twitter est atteint, veillez réessayer plus tard")

def get_replies_to_candidate(num_candidate):





