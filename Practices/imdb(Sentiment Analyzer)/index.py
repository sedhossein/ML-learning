import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# download dependencies here
nltk.download('punkt')
nltk.download('stopwords')

# configs and storage
folder = 'acl'
labels = {'pos': 1, 'neg': 0}
df = pd.DataFrame()

# convert the dataset from files to a python DataFrame
for f in ('test', 'train'):
    for l in ('pos', 'neg'):
        path = os.path.join(folder, f, l)
        for idx, file in enumerate(os.listdir(os.getcwd() + "/" + path)):
            with open(os.path.join(path, file), 'r+',
                      encoding='utf-8') as infile:  # encoding='utf-8' just work in python3
                txt = infile.read()

            df = df.append([{
                'review': txt,
                'sentiment': labels[l],
            }], ignore_index=True)

# TODO: uncomment if you need
# save the assembled data as .csv file for further use.
# df.to_csv('movie_data.csv', index=False, encoding='utf-8')
# df.head()

# frequency distribution of the words in the text
reviews = df.review.str.cat(sep=' ')  # function to split text into word
tokens = word_tokenize(reviews)
vocabulary = set(tokens)
print("number of vocabulary:" + str(len(vocabulary)))

# remove the stop words to further cleanup the text corpus.
stop_words = set(stopwords.words('english'))
tokens = [w for w in vocabulary if not w in stop_words]

frequency_dist = nltk.FreqDist(tokens)
sortedData = sorted(frequency_dist, key=frequency_dist.__getitem__, reverse=True)[0:50]
print(sortedData)

# visualization tool wordcloud package helps to create word clouds by
# placing words on a canvas randomly, with sizes proportional to their frequency in the text.
wordcloud = WordCloud().generate_from_frequencies(frequency_dist)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# Building a Classifier
X_train = df.loc[:24999, 'review'].values
y_train = df.loc[:24999, 'sentiment'].values
X_test = df.loc[25000:, 'review'].values
y_test = df.loc[25000:, 'sentiment'].values

vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)
print(train_vectors.shape, test_vectors.shape)

# train the model on the training set
clf = MultinomialNB().fit(train_vectors, y_train)

# test the performance of our model on the test set to predict the sentiment labels
predicted = clf.predict(test_vectors)
print(accuracy_score(y_test, predicted))
