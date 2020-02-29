# using NLTK library, we can do lot of text pre-processing
import nltk
from nltk.tokenize import word_tokenize

# function to split text into word
tokens = word_tokenize("The quick brown fox jumps over the lazy dog")
nltk.download('stopwords')
print(tokens)
