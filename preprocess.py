import re
import nltk

def preprocess(tweet, do_stem=True):
    # Convert to lower case
    tweet = tweet.lower()

    # Remove all quotations: ' and "
    tweet = tweet.strip('\'"')

    # Remove newlines
    tweet = tweet.strip('\n')

    # Convert links in the form of www.* or https?://* to "URL"
    # e.g. www.google.com -> "URL". Why?
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)

    # Convert @username to __userhandle__
    # e.g. @geraldzakwan -> __userhandle__. Why?
    tweet = re.sub('@[^\s]+','__userhandle__',tweet)

    # Replace hashtag: #word with the word itself
    # e.g. #liverpool -> liverpool. Why?
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    # Remove repeating chars
    # e.g. helloooo -> hello
    repeat_char = re.compile(r"(.)\1{1,}", re.IGNORECASE)
    tweet = repeat_char.sub(r"\1\1", tweet)

    # List of positive and negative emoticons
    emoticons = \
    [
     ('__positive__',[ ':-)', ':)', '(:', '(-:', \
                       ':-D', ':D', 'X-D', 'XD', 'xD', \
                       '<3', ':\*', ';-)', ';)', ';-D', ';D', '(;', '(-;', ] ),\
     ('__negative__', [':-(', ':(', '(:', '(-:', ':,(',\
                       ':\'(', ':"(', ':((','D:' ] ),\
    ]

    def replace_parenthesis(arr):
       return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]

    def join_parenthesis(arr):
        return '(' + '|'.join( arr ) + ')'

    # Build emoticon regex
    emoticons_regex = [(repl, re.compile(join_parenthesis(replace_parenthesis(regx)))) \
                        for (repl, regx) in emoticons]

    # Replace positive emoticons with "__positive__"
    # and negative emoticons with "__negative__"
    for (repl, regx) in emoticons_regex:
        tweet = re.sub(regx, ' ' + repl + ' ', tweet)

    if do_stem:
        tweet = stem(tweet)

    return tweet

# Stem using PorterStemmer from NLTK
def stem(tweet):
    # NOTE: You can play with this, i.e. try other stemmer types!
    stemmer = nltk.stem.PorterStemmer()

    # EXERCISE 1: Simply tokenize by space
    # words = ...

    # EXERCISE 2: Stem each token
    # words = ...

    # Rejoin them
    return ' '.join(words)
