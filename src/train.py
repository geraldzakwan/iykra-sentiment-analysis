import time
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

from __init__ import DATA_FILEPATH, FEATURE_EXTRACTOR_FILEPATH, CLASSIFIER_FILEPATH
import preprocess as pr

# This function is speficic for Sentiment140 dataset
def load_dataset():
    df = pd.read_csv(DATA_FILEPATH, encoding='ISO-8859-1', header=None)

    # Column 5 is the tweet
    X = df.iloc[:, 5].values
    X = pd.Series(X)

    # Column 0 is the label (positive/negative)
    y = df.iloc[:, 0].values

    return X, y

# Train test split and preprocess
def prepare_data(X, y, test_size):
    # 80/20 train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=28)

    # Preprocess pipeline (see preprocess.py)
    X_train = [pr.preprocess(tweet, do_stem=True) for tweet in X_train]
    X_test = [pr.preprocess(tweet, do_stem=True) for tweet in X_test]

    return X_train, X_test, y_train, y_test

def extract_feature(X, vec, fit):
    # Fit means that we train our extractor using the data (do this with train data)
    if fit:
        return vec.fit_transform(X)

    # No fit means that we only apply extraction to the data (do this with test data)
    return vec.transform(X)

def train(cls, X, y):
    return cls.fit(X, y)

def predict(cls, X):
    return cls.predict(X)

def get_pred_statistics(y, pred):
    print("Accuracy: {:.2f}",format(metrics.accuracy_score(y, pred)*100))
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
    with open(feat_ext_filepath, 'wb') as outfile:
        pickle.dump(feat_ext, outfile, protocol=pickle.HIGHEST_PROTOCOL)

    with open(cls_filepath, 'wb') as outfile:
        pickle.dump(cls, outfile, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    # To log the training time
    start = time.time()

    X, y = load_dataset()

    X_train, X_test, y_train, y_test = prepare_data(X, y, test_size=0.2)

    # Use TF-IDF as feature extractor
    # NOTE: You can play with this, i.e. try other extractors or change hyperparameters!
    extractor = TfidfVectorizer(min_df=5, use_idf=True, ngram_range=(1, 4))

    # Apply feature extractor, e.g. TF-IDF, on train data
    X_train_vec = extract_feature(X_train, extractor, fit=True)

    # Define your classifier, e.g. Naive Bayes
    # NOTE: You can play with this, i.e. try other classifiers or change hyperparameters!
    classifier = MultinomialNB()

    train(classifier, X_train_vec, y_train)

    save(classifier, extractor)

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
