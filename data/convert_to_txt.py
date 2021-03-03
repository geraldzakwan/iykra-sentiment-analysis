import pandas as pd

df = pd.read_csv("tweets_100k.csv", encoding='ISO-8859-1', header=None)

positive_tweets = df.iloc[:, 5].values[50000:]
negative_tweets = df.iloc[:, 5].values[:50000]

with open("positive_tweets_50k.txt", "w") as outfile:
    for tweet in positive_tweets:
        outfile.write(tweet + "\n")

with open("negative_tweets_50k.txt", "w") as outfile:
    for tweet in negative_tweets:
        outfile.write(tweet + "\n")
