# Opinion-Mining-Reddit

Web-scraped Text Data using Reddit API onto MongoDB to Harvest Opinions.  This project is broken out into two phases:

Phase 1:
* Connect to the Reddit API
* build an ETL pipeline to extract, transform, and load the data into a NOSQL database (MongoDB)
* perform basic queries

<a href="https://github.com/jonpresto/Opinion-Mining-Reddit/blob/main/Stage-01-Webscraping/opinion-nb-m03.ipynb">Notebook: Phase 1</a>

Phase 2: 
* Perform initial exploratory data analysis
* Preprocess the text data to remove noise such as nulls and duplicates
* Apply NLP processing techniques such as stemming, n-gram, removal of stop words using Natural Language Toolkit (NLTK)
* Visualize the Word cloud and top n-grams and perform topic modeling using LDA

<a href="https://github.com/jonpresto/Opinion-Mining-Reddit/blob/main/Stage-02-Cleaning-Exploring/opinion-nb-c02m03.ipynb">Notebook: Phase 2</a>

Here is <a href="https://github.com/jonpresto/Opinion-Mining-Reddit/blob/main/Stage-02-Cleaning-Exploring/Goodnotes_Subreddit_Insights_Dec2022.pdf">summary of findings</a>.
