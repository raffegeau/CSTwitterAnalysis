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



