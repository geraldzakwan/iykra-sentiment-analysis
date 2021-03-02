import time
import pickle

from train import load_dataset, extract_feature, predict, get_pred_statistics
from config import DATA_FILEPATH, FEATURE_EXTRACTOR_FILEPATH, CLASSIFIER_FILEPATH

if __name__ == '__main__':
    # To log the total time
    start = time.time()

    X, y = load_dataset()

    with open(FEATURE_EXTRACTOR_FILEPATH, 'rb') as infile:
        extractor = pickle.load(infile)

    with open(CLASSIFIER_FILEPATH, 'rb') as infile:
        classifier = pickle.load(infile)

    # Apply feature extractor, e.g. TF-IDF, on the whole data
    X_vec = extract_feature(X, extractor, fit=False)

    print("*"*50)
    print()

    print("Statistics using test data:")
    print()

    # Get prediction on whole data
    pred = predict(classifier, X_vec)

    get_pred_statistics(y, pred)

    print("*"*50)
    print()

    print("Your total inference time is: {} seconds".format(time.time() - start))
