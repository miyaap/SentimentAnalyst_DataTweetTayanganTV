# -*- coding: utf-8 -*-
"""SentimenAnalyst_DataTweetTayanganTV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fCPZF8MVXcP7gNs4xRhdUs9I7LZt74N1
"""

!pip install nltk
!pip install Sastrawi

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import random
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
print(tf.__version__)

!pip -q install transformers

import transformers
print(transformers.__version__)

data = pd.read_csv('/content/sentimen_tayangan_tv.csv')

data.head()

data.shape

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

data['Sentiment'] = lb.fit_transform(data['Sentiment'])
data

raw_data = data.copy()

"""#  Preprocessing"""

import re
def text_preprocessing(text):
  text = text.lower()
  text = re.sub(r'https?://\S+|www\.\S+', '', text)
  text = re.sub(r'[-+]?[0-9]+', '', text)
  text = re.sub(r'[^\w\s]', '', text)
  #text = text.script()
  return text

print(data.columns)

# Commented out IPython magic to ensure Python compatibility.
# %time data['Text'] = data['Text Tweet'].apply(text_preprocessing)

data.head()

import nltk
nltk.download('all')
from nltk.tokenize import word_tokenize

def tokenize_text(kalimat):
  tokens = nltk.tokenize.word_tokenize(kalimat)
  return tokens

print(df.columns)

df['token'] = df['cleaned_text'].apply(tokenize_text)
df.head()

"""**Filtering(Stopword Removal)**"""

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
stopwords = factory.get_stop_words()
print(stopwords)

def stopword_text(tokens):
  cleaned_tokens = []
  for token in tokens:
    if token not in stopwords:
      cleaned_tokens.append(token)
  return cleaned_tokens

df['stop'] = df['token'].apply(stopword_text)
df.head()

"""**Stemming**"""

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()

def stemming_text(tokens):
  hasil = [stemmer.stem(token) for token in tokens]
  return hasil

df['stemmed'] = df['stop'].apply(stemming_text)
df.head()

"""**Viz**"""

from nltk.probability import FreqDist
import matplotlib.pyplot as plt

all_tokens = [token for sublist in df['stemmed'] for token in sublist]
freq_dist = FreqDist(all_tokens)
print(freq_dist.most_common())

freq_dist.plot(30, cumulative=False)
plt.show()

"""### **Simpan** **dataset bersih**"""

df.to_csv('data_clean.csv', index=False)

data = pd.read_csv('/content/data_clean.csv')
data.head(20)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv('/content/data_clean.csv')

"""**TF-IDF**"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = df['stemmed']
y = df['Sentiment']

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

"""**Algoritma : Multinomial Naive Bayes**"""

from sklearn.naive_bayes import MultinomialNB

model_nb = MultinomialNB()
model_nb.fit(X_train, y_train)

y_pred_nb = model_nb.predict(X_test)

print(classification_report(y_test, y_pred_nb))
print(confusion_matrix(y_test, y_pred_nb))


# Confusion Matrix
class_label = ["negative", "positive"]
df_cm = pd.DataFrame(confusion_matrix(y_test, y_pred_nb), index=class_label, columns=class_label)
sns.heatmap(df_cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

"""**Algoritma: Support Vector Machine (SVM)**"""

from sklearn.svm import SVC

model_svm = SVC()
model_svm.fit(X_train, y_train)

y_pred_svm = model_svm.predict(X_test)

print(classification_report(y_test, y_pred_svm))
print(confusion_matrix(y_test, y_pred_svm))

# Confusion Matrix
class_label = ["negative", "positive"]
df_cm = pd.DataFrame(confusion_matrix(y_test, y_pred_svm), index=class_label, columns=class_label)
sns.heatmap(df_cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

"""**Algoritma: Random Forest Classifier**"""

from sklearn.ensemble import RandomForestClassifier

model_rf = RandomForestClassifier()
model_rf.fit(X_train, y_train)

y_pred_rf = model_rf.predict(X_test)

print(classification_report(y_test, y_pred_rf))
print(confusion_matrix(y_test, y_pred_rf))

# Confusion Matrix
class_label = ["negative", "positive"]
df_cm = pd.DataFrame(confusion_matrix(y_test, y_pred_rf), index=class_label, columns=class_label)
sns.heatmap(df_cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

"""**Algoritma: K-Nearest Neighbor (KNN)**"""

from sklearn.neighbors import KNeighborsClassifier

model_knn = KNeighborsClassifier()
model_knn.fit(X_train, y_train)

y_pred_knn = model_knn.predict(X_test)

print(classification_report(y_test, y_pred_knn))
print(confusion_matrix(y_test, y_pred_knn))

# Confusion Matrix
class_label = ["negative", "positive"]
df_cm = pd.DataFrame(confusion_matrix(y_test, y_pred_knn), index=class_label, columns=class_label)
sns.heatmap(df_cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()