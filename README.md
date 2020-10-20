## The program/application can be broken down into the various subparts (actual file names also added) :

1. jsonconverter.py:
 converting corpus(quotes.json) to individual json file(quotes )
2. store_authors_list.py:
  getting authors from corpus and saving it as authors.json
3. category.py
   getting category from corpus and saving it as category.json
4. store_document_tokens_list.py:
Stores the tokenized words of each document as lists and then the corresponding list is stored in a json file.

5. store_vocabulary.py:
Stores all the unique words present in the corpus

6. store_megadict.py:
creates a dictionary which contains the words in the vocabulary as the key and the
value as another dictionary which contains each document as key and its value is one more dictionary as which contains the TF,IDF and TF-IDF values.

7. document_normalized_denominator.py:
   precalculating normalized length of each documents.

8.  store_scores_gui.py:
Takes query as input and calculates the scores for each document.

9. final_gui.py: Contains the gui program writtem in flask framework for python to accept query and receive the names of the top 10 documents with the highest scores

## Order of executing the files.
```
$ sudo python3 jsonconverter.py
$ sudo python3 store_authors_list.py
$ sudo python3 category.py
$ sudo python3 store_document_tokens_list.py
$ sudo python3 store_vocabulary.py
$ sudo python3 store_megadict.py
$ sudo python3 document_normalized_denominator.py
$ sudo python3 store_scores_gui.py
$ sudo python3 final_gui.py

```


## DATA STRUCTURES USED:

### Document_tokens_list
Contains lists enclosed within a list
It will contain the stemmed tokens from each file in the corpus as individual lists. All are appended to
make a list. Example:
```
[[‘i’,’play’,’cricket’],[‘sachin’,’tendulkar’],[‘india’,’is’,’best’]]
```
### Vocabulary
Will contain a dictionary of all the unique words in the corpus. Example:
```
{‘i’: 1, ‘play’:2, ‘cricket’:3, ‘sachin’:4, ‘tendulkar’ :5, ‘india’:6 , ‘is’ :7, ‘best’:8]
```
### Prime Dictionary
A nested dictionary containing the following structure explained through the following example:(Numbers are just representational )

```
{‘i’:{‘0’: {‘TF’:1 ,“IDF”:0.8, ‘TF-IF’ : 0.8} , ‘1’:{‘TF’: 2 ,‘IDF’: 0.4, ‘TF-IDF’:0.8}, ‘2’:{‘TF’: 0 ,‘IDF’: 0.78,
‘TF-IDF’:0.8}} , ‘cricket’ :{‘0’: {‘TF’:2 ,“IDF”:0.6, ‘TF-IF’ :1.2} , ‘1’:{‘TF’: 0 ,‘IDF’: 0.4, ‘TF-IDF’:1.2}, ‘2’:{ ‘TF’: 1
,‘IDF’: 0.4, ‘TF-IDF’:1.2}}}
```
### Scores
A dictionary which will contain the scores of the documents after inputting the query and running cosine similarity algorithm. Example :
```
{‘0’: 0.2323 , ‘1’: 0.3125 , ‘2’ : 0.467 }
```
## Creating the GUI

Flask Framework V-1.0.2 has been used to create the GUI. It is a web application framework written in Python. It contains boilerplate code consisting of html, css and bootstrap files for easy front-end development.

On the homepage, the user can search for the quotes using words, author's name or even categories using the search box. Top 10 most relevant quotes along with their authors will be displayed over the next page.

There are options for searching Popular Authors and Category-wise quotes as well on the homepage.

<-Screenshots->
1) Offline
	(Path= ./Screenshots/)
2) Online (Requires BITS-Mail)
	https://drive.google.com/open?id=1_T4MgKGKjUPu7uQ-5TnnF62PfKiTiavk

## Built and Tested on Machine with following specs:
1) Processor: i5 7200U
2) RAM- 8GB DDR3
3) OS- macOS High Sierra 10.13.3


## Group members
1. Ayush Kumar Tiwary    -- 2016A2PS0567H
2. Mukesh                -- 2016A7PS0116H
3. Srijan Soni           -- 2016A4PS0328H
4. Vivek pratap Deo      -- 2016A7PS0056H
