import time
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

from config import DATA_FILEPATH, FEATURE_EXTRACTOR_FILEPATH, CLASSIFIER_FILEPATH
import preprocess as pr

# This function is speficic for Sentiment140 dataset
def load_dataset():
    # Read data/tweets_100k/positive.txt
    with open(DATA_FILEPATH + "/positive.txt", "r") as infile:
        positive_tweets = infile.readlines()

    # Do the same with negative tweets
    with open(DATA_FILEPATH + "/negative.txt", "r") as infile:
        negative_tweets = infile.readlines()

    X = negative_tweets + positive_tweets
    y = np.concatenate([np.full(len(negative_tweets), 0), np.full(len(positive_tweets), 4)])

    return X, y

# Train test split and preprocess
def prepare_data(X, y, test_size):
    # EXERCISE 3: Do 80/20 train test split
    # X_train, X_test, y_train, y_test = ...

    # Preprocess pipeline (see preprocess.py), convert sentences to their numerical representation
    X_train = [pr.preprocess(tweet, do_stem=True) for tweet in X_train]
    X_test = [pr.preprocess(tweet, do_stem=True) for tweet in X_test]

    return X_train, X_test, y_train, y_test

def extract_feature(X, vec, fit):
    # EXERCISE 4: transform feature
    # Fit means that we train our extractor using the data (do this with train data)
    if fit:
        # return vec.
        pass

    # No fit means that we only apply extraction to the data (do this with test data)
    # return vec.

def train(cls, X, y):
    # EXERCISE 5: Train classifier cls
    # return cls.
    pass

def predict(cls, X):
    # EXERCISE 6: Predict X
    # return cls.
    pass

def get_pred_statistics(y, pred):
    print("Accuracy: {:.2f}".format(metrics.accuracy_score(y, pred)*100))
    print()

    print("Confusion matrix:")
    print(metrics.confusion_matrix(y, pred))
    print()

    cm = metrics.confusion_matrix(y, pred)

    print("Classification report:")
    print(metrics.classification_report(y, pred))
    print()

# Save both the feature extractor and the classifier with pickle
def save(feat_ext, cls, cls_filepath=CLASSIFIER_FILEPATH, feat_ext_filepath=FEATURE_EXTRACTOR_FILEPATH):
    # EXERCISE 7: Save feature extractor and classifier
    with open(feat_ext_filepath, 'wb') as outfile:
        # pickle.dump(...)
        pass

    with open(cls_filepath, 'wb') as outfile:
        # pickle.dump(...)
        pass


if __name__ == '__main__':
    # To log the training time
    start = time.time()

    X, y = load_dataset()

    X_train, X_test, y_train, y_test = prepare_data(X, y, test_size=0.2)

    # EXERCISE 8: Use TF-IDF as feature extractor
    # extractor = ...

    # Apply feature extractor, e.g. TF-IDF, on train data
    X_train_vec = extract_feature(X_train, extractor, fit=True)

    # EXERCISE 9: Define your classifier, e.g. Naive Bayes
    # classifier = ...

    train(classifier, X_train_vec, y_train)

    save(extractor, classifier)

    print("*"*50)
    print()

    print("Training finish in {:.2f} seconds".format(time.time() - start))
    print()

    print("Statistics using train data:")
    print()

    # Get prediction on training data
    pred = predict(classifier, X_train_vec)

    get_pred_statistics(y_train, pred)

    print("*"*50)
    print()

    print("Statistics using test data:")
    print()

    # Apply TF-IDF on test data
    # IMPORTANT: Don't fit again, just transform! Why?
    X_test_vec = extract_feature(X_test, extractor, fit=False)

    # Get prediction on training data
    pred = predict(classifier, X_test_vec)

    get_pred_statistics(y_test, pred)

    print("*"*50)
    print()
