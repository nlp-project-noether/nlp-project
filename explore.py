# imports
import pandas as pd
import nltk
import re
import unicodedata
import os
#imports
import matplotlib.pyplot as plt
import seaborn as sns


def word_freq_new_df(df, clean_text):
    '''
    This function takes in a dataframe and the clean_text function
    to produce a new dataframe of words and word frequency rates.
    '''
    # creating a list of words for readmes and programming languages
    all_readme_words = clean_text(' '.join(df['readme_contents']))
    python_words = clean_text(' '.join(df[df['language'] == 'python']['readme_contents']))
    cplus_words = clean_text(' '.join(df[df['language'] == 'c++']['readme_contents']))
    html_words = clean_text(' '.join(df[df['language'] == 'html']['readme_contents']))
    other_words = clean_text(' '.join(df[df['language'] == 'other']['readme_contents']))
    # The value counts for the readme and programming languages' words
    readme_counts = pd.Series(all_readme_words).value_counts()
    python_counts = pd.Series(python_words).value_counts()
    cplus_counts = pd.Series(cplus_words).value_counts()
    html_counts = pd.Series(html_words).value_counts()
    other_counts = pd.Series(other_words).value_counts()
    # concatinating the readme and programming languages into one dataframe
    word_freq = pd.concat([readme_counts, python_counts, cplus_counts, html_counts, other_counts], axis=1)
    word_freq.columns = ['readme', 'python', 'cplus+', 'html', 'other']
    # eliminating the most and least frequent words to reveal a more accurate depiction of specific programming
    # languages and their respective top words
    word_freq = word_freq.loc[word_freq['readme'] <= 200]
    word_freq = word_freq.loc[word_freq['readme'] >= 25]
    # filling the nan values with zero and making the df columns integers versus floats
    word_freq.fillna(0, inplace=True)
    word_freq = word_freq.astype('int')
    return word_freq


def python_vis(word_freq):
    '''
    This function creates a bar plot of the most common words appearing in python.
    '''
    
    #Plot the most frequent python words and color by label
    word_freq.sort_values('python', ascending=False).head(10).plot.bar(figsize=(16, 9))
    plt.title('Most Common Words in Python')
    plt.ylabel('Count')
    plt.xlabel('Most Common Words')
    plt.xticks(rotation=45)
    return plt.show()

def c_plus_plus_vis(word_freq):
    '''
    This function creates a bar plot of the most common words appearing in C++.
    '''
    #Plot the most frequent C++ words and color by label
    word_freq.sort_values('cplus+', ascending=False).head(10).plot.bar(figsize=(16, 9))
    plt.title('Most Common Words in C++')
    plt.ylabel('Count')
    plt.xlabel('Most Common Words')
    plt.xticks(rotation=45)
    return plt.show()


#Plot the most frequent words and color by label
def html_vis(word_freq):
    '''
    This function creates a bar plot of the most common words appearing in C++.
    '''
    #Plot the most frequent HTML words and color by label
    word_freq.sort_values('html', ascending=False).head(10).plot.bar(figsize=(16, 9))
    plt.title('Most Common Words in HTML')
    plt.ylabel('Count')
    plt.xlabel('Most Common Words')
    plt.xticks(rotation=45)
    return plt.show() 

def other_vis(word_freq):
    '''
    This function creates a bar plot of the most common words
    appearing in other programming languages.
    '''
    #Plot the most frequent other words and color by label
    word_freq.sort_values('other', ascending=False).head(10).plot.bar(figsize=(16, 9))
    plt.title('Most Common Words in Other Languages')
    plt.ylabel('Count')
    plt.xlabel('Most Common Words')
    plt.xticks(rotation=45)
    return plt.show() 

def length_viz(df):
    '''
    This function generates a visualization for lengths
    of readmes by language; input should be the training set
    '''
    lengths = []
    for x in df['model']:
        temp = len(x)
        lengths.append(temp)
    df['lengths'] = lengths
    viz001 = df[df['lengths'] < 8000]
    sns.barplot(data = viz001, x = 'language', y = 'lengths')
    plt.title('ReadMe Overal Length by Language')
    plt.ylabel('Overal Length')
    plt.xlabel('Language Used')
    return plt.show()
