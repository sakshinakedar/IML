import json
import codecs
import numpy as np
import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

file_name = 'training.json'
with codecs.open(file_name, 'r', encoding='iso-8859-1') as f:
    data = f.read()
data = data.split("\n")

N = int(data[0].strip())
topics = []
questions = []
excerpts = []
rows = []
for i in range(1,N+1):
    item = json.loads(data[i])
    topics.append(item['topic'])
    questions.append(item['question'])
    excerpts.append(item['excerpt'])

    row = [item['topic'], item['question'], item['excerpt']]
    rows.append(row)
colnames = ["topic", "question", "excerpt"]
training_df = pd.DataFrame(rows, columns= colnames)


df = sys.stdin.readlines()
df = [line.rstrip() for line in df]
N = int(df[0].strip())
topics = []
questions = []
excerpts = []
rows = []
for i in range(1,N+1):
    item = json.loads(df[i])
    
    questions.append(item['question'])
    excerpts.append(item['excerpt'])

    row = [item['question'], item['excerpt']]
    rows.append(row)

colnames = ["question", "excerpt"]
testing_df = pd.DataFrame(rows, columns= colnames)

vectorizer = CountVectorizer()
classifier = MultinomialNB()

X = vectorizer.fit_transform(training_df['question'] + ' ' + training_df['excerpt'])
y = training_df['topic']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# # Train the model in training data
classifier.fit(X_train, y_train)

X_eval = vectorizer.transform(testing_df['question'] + ' ' + testing_df['excerpt'])
y_eval = classifier.predict(X_eval)

for y in y_eval:
    print(y)
