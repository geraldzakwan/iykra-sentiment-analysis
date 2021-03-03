import sys
import pandas as pd

# Read data/tweets_100k/tweets_100k.csv
# Specify the directory in sys.argv[1]
df = pd.read_csv(sys.argv[1] + "/tweets.csv", encoding='ISO-8859-1', header=None)

# Split positive and negative tweets
positive_tweets = df.iloc[:, 5].values[50000:]
negative_tweets = df.iloc[:, 5].values[:50000]

# Put them accordingly to two different file
with open(sys.argv[1] + "/positive.txt", "w") as outfile:
    for tweet in positive_tweets:
        outfile.write(tweet + "\n")

with open(sys.argv[1] + "/negative.txt", "w") as outfile:
    for tweet in negative_tweets:
        outfile.write(tweet + "\n")
