import json
from twitter_collect.twitter_connection_setup import *
import pandas


'''tweets = collect()
status=tweets[0]'''

def count_lignes(filename):
    with open(filename,'r') as f :
        cnt=0
        for l in f:
            cnt=cnt+1
        return cnt

def store_tweets(tweets,filename):
    "stocke des tweet dans un ficier json à l'adresse filename"
    with open(filename,'w') as f_out:
        for status in tweets:
            json.dump(status._json, f_out,indent=2)
            f_out.write(',\n')

def store_tweets_exploitable(filename,filename_clean):
    '''ce programme prend des tweets en fichier json mal "indentés" localisé en filename et rajoute l'indentation
     pour avoir des "bons fichiers" json sur file_nameclean"'''

    f = open(filename,"r")
    f2 = open(filename_clean,"w")
    f2.write("{\n  \"tweets\": [\n")
    cnt=1
    for l in f:
        if cnt == count_lignes(filename):
            f2.write("      }\n")
        else:
            f2.write("      "+l)
        cnt=cnt+1
    f2.write("  ]\n}")

def dataframe_exploitable(filename_clean,clefs_utiles):

    '''ce programme importe des donnees sous forme de fichier json qui sont à l'adresse filename_clean et renvoie un dataframe
    qui a pour colonnes des clefs uriles du tweet'''
    with open(filename_clean) as f:
        data = json.load(f)
        dictionnaire_utile=[]
        for tweet in data["tweets"]:
            caract_nouveau_tweet={}
            for k in clefs_utiles:
                if k != "len":
                    caract_nouveau_tweet[k]=tweet[k]
                else:
                    caract_nouveau_tweet['len']=len(tweet["text"])
            dictionnaire_utile.append(caract_nouveau_tweet)
        donnees_exploitables=pandas.DataFrame(dictionnaire_utile)
        return donnees_exploitables







