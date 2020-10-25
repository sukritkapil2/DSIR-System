## jsonconverter.py
    - jsonconverter() is being called which creates individual json files for each book.

## jsonconverter()
    - Function for creating individual json files for storing each book.
    - Data taken from: books.json
    - Data stored in: /jsonnn

## store_categories_authors.py
    - create_author_category() is being called which creates json for storing authors and categories.

## create_author_category()
    - Function for storing unique authors and categories list.
    - Data taken from: /jsonnn
    - Data stored as: /savers/categories.json and /savers/authors_list.json

## store__document_tokens_list.py
    - create_document_tokens_list() is being called which is tokenizing the file.

## create_document_tokens_list();
    - Function for creating document_tokens_list and then storing in json file for further usage and then function is being called.
    - Data taken from: /jsonnn
    - Data stored in: /savers/document_tokens_list.json

## store_vocabulary.py
    - compute_vocabulary() is called which accesses build_vocabulary() function to build the vocabulary.
    - The functions used are:
    - compute_vocabulary()
    - build_vocabulary()

## compute_vocabulary():
    - Function is retreiving the document_tokens_list to create the vocabulary,then storing the vocabulary in a json file
    - Data taken from : /savers/document_tokens_list.json
    - functions called : build_vocabulary(document_tokens)
    - Data stored in : /savers/vocabulary.json

## build_vocabulary():
    - Function for building the vocabulary i.e. the dictionary which has all the unique words in the jsonnn
    - Parameters given: document_tokens

## store_megadict.py
    - The code is for creating the dictionary which contains all the unique words and their tf,idf and tf-idf in each document..
    - The structure of dictionary is as follows-
    - It is a nested dictionary which contains-
    - Dictionary1-containing word of vocabulary
        - Dictionary2-containing the document number
            - Dictionary3-contains Tf,Idf,Tf_idf for each document

    - Data for making the above dictionary is taken from
    1.Vocabulary - list of all word in the dictionary.
    2.Document Token list - list of all files containing books.


## Descriptions of function-

### buildIDF()--
    For counting the number of documents in which a word is appearing.

### buildFreqDist()--
    For counting the frequency of each word in the particular document.

### returnIdf()--
    Returns the calculated idf for each word for each document.

### returnTermFrequency()--
    Returns the tf value of each term in a document.


## document_normalized_denominator.py

    This code is for creating a normalized denominator i.e length for each document. It creates a list which creates normalized length for each document. It saves the normalized length in a file to avoid computation again and again while seaching for quering.

## store_scores_gui.py
    Data accessed from :
    - /savers/primeDictionary.json
    - /savers/normaliseddenom.json
    - /savers/score.json'

    Functions called:
    - terminal_function()
    - process_function()

    Data returned to :
    - /savers/store.json

### process_function()
    - Function for inputting query and performing query based operations and finally calculating cosine scores. It performs the following features:
    1. Applying stemming porting on query
    2. calculating tf and idf for query
    3. for every word in query_wt we parse all documents

## final_gui.py
    - This file is for creating the GUI as well as processing the query based on author, words or categories. It uses Flask framework for the front-end work. CSS and JS files are provided in separate folders.

    - Functions used:
    1) homepage()- This is the homepage
    2) about()- This is used to redirect user to about.html
    3) result() - This is used to create GUI of the final results page consisting of 10 results. It uses process_function() of store_scores_gui.py
