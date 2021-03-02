# IYKRA Sentiment Analysis

A simple sentiment analysis module wrapped in `Flask`.

This repo is used as a resource for model deployment sharing at `IYKRA` (https://iykra.com/).

## Assignment

- Take a look at the file `inference.py`. Run it:

`python3 inference.py` or `python inference.py`

- It will load the saved extractor and model file and do inference on the whole data locally.
The performance and the inference time will be shown as well.

- Screenshot/copy the result.

- Your task is to modify the `train.py` and/or `preprocess.py` and train your own model.

- Search for `"# NOTE"` in both files where I put the part of the code I suggest you to modify (but feel free to modify other parts too!).

- The goal is to reduce the total inference time without losing too much performance. Say you can reduce the inference time by 20% with only losing 2% accuracy. That's respectable.

- Report your experiment result and detail on what you do in 1 page PDF file (yes, be concise!). Explain why your solution works!

- If you didn't manage to reduce the inference time that's okay. Just report what you do and argue why it fails.

- Some hint to get you kicking:

1. Take a look into `TfidfVectorizer` hyperparameters, what can you change/add to improve the speed?

2. Explore other kind of text vectorizer such as: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html.

3. Do we actually need a `stemmer`? Investigate!

4. Are there faster models, e.g. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html?

5. Is there any unmeaningful words we can remove in preprocessing? Google `"stopwords"`.

- Some serious note: You shouldn't change too much code! You probably add/remove/change the total of 10 lines at most.

## Questions

- If you have questions or have difficulties with the assignment, please email me (`geraldi.dzakwan@gmail.com`) with email subject: `IYKRA Assignment - {Your name}`, e.g. `IYKRA Assignment - Geraldi Dzakwan`.

- Thanks and good luck!

Cheers,

Geral
