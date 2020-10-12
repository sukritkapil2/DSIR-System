#importing the required libraries
import sys
import glob
import os
from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import json
import store_scores_gui
from store_scores_gui import main_class
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
from urllib import parse
import requests

'''
    This is the category page where you can search for the quotes by categories
'''
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('categories.html')

'''
    This is the authors page where you can search for the quotes by author's name. The list is sorted alphabetically.
'''
@app.route('/authors', methods=['GET', 'POST'])
def authors():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('authors.html')

@app.route('/')
def homepage():
    return render_template("index.html")

'''
    This is the Result page which shows the most relevant 10 quotes.
'''
@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		query = request.form["query"]
	html="<!DOCTYPE html> <head><link rel=stylesheet type=text/css href=static/bootstrap.min.css></head><body>"
	html+="<div style='height: 10vh'> <div class='text-center'><h2>Search results for <i><b>"+query+"</b></i></h2></div></div>"

	result = main_class.process_function(query)
    
	for docname in result:
		html+="<div><div style=\"margin-left:90px\"><a class='resultxx'>"+docname+"</a><br></div><br>"
	html+="<div class=text-center animated fadeIn mb-3><h4><a href=/>Search Again</a></h4></div>"
	html+="</body></html>"
	return html


if __name__ == '__main__':
	app.run(debug = True)
