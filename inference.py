import sys
import time
import pickle

from train import load_dataset, extract_feature, predict, get_pred_statistics
from config import DATA_FILEPATH, FEATURE_EXTRACTOR_FILEPATH, CLASSIFIER_FILEPATH

if __name__ == '__main__':
    total_time = 0

    for i in range(0, int(sys.argv[1])):
        # To log the inference time
        start = time.time()

        X, y = load_dataset()

        with open(FEATURE_EXTRACTOR_FILEPATH, 'rb') as infile:
            extractor = pickle.load(infile)

        with open(CLASSIFIER_FILEPATH, 'rb') as infile:
            classifier = pickle.load(infile)

        # Apply feature extractor, e.g. TF-IDF, on the whole data
        X_vec = extract_feature(X, extractor, fit=False)

        if i == 0:
            print("*"*50)
            print()

            print("Statistics using test data:")
            print()

        # Get prediction on whole data
        pred = predict(classifier, X_vec)

        if i == 0:
            get_pred_statistics(y, pred)

        total_time += time.time() - start

    print("Your average inference time is: {} seconds".format(total_time/int(sys.argv[1])))
    print("*"*50)
