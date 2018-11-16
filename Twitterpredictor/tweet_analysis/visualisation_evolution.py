
import matplotlib.pyplot as plt
import pandas as pd


data= pd.read_csv('macron_lepen_dataframe.csv', sep = '\t')

'''tret = pd.Series(data=data["retweet_count"].values, index=data['created_at'])
tfav = pd.Series(data=data["favorite_count"].values, index=data['created_at'])

    # Likes vs retweets visualization:
tret.plot(figsize=(16,4), label="retweet_count", legend=True)
tfav.plot(figsize=(16,4), label="favorite_count", legend=True)

plt.show()'''

#afficher_like_par_candidat

l=len(data["text"])
liste=[""]*l
for candidat in ["@EmmanuelMacron","@marinelepen"]:
    for i in range(l):
        if candidat in data["text"][i]:
            liste[i]=candidat+liste[i]
        else:
            continue

data["candidat"]=liste
liste_dico={}
for candidat in ["@EmmanuelMacron","@marinelepen"]:
    rt=0
    for i in range(len(data['text'])):
        if data["candidat"][i]!= candidat:
            continue
        else :
            rt=rt+data["retweet_count"][i]
            
    liste_dico[str(candidat)]=rt

print(liste_dico)
plt.bar(list(liste_dico.keys()), liste_dico.values(), color='g')
plt.show()

#fonctionne!





















