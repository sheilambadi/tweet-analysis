from setup import *

def getTweets():
    results = filterTweets("#amzn")
    return results
    
tweetResults = getTweets()    
print("5 recent tweets:\n")
for tweet in tweetResults:
    print(tweet.text)
    print()
