import pandas as pd
import numpy as np
import nltk
#nltk.download('stopwords')
pd.set_option("display.max_rows", 600)

#Import csv
df = pd.read_csv('running-comments.csv')

#Take just the comments
all_comments = str(df.body)

#Tokenize all comments
tokens = nltk.word_tokenize(all_comments)

#Create stopwords
#stop_words = set(stopwords.words('english'))
#
#filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
#filtered_sentence = []
#
#Cycle through stopwords and append
#for w in tokens:
#    if w not in stop_words:
#        filtered_sentence.append(w)

#Create Series
series = pd.Series(tokens)

#Create dataframe of words and their counts
df2 = pd.DataFrame(series.value_counts())

#Export to CSV
#df2.to_csv('output.csv')

#Debug export
#df2.to_csv('debug1.csv')
print(df2)