import re
import textblob
from textblob import TextBlob

thestring = "@ExchangeGoddess Amateur hour over at #msft or a cunning ploy to get the hold out on-prem customers over to exchang… https://t.co/gI332ph2pW"

#URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*|(@[A-Za-z0-9]+)', '', thestring)
URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', thestring)
blob = TextBlob(URLless_string)

# analyze
polarity = blob.sentiment.polarity;
print(polarity)