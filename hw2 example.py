#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Due Wednesday October 21st before midnight

Your task today is to parse the US Energy Information Administration's annual energy outlook reports. 
The goal is code that summarizes the predictions in a table for a given year, so it can be re-run on 
every year with a similar format. You will just be working with 2019 and 2018.

Fortunately the required information is availble in the "key takeaway" sections at beginning of 
the documents, so you can ignore the rest (e.g. pages 9-28 in the 2019 table of contents). 
The end result should be two (one for each year) csv documents with the columns "energy type",
 "price", "emissions", "production", "export/import". There should be five rows of data, one for 
 each energy type of "coal", "nuclear", "wind", "solar", and "oil". The values in the other columns 
 should be a rough categorization of the predictions - will price go up or down, will emissions 
 increase or decrease, will exports increase or decrease, and so on. The exact details are open 
 to what you think is best, as long as it helps summarize the key takeaways. Obviously if 
 the document doesn't say anything about a certain value in the table, it should be a missing 
 value or a zero.

    Remember to break your work into bite-size pieces, and then generalize!
        First, focus on one year.
        Second, focus on one value.
        When you have something working for one value, generalize it to the other values.
        When you have something working for one whole year, generalize it to the other year.
    You should retrieve the pdf documents from their respective urls within your code.
    As we did in the NLP lecture, test your code on small blocks of text rather than the entire document.
    Remember all we've talked about for good testing and debugging practices.
    Ask for help; speak with the TAs, come see or email me, or use Piazza
    The final format of the two tables is not rigid. If you think a slight change 
    (e.g. to a column description, or adding a new column or row) would make the data 
    easier to summarize, you can do that.
    Please include a small comment block (around 5-10 lines, give or take) 
    that outlines the logic of your code, and points out any remaining weaknesses.
    Your code must utilize functions appropriately.
    Do as much as you can - partial credit counts!

"""
import PyPDF2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
import os

# You want to only specify the path once! Don't hard code throughout code

path = '/Users/Emily/Documents/GitHub/assignment-2'
os.chdir(os.path.expanduser(path)) # for macs

df = pd.read_csv(os.path.join(path, 'filename'))

df = pd.read_csv(os.path.join('/Users/Emily/Documents/GitHub/filename')

negative_words = []
positive_words = []

def read_in_pdf(filename):
    '''
    Pulls a word from a url.
    
    Input:
        - url (string)
    Output:
        - words (string)
    '''
    # this line does this
    return words
    
def tokenize_and_clean(words):
	return clean_tokens

def check_direction(tokenized_list):
	return final_df



words = pull_url('url')
tokens = tokenize(words)
print(check_direction(tokens))


if __name__ == '__main__': # you don't need a main function - can also run
    words = pull_url('url')
	tokens = tokenize(words)
    print(check_direction(tokens))
    
    
    
    
    