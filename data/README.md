## Data Source

- I use the `Stanford Sentiment140` data, a sentiment analysis data (positive and negative) from tweets.

- Please refer to this link for the details: `https://www.kaggle.com/kazanova/sentiment140`.

- The full version of the data consists of `1.6 million` tweets.

- But, to make it quick for everyone to train on, I use only `100k` tweets (see `tweets_100k.csv` file). It should take a minute maximum.

- Half of them are positive sentiments and another half are negative sentiments.

- In the CSV file, positive sentiments are denoted by label 4, meanwhile negative sentiments are denoted by 0.

- I preprocess the CSV file and take only the label information (0/4) and the tweet itself, ignoring the other fields like tweet ID and date.

- I put them into two simpler text files (see `data/convert_to_txt.py`):

1. `positive_tweets_50k.txt`, in which every line contains a tweet with a positive sentiment.

2. `negative_tweets_50k.txt`, in which every line contains a tweet with a negative sentiment.
