# Hacktober NLP Project
------
# Project Description 

This project aims to predict the programming language that a Github repository will be using. This will be done by webscraping 130 ReadMes. Then using NLP skills to find which words are more likly to be used for each language.

------
# Project Goals
+ Find the most used words for each prgramming language and used that as our drivers 
+ Take the found drivers and develop a machine learning that can help predict the programming language
+ Make code reproducable

-----
# Data Dictionary


| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| repo | The repository obtained from Github| `object` |
| language| The main programming language used | `object` |
| readme_content | The contents included in the ReadMe file | `object` |
| lem | Readme contents that have been lemmatized | `object` |



------
# Initial Hypothesis

TBD

------
# My Plan of Action

+ Aquire data from Github website
  - Use webscraping to acquire the readme contents 
  
+ Prepare the acquired data
  - Download and turn github data into a json file
  - Bring in data into our jupyter notebook
  - Use pandas library
    - to clean data using regex
    - lemmatize our readme contents
    - replace null values with correct programming languages
  - Split our data into three parts 
    - `Train` which will have the largest amount of the data so we can use it to make our model
    - `Validate` which is used to make sure our model is the best it can before finally moving on
    - `Test` which is the final determinator to see if the model is good enough, the last part of modeling

Exploration
  
- Explore data in search of most frequent words used in readmes by programming languages
- Answer the following initial questions:
    - Are there any words that uniquely identify a programming language? 
    - What are the most common words in READMEs?
    - Does the length of the README vary by programming language?
    - Is there a numerical difference in bigrams by language?
- Use or make functions to help build our models 

Modeling

- Build models 
  - Create our object
  - fit the model to find the most useful model
  - Use the best model on the in-sample data
  - Use the best model on the out-of-sample data
  
Delivery
  
  - Visualze to help the audiance easily see the findings of the work that was done
  - Model to help predict the programming language that is being used
  
  ----
  # How to Reproduce the work
  
  - Clone this repo
  - Put data in the same file as the repo
  - Run the notebook
