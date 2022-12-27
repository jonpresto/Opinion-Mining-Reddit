# Opinion-Mining-Reddit

Web-scraped Text Data using Reddit API onto MongoDB to Harvest Opinions.  This project is broken out into two phases:

Phase 1. Connect to the Reddit API, build an ETL pipeline to extract, transform, and load the data into a NOSQL database (MongoDB), and perform basic queries.

<a href="Notebook - Phase 1">https://github.com/jonpresto/Opinion-Mining-Reddit/blob/main/Stage-01-Webscraping/opinion-nb-m03.ipynb</a>

Phase 2. Perform initial exploratory data analysis, preprocess the text data to remove noise such as nulls and duplicates.  Then apply NLP processing techniques such as stemming, n-gram, removal of stop words using Natural Language Toolkit (NLTK).  Finally, we can visualize the Word cloud and top n-grams and perform topic modeling using LDA.

<a href="Notebook - Phase 2">https://github.com/jonpresto/Opinion-Mining-Reddit/blob/main/Stage-02-Cleaning-Exploring/opinion-nb-c02m03.ipynb</a>

Here is <a href="summary of findings">https://github.com/jonpresto/Opinion-Mining-Reddit/blob/main/Stage-02-Cleaning-Exploring/Goodnotes_Subreddit_Insights_Dec2022.pdf</a>
