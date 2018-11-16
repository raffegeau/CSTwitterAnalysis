import tweet_collection.generer_donnees as tw
import matplotlib.pyplot as plt
import pandas as pd

#data=tw.create_data()

def afficher_RT_Likes(data):
    tfav = pd.Series(data=data["retweet_count"].values, index=data['created_at'])
    tret = pd.Series(data=data["favorite_count"].values, index=data['created_at'])

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="retweet_count", legend=True)
    tret.plot(figsize=(16,4), label="favorite_count", legend=True)

    plt.show()


#afficher_like_par_candidat

def afficher_like_candidat(liste_candidat,data):
    for candidat in liste_candidat:
        data.add(data[candidat],axis="rows")
        for






