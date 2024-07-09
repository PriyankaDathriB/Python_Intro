import pandas as pd
from ast import literal_eval

rawData = pd.read_csv("movies.csv")
#print(rawData)


columns = ['genres','director','soup']


print(type(rawData['genres'].tail(2)))

rawData['genres'] = rawData['genres'].apply(literal_eval)

print(type(rawData['genres']))

for val in rawData




