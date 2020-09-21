# Sentiment Analyzer: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)


## Demo
Link: [https://moviereviewanalyzer.herokuapp.com/](https://moviereviewanalyzer.herokuapp.com/)

## Overview
This is a Django web app which predicts the sentiment for the given input.

## Installation
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
|── sentiAnalyzer
|   |── __init__py
|   |── asgi.py
|   |── settings.py
|   |── urls.py
|   |── wsgi.py
|── sentiAnalyzerApp
├── template
│   ├── home.html
├── Procfile
├── README.md
├── manage.py
├── requirements.txt
|── runtime.txt
```

## Technologies Used

   Django, Keras, Sklearn


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/vishal958/sentimentAnalyzer/issues) here by including your search query and the expected result

## Future Scope

* Use multiple Algorithms
* Front-End 
