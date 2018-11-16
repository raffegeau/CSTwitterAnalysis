import tweet_collection.generer_donnees as tw
import matplotlib.pyplot as plt
import pandas as pd

data=tw.create_data()

def afficher_RT_Likes(data):
    tret = pd.Series(data=data["retweet_count"].values, index=data['created_at'])
    tfav = pd.Series(data=data["favorite_count"].values, index=data['created_at'])

    # Likes vs retweets visualization:
    tret.plot(figsize=(16,4), label="retweet_count", legend=True)
    tfav.plot(figsize=(16,4), label="favorite_count", legend=True)

    plt.show()


#afficher_like_par_candidat

def afficher_like_candidat(liste_candidat,data):
    data.add(data["candidat"],axis="rows")
    for candidat in liste_candidat:
        l=len(data["texte"])
        for i in range(l):
            if candidat in data["texte"][i]:
                data["candidat"][i]=candidat
    tret = pd.Series(data=data["favorite_count"].values, index=data["candidate"])
    tret.plot(figsize=(16,4), label="retweet_count", legend=True)

print(afficher_like_candidat(["@EmmanuelMacron","@MarineLepen"],data))














