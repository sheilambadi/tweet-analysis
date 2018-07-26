import csv
import re
import textblob
from textblob import TextBlob
from setup import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def getTweets(searchKey):
    results = filterTweets(searchKey)
    return results

def tweets(search):
    tweetResults = getTweets(search)
    # save reults to csv file
    with open (str(search)+'.csv', 'a', newline='') as f:
        fieldnames = ['searchKey', 'tweetId', 'tweetDate', 'tweet', 'polarity']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        for tweet in tweetResults:
            if not tweet.retweeted and 'RT @' not in tweet.text:
                clean_tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*|(@[A-Za-z0-9]+)', '', tweet.text)
                blob = TextBlob(clean_tweet)
                # analyze
                polarity = blob.sentiment.polarity;
                thewriter.writerow({'searchKey' : str(search), 'tweetId' : tweet.id,'tweetDate': tweet.created_at, 'tweet' : clean_tweet, 'polarity':polarity})

tweets('amzn')

''' 
def preprocessTweets():
    tweetResults = getTweets()   
    stop_words = set(stopwords.words('english')) 
    ps = PorterStemmer()

    for tweet in tweetResults:
        # word tokenization
        word_tokens = word_tokenize(str(tweet))

        # stop words removals
        filtered_sentence = [w for w in word_tokens if not w in stop_words]

        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                # stemming for normalization purpose
                stemmed_word = ps.stem(w)
                filtered_sentence.append(stemmed_word)

        print(filtered_sentence)

#preprocessTweets()
'''