# using NLTK library, we can do lot of text pre-processing
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# function to split text into word
tokens = word_tokenize("The quick brown fox jumps over the lazy dog")
stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if not w in stop_words]

print(tokens)

porter = PorterStemmer()
stems = []
for t in tokens:
    stems.append(porter.stem(t))

print(stems)
