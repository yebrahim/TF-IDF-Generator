#!/usr/bin/env python
# encoding: utf-8

"""
File: tfidf.py
Author: Yasser Ebrahim
Date: Oct 2012

Generate the TF-IDF ratings for a collection of documents.

This script will also tokenize the input files to extract words (removes punctuation and puts all in
    lower case), and it will use the NLTK library to lemmatize words (get rid of stemmings)

IMPORTANT:
    A REQUIRED library for this script is NLTK, please make sure it's installed along with the wordnet
    corpus before trying to run this script

Usage:
    - Create a file to hold the paths+names of all your documents (in the example shown: input_files.txt)
    - Make sure you have the full paths to the files listed in the file above each on a separate line
    - For now, the documents are only collections of text, no HTML, XML, RDF, or any other format
    - Simply run this script file with your input file as a single parameter, for example:
            python tfidf.py input_files.txt
    - This script will generate new files, one for each of the input files, with the prefix "tfidf_"
            which contains terms with corresponding tfidf score, each on a separate line

"""

import sys, re, math
from nltk.stem.wordnet import WordNetLemmatizer

# we maintain an array of (words-freq) pairs for each document
global_terms_in_doc = {}
global_term_freq    = {}
num_docs            = 0

# function to tokenize text, and put words back to their roots
def tokenize(str):

    # remove punctuation
    tokens = re.findall(r"<a.*?/a>|<[^\>]*>|[\w'@#]+", str.lower())

    # lemmatize words. try both noun and verb lemmatizations
    lmtzr = WordNetLemmatizer()
    for i in range(0,len(tokens)):
        res = lmtzr.lemmatize(tokens[i])
        if res == tokens[i]:
            tokens[i] = lmtzr.lemmatize(tokens[i], 'v')
        else:
            tokens[i] = res
    return tokens

reader = open(sys.argv[1])
all_files = reader.read().splitlines()

num_docs  = len(all_files)

for f in all_files:
    
    # local term frequency map
    terms_in_doc = {}
    
    file_reader  = open(f)
    doc_words    = tokenize(file_reader.read())
    
    # increment local count
    for word in doc_words:
        if word in terms_in_doc:
            terms_in_doc[word] += 1
        else:
            terms_in_doc[word]  = 1

    # increment global frequency
    for (word,freq) in terms_in_doc.items():
        if word in global_term_freq:
            global_term_freq[word] += 1
        else:
            global_term_freq[word]  = 1

    global_terms_in_doc[f] = terms_in_doc

for f in all_files:

    writer = open('tfidf_' + f, 'w')
    # iterate over terms in f, calculate their tf-idf
    for (term,freq) in global_terms_in_doc[f].items():
        idf = math.log(float(1 + num_docs) / float(1 + global_term_freq[term]))
        print('term: ' + term + ' - tf = ' + str(freq) + ', idf = ' + str(global_term_freq[term]))
        tfidf = freq * idf
        writer.write(term + '\t' + str(tfidf) + '\n')

print('success, with ' + str(num_docs) + ' documents.')
