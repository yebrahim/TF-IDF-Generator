# TF-IDF Generator

This script implements the TF-IDF term relevance scoring as described on wikipedia's article: <en.wikipedia.org/wiki/Tf–idf> to generate the TF-IDF ratings for a collection of documents. This script will also tokenize the input files to extract words (removes punctuation and puts all in lower case), and it will use the NLTK library to lemmatize words (get rid of stemmings)

## Prerequisites:

A REQUIRED library for this script is NLTK, please make sure it's installed along with the wordnet corpus before trying to run this script

## Usage:

* Create a file to hold the paths+names of all your documents (in the example shown: input_files.txt)
* Make sure you have the full paths to the files listed in the file above each on a separate line
* For now, the documents are only collections of text, no HTML, XML, RDF, or any other format
* Simply run this script file with your input file as a single parameter, for example:
 
        python tfidf.py input_files.txt

* This script will generate new files, one for each of the input files, with the prefix "tfidf_" which contains terms with corresponding tfidf score, each on a separate line

This code now supports French (and similar accented European languages), but a lexicon file is needed, which maps a word to its lemmata. An example file for French is given under the name oldlexique.txt
If needed to run using the lexicon file, use the `-l` directive to specify the file, from which the script will load two columns corresponding to the word and its lemmata.
Example usage:

        python tfidf.py -l oldlexique.txt input_files.txt
