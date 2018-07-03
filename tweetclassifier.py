from setup import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def getTweets():
    results = filterTweets("#amzn")
    return results
    
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

preprocessTweets()