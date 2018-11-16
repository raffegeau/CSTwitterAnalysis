from textblob import TextBlob

words={}
uniquesoulem=[]
def voctweet(data):
    uniquesoulem=[]
    for tweet in data['tweet_textual_content'] :
        txt=TextBlob(tweet)
        l=txt.words
        for word in l:
            if word in words:
                words[word]=words[word]+1

            else:
                words[word]=1

    for word in words:
        if words[word]==1 or word.lemmatize()==word:
            uniquesoulem.append(word)

def opiniontweet(data):
    pos_tweets=[]
    neu_tweets=[]
    neg_tweets=[]
    for tweet in data['tweet_textual_content'] :
        txt=TextBlob(tweet)
        n=tweet.sentiment[0]
        if n<-0.5:
            neu_tweets.append(txt)
        elif n>0.5:
            pos_tweets.append(txt)
        else:
            neg_tweets.append(txt)

    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))

