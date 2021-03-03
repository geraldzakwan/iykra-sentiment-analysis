# IYKRA Sentiment Analysis

A simple sentiment analysis module wrapped in `Flask`.

This repo is used as a resource for model deployment sharing at `IYKRA` (https://iykra.com/).

## Getting Ready

### Git

- You will use Git (and GitHub) to access this code base and to submit the assignment later.

- Create a GitHub account (https://github.com/)

- Install Git: https://www.atlassian.com/git/tutorials/install-git.

- Learn a bit about Git: https://opensource.com/article/18/1/step-step-guide-git.

- (Optional) If you want to dive deeper: https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6.

- Fork this repo, follow the instruction here: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

- Clone the forked repo by running the following command inside your terminal:

`git clone https://github.com/{Your-GitHub-username}/iykra-sentiment-analysis`

- It will create `iykra-sentiment-analysis` directory in your local machine, please remember the path to this directory.

### Python

- We're using `Python` as our main programming language (and some libraries in it).

- Install `Python3.6` or above (https://realpython.com/installing-python/).

- Check it, for example you can run: `python3 --version` or `python --version` in your terminal.
  You're okay if the output says it's `Python3.6` or above.

- Inside the `iykra-sentiment-analysis` directory, please run the following commands to install the libraries:

`pip3 install -r requirements.txt`

- If the above doesn't work, try:

`pip install -r requirements.txt`

- (Optional) If you're familiar with `virtualenv`, run the above command inside your virtual environment.
  Please refer here: https://www.petanikode.com/python-virtualenv/.

- Run:

`cp env.sample .env`

`python3 app.py` or `python app.py`

- See if it's running okay. If it's running okay then run this on your terminal:

```
curl --location --request POST 'http://localhost:5000/classify' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "im glad ur doing well"
}'
```

- You should see this output as the result:

```
{
  "data": {
    "sentiment": "positive",
    "text": "im glad ur doing well"
  }
}
```

- You can change the value of the `text` field with any English sentence to see the predicted sentiment.

- Alternatively, if the above doesn't work for you, you can access the model that I've deployed on `Heroku` by running this command:

```
curl --location --request POST 'https://iykra-sentiment-analysis-geral.herokuapp.com/classify' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "im glad ur doing well"
}'
```

### IDE

- Install your favorite `IDE`, mine is `Atom` (https://atom.io/). Atom is very light (got it?)!

- Some other alternatives are `PyCharm` (https://www.jetbrains.com/pycharm/) and `Microsoft Visual Studio` (https://visualstudio.microsoft.com/).

### Postman

- We will use `Postman` to test our deployed ML model.

- Install `Postman` (https://learning.postman.com/docs/getting-started/installation-and-updates/).

### Heroku

- Please create a `Heroku` account: (https://www.heroku.com/).

- Install `Heroku CLI` (https://devcenter.heroku.com/articles/heroku-command-line).

- (Optional): Read these two amazing resources on deploying Flask to Heroku:

https://stackabuse.com/deploying-a-flask-application-to-heroku/

https://www.jcchouinard.com/deploy-a-flask-app-on-heroku/

- We will follow closely the above resource in the training session.

### Dataset

Please refer here: https://github.com/geraldzakwan/iykra-sentiment-analysis/tree/main/data.

### Libraries

Get to know about these two main libraries for our project:

- `scikit-learn`

- `flask`

and briefly about these other libraries:

- `pandas`

- `nltk`

- `gunicorn`

## Questions

- If you have difficulties or find some errors following the above instructions, please email me (`geraldi.dzakwan@gmail.com`) with email subject: `IYKRA Getting Ready - {Your name}`, e.g. `IYKRA Getting Ready - Geraldi Dzakwan`.

- Explain your difficulties/errors and provide screenshot if any.

- Thanks and see you Friday!

Cheers,

Geral
