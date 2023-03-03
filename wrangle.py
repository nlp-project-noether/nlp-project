import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Union, cast
from bs4 import BeautifulSoup
import requests
import nltk
import unicodedata
import re


def get_readme():

    '''
    This function returns the json file if it already exists in our local file. If not, it
    will create the file. 
    '''

    filename = "data.json"

    if os.path.isfile(filename):
        return pd.read_json(filename)
    
    else:
        hrefs = [] 
        for p in range(1,14):
            url = f'https://github.com/search?p={p}&q=Hacktoberfest&type=Repositories'
            response = requests.get(url)
            soup = BeautifulSoup(response.text,'html.parser')
            links = soup.find_all("a", {"class": "v-align-middle"})
            links = [l['href'] for l in links]
            hrefs.append(links)
            time.sleep(15)
        flat_list = [item for sublist in hrefs for item in sublist]  
        return flat_list


REPOS: flat_list

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)


def clean_text(text, extra_stopwords=[]):

    '''
    This function takes in the words and cleans it, and returns the words that have been 
    lemmatized.
    '''

    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') + extra_stopwords
    clean_text = (unicodedata.normalize('NFKD', text)
                   .encode('ascii', 'ignore')
                   .decode('utf-8', 'ignore')
                   .lower())
    words = re.sub(r'[^\w\s___]', '', clean_text).split()
    words = re.sub(r'_', '',' '.join(words)).split(' ')
    words = [w for w in words if len(w)<25]
    return [wnl.lemmatize(word) for word in words if word not in stopwords]

def jupy_replace(df):
    
    '''
    This function goes through the `language` column, and replaces it with the 
    second most used language from the repo. 
    '''
    
    new_lang = ['C++', 'C++','C++','python','python','python', 'python', 'python',
                 'python', 'python', 'python', 'python', 'python', 'C++',
                 'python', 'C++', 'python', 'python', 'python', 'HTML', 'python',
                 'Javascript']
    repo_mod = pd.DataFrame(df[df['language']== 'Jupyter Notebook']['repo'])
    repo_mod['new_lang'] = new_lang
    for x in repo_mod.index:
        df.loc[x, 'language'] = repo_mod.loc[x, 'new_lang']
    return df


def clean_lang(df):
    '''
    This function gets the top three languages used. If the language is not in the top three,
    it will replace the language with `other`.
    '''
    df.language = df.language.str.lower()
    invalid = list(set(list(df.language.value_counts().index))-set(['c++', 'python', 'html']))
    invalid_index = df[df.language.isin(invalid)]['language'].index
    df.loc[invalid_index,'language']='other'
    return df