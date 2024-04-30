from flask import Flask
from reddit_data import reddit_data
from preprocess import preprocess_text_with_tfidf, preprocess\
from flask import Blueprint, jsonify, request
import praw
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

