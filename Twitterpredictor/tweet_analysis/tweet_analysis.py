import numpy as np

def RTmax(data):
    #renvoie le tweet avec le max de retweet
    rt_max= np.max(data['RTs'])
    rt= data[data.RTs == rt_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

def RTmin(data):
    #renvoie le tweet avec le min de retweet
    rt_min=np.min(data['RTs'])
    rt= data[data.RTs==rt_min].index[0]
    #Min RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_min))
    print("{} characters.\n".format(data['len'][rt]))

def LikeMin(data):
    #renvoie le tweet avec le max de likes
    like_min=np.min(data['Likes'])
    like= data[data.Likes==likes_max].index[0]
    #Min likes:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][like]))
    print("Number of retweets: {}".format(likes_max))
    print("{} characters.\n".format(data['len'][like]))

def recherche_mots_clefs(data,mot_clef):
    #renvoie les tweet avec le mot clef
    liste_tweet_contenant_mot_clef=[]
    liste_tweet_texte=data[tweet_textual_content]
    for tweet in liste_tweet_texte:
        if mot_clef in tweet:
            liste_tweet_contenant_mot_clef.append(tweet)
    return liste_tweet_contenant_mot_clef




