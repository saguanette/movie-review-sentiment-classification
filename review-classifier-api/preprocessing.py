from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import contractions
import re


def remove_tags(text):
  soup = BeautifulSoup(text, "html.parser")
  return soup.get_text()

def to_lower(text):
  return text.lower()

def expand_contractions(text):
  return contractions.fix(text)

def remove_noise(text):
  pattern = r'[^a-zA-Z0-9\s]'
  return re.sub(pattern, '', text)

def clean_text(text):
  text_no_tags = remove_tags(text)
  text_lower = to_lower(text_no_tags)
  text_expanded = expand_contractions(text_lower)
  text_cleaned = remove_noise(text_expanded)
  return text_cleaned

def tokenize_text(text):
  return word_tokenize(text, language='english', preserve_line=True)


stop_words = set(stopwords.words('english'))

# negations should be kept
negations = {'no', 'nor', 'not'}
custom_stopwords = stop_words - negations

def remove_stopwords(tokens):
    return [word for word in tokens if word not in custom_stopwords]

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

lemmatizer = WordNetLemmatizer()

def lemmatize_tokens(tokens):
    pos_tags = pos_tag(tokens)
    return [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]

def preprocessing_pipeline(text):
  text = clean_text(text)
  tokens = tokenize_text(text)
  tokens_cleaned = remove_stopwords(tokens)
  tokens_lemmatized = lemmatize_tokens(tokens_cleaned)
  return ' '.join(tokens_lemmatized)

