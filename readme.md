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
 
 # Takeaways and Conclusion
 
 - Two of the top three words in python (pr and create) do not appear as top words in any of the other programming languages, along with software. 
 - None of the top words in C++ appeared as top words in any of the other programming languages and had the highest difference between these top words versus the three other programming languages. 
 - Only one of the top words words in HTML (branch) did not appear in the other progamming language. 
 - None of the top three programming languages appeared in the top ten of eachother. 
 - Only other had the same top words (source, file, and change) with python and mainly HTML. 
 - The top three words overall in READMEs were source, code, and td. Code did not appear in any of the top three, but source and td appeared in python, C++, and other, the top three coding languages.

# Recommendations

- Based on these takeaways it appears that the words below are most related to the respective programming language:
    - Python = pr, create, and software
    - C++ = td, im, hobby, and titlecode
    - HTML = branch
