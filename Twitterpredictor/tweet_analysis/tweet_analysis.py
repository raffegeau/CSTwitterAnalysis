import numpy as np

def RTmax(data):
    rt_max= np.max(data['RTs'])
    rt= data[data.RTs == rt_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

def RTmin(data):
    rt_min=np.min(data['RTs'])
    

def  Likesmax(data):
    likes_max  = np.max(data['Likes'])
    likes = data[data.Likes == rt_max].index[0]
    print("The tweet with most like: \n{}".format(data['tweet_textual_content'][likes]))
    print("Number of retweets: {}".format(likes))
    print("{} characters.\n".format(data['len'][rt]))

def lenmin(data):
    len_min  = np.min(data['len'])
    Len  = data[data.len == len_min].index[0]
    print("The smallest tweet is: \n{}".format(data['tweet_textual_content'][len]))
    print("Number of retweets: {}".format(likes))
    print("{} characters.\n".format(data['len'][rt]))

def lenmax(data):
    len_max  = np.max(data['len'])
    Len  = data[data.len == len_max].index[0]
    print("The longest tweet is: \n{}".format(data['tweet_textual_content'][len]))
    print("Number of retweets: {}".format(likes))
    print("{} characters.\n".format(data['len'][rt]))

tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])


tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()

