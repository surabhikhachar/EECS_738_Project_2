import numpy as np
import pandas as pd

filename = 'examiner-date-tokens.csv'

#This is for running the python script from a subdirectory of root. Modify as needeed
df_text = pd.read_csv('../Data/'+filename)
df_text.head()

wordArray = []
headlines = df_text['headline_tokens']
for headline in headlines:
    for word in headline.split():
        wordArray.append(word)


uniqueWords = list(set(wordArray))
uniqueWords.sort()
uniqueWordCount = len(uniqueWords)

print("Number of words in all headlines:", len(wordArray))
print("Number of unique words used:", uniqueWordCount)

words = dict.fromkeys(uniqueWords)
index = 0
for word in words:
    words[word]=index
    index += 1

transitionCount = np.zeros((uniqueWordCount+1, uniqueWordCount+1))
transition2Count = np.zeros((uniqueWordCount+1, uniqueWordCount+1))

for headline in headlines:
    sentence = headline.split()
    for i in range(len(sentence)):
        if i < len(sentence) - 1:
            transitionCount[words[sentence[i]]][words[sentence[i+1]]] += 1
        else:
            transitionCount[words[sentence[i]]][uniqueWordCount] += 1

        if i < len(sentence) - 2:
            transition2Count[words[sentence[i]]][words[sentence[i+2]]] += 1
        else:
            transition2Count[words[sentence[i]]][uniqueWordCount] += 1

print(transitionCount[words['happy']][words['new']])
print(transitionCount[words['new']][words['year']])
print(transition2Count[words['happy']][words['year']])

transitionCountNorm = transitionCount / transitionCount.sum(axis=1)
print(transitionCountNorm[words['happy']][words['new']])
