# EECS 738 Project 2: Hidden Markov Models

This is Surabhi Khachar and Andre Kurait's second project for EECS 738, Machine Learning in Spring 2019. For the project one, we built a Hidden Markov Model using Python and tested it on datasets from Kaggle.

The project requirements were the following:

1. Set up a new git repository in your GitHub account
2. Pick a text corpus dataset such as 
https://www.kaggle.com/kingburrito666/shakespeare-plays 
or from https://github.com/niderhoff/nlp-datasets 
3. Choose a programming language (Python, C/C++, Java)
4. Formulate ideas on how machine learning can be used to learn word correlations and distributions within the dataset
5. Build a Hidden Markov Model to be able to programmatically
    1. Generate new text from the text corpus
    2. Perform text prediction given a sequence of words
6. Document your process and results
7. Commit your source code, documentation and other supporting files to the git repository in GitHub

## Data
The data chosen for this project was from "The Examiner - SpamClickBait News Dataset" (https://www.kaggle.com/therohk/examine-the-examiner#examiner-date-tokens.csv) found from https://github.com/niderhoff/nlp-datasets 

Data features headlines from 3 million articles

## Hidden Markov Model Algorithm:
We began by randomly sampling from the dataset as it was too computationally difficult at full size.
We then implemented a Markov Model based on the transition probabilities of the past two words in the headlines.
Although a Markov Model has no memory of the previous state, this can still be represented as a traditional markov model with n^2 states where n is the number of unique words.

Extending this to our hidden state, we took the concept that long words are less likely followed by additional long words and created two hidden states, one that prefers short words and one that prefers longer words. The emission probabilities were based off of this hidden state which was not observed making this a Hidden Markov Model.