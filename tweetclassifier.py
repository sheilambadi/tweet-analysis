from setup import *
from nltk.tokenize import sent_tokenize, word_tokenize

def getTweets():
    results = filterTweets("#amzn")
    return results
    
def preprocessTweets():
    tweetResults = getTweets()    

    for tweet in tweetResults:
        print(word_tokenize(str(tweet)))

preprocessTweets()