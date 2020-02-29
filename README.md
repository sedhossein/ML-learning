This Repo is about learning ML for Lexicon-Based Sentiment Analysis in the Social Web.
<b>(Text Processing)</b>

## tools:

- python3
- use STUDIO3R GUI for mongoDB
- use injected package in `./Tests` for crawling ()
- IMDB data set : `http://ai.stanford.edu/~amaas/data/sentiment/` 

## questions:

- text mining vs text analisys vs  text proccesing
- https://blog.bitext.com/what-is-the-difference-between-stemming-and-lemmatization/
- unsupervised vs supervised learning

## concepts & algorithms

- Algorithms for: text mining, text algorithms, topic detection, text processing
- Lexicon-Based Sentiment Analysis in the Social Web
- Algorithms for: network
- Naive Bayes
- Support Vector Machines
- bios and variance trade-off
- Linear re-ression (aka least squares)


# docs:
### Step 1 : Data pre-processing

- **Tokenizing** — convert sentences to words
- **Removing** unnecessary punctuation, tags
- **Removing** stop words — frequent words such as ”the”, ”is”, etc. that do not have specific semantic
- **Stemming** — words are reduced to a root by removing inflection through dropping unnecessary characters, usually a suffix.
```
The stemmed form of studies is: studi
The stemmed form of studying is: study
```
- **Lemmatization** — Another approach to remove inflection by determining the part of speech and utilizing detailed database of the language.
```
The lemmatized form of studies is: study
The lemmatized form of studying is: study
```

### Step 2: Feature Extraction

The mapping from textual data to real valued vectors is called feature extraction. One of the simplest techniques to numerically represent text is Bag of Words.
    
**Bag of Words (BOW):** <br>
 We make the list of unique words in the text corpus called vocabulary. Then we can represent each sentence or document as a vector with each word represented as 1 for present and 0 for absent from the vocabulary. Another representation can be count the number of times each word appears in a document. The most popular approach is using the Term Frequency-Inverse Document Frequency (TF-IDF) technique.

 - Term Frequency (TF) = (Number of times term t appears in a document)/(Number of terms in the document)
 - Inverse Document Frequency (IDF) = log(N/n), where, N is the number of documents and n is the number of documents a term t has appeared in. The IDF of a rare word is high, whereas the IDF of a frequent word is likely to be low. Thus having the effect of highlighting words that are distinct.
 - We calculate TF-IDF value of a term as = TF * IDF

One of the major disadvantages of using BOW is that it discards word order thereby ignoring the context and in turn meaning of words in the document. For natural language processing (NLP) maintaining the context of the words is of utmost importance. To solve this problem we use another approach called Word Embedding.

Word Embedding: It is a representation of text where words that have the same meaning have a similar representation. In other words it represents words in a coordinate system where related words, based on a corpus of relationships, are placed closer together.

**Word2Vec** <br>
    Word2vec takes as its input a large corpus of text and produces a vector space with each unique word being assigned a corresponding vector in the space. Word vectors are positioned in the vector space such that words that share common contexts in the corpus are located in close proximity to one another in the space. Word2Vec is very famous at capturing meaning and demonstrating it on tasks like calculating analogy questions of the form a is to b as c is to ?. For example, man is to woman as uncle is to ? (aunt) 

**GloVe** <br>
    GloVe constructs an explicit word-context or word co-occurrence matrix using statistics across the whole text corpus. The result is a learning model that may result in generally better word embeddings.

### Step 3: Choosing ML Algorithms
Classical ML approaches like ‘Naive Bayes’ or ‘Support Vector Machines’ for spam filtering has been widely used.
   
   
   
   
reference : https://towardsdatascience.com/machine-learning-text-processing-1d5a2d638958    