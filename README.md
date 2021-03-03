# IYKRA Sentiment Analysis

A simple sentiment analysis module wrapped in `Flask`.

This repo is used as a resource for model deployment sharing at `IYKRA` (https://iykra.com/).

## Assignment

You can choose to work on one of the assignments below

### Assignment 1: Model Optimization

- Take a look at the file `inference.py`. Run it:

`python3 inference.py 10` or `python inference.py 10`

- It will load the saved extractor and model file and do inference on the whole data locally.
The performance and the inference time will be shown as well.

- For the experiment, do it 10 times (or more, feel free to change it) and take the average inference time. This is to make the result more objective.

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

### Assignment 2: Model Update

- Suppose you notice that there are false positive or negative from the model prediction.

- Build an endpoint `/feedback` where it receives an input of something like:

```
{
    "text": "im glad ur doing well",
    "sentiment": "positive"
}
```

- The endpoint should do the following tasks:

1. It checks if the `text` exists in either `positive.txt` or `negative.txt` (just do simple string matching). If it exists, we ignore the request, i.e. do nothing and return something like:

```
{
  "data": {
    "text": "im glad ur doing well",
    "sentiment": "positive",
    "msg": "We have it already!"
  }
}
```

If it doesn't exist, then add it to the suitable file (either `positive.txt` or `negative.txt`) and return something like:

```
{
  "data": {
    "text": "im glad ur doing well",
    "sentiment": "positive",
    "msg": "Your feedback is well received!"
  }
}
```

To add the data to the text file, just append the text file.

2. Keep track of how many new data are added. Hint: Don't store it as a variable, but in an output file (Why?). For example, you can create a file called `count_new_data_added.txt` and update it every time you receive a feedback and add new data.

3. Retrain your model (feature extractor and classifier) whenever `10` new data is added! Hint: Call `train.main()` function to retrain.

Note: In practice, `10` data is insignificant. We usually train if the data size grows `5-10%` larger from the previous version. In our case, that means `5-10k` data. We don't want to retrain too often as it waste resources. Also, it's common in industry to retrain periodically as well (every 2 weeks for example).

- Bonus:

1. Modify the `/feedback` endpoint so that it receives a list instead, e.g.

```
{
    "text": "[im glad ur doing well, im not glad ur doing well]",
    "sentiment": "[positive, negative]"
}
```

2. Do simple model versioning every time the model is updated! For example, before the first model update, change the `classifier_latest.pk` and `feature_extractor_latest.pk` to `classifier_v0.pk` and `feature_extractor_v0.pk`. Then, after model update you will have `4` files. Furthermore, after the second model update, you will have `6` files (`v0`, `v1` and `latest`).

Note that one benefit from versioning your model is that you can revert back if your latest model is bad!

## Serious Notes

You shouldn't change too much code! You probably add/remove/change the total of 20 lines at most for both assignments (unless you do the bonus part for Assignment 2).

## Questions

- If you have questions or have difficulties with the assignment, please email me (`geraldi.dzakwan@gmail.com`) with email subject: `IYKRA Assignment - {Your name}`, e.g. `IYKRA Assignment - Geraldi Dzakwan`.

- Thanks and good luck!

Cheers,

Geral
