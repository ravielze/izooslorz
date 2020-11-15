# izooslorz
> `Tugas Besar Algeo II` is a simple seach engine. Using cosine similarity, this project can find you similar document. It's also provided to add new documents from local files, link (web scrapping), and manual input.

## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Inspiration](#inspiration)

## General info
A Search Engine using TF and IDF with Cosine Similarity.

## Requirements
To run this on your pc, you need:
* Python 3.7.X (Recommended 3.7.9)
* NPM and Node.js

## Technologies
* Flask
* Textract - Extract Content from All Document Extension
* NLTK - Stemming & Stopword for English
* Sastrawi - Stemming & Stopword for Bahasa Indonesia
* React
* @material-ui

## Setup
First, you need to install pip :
1. Download "get-pip.py" file on pypa.io
2. Run cmd as Administrator
3. Type in the following command :
```$ python get-pip.py```

Second, you need to install the dependencies. All the required dependencies can be found in the folder server by the name "requirements.txt" using ```$ pip -r requirements.txt```

Third, you need NPM and node to start the development server for the client side/front end.

Fourth, you need to install the dependencies to start the client server. The dependencies are as following :
1. Go to client directories, @material-ui/core, which can be installed by going to the directory of this project on cmd ran as administrator and by typing in
```$ npm install @material-ui/core```
2. @material-ui/icons, which can be installed by going to the directory of this project on cmd ran as administrator and by typing in
```$ npm install @material-ui/icons```
3. axios, which can be installed by going to the directory of this project on cmd ran as administrator and by typing in
```$ npm install axios```
4. react-router-dom, which can be installed by going to the directory of this project on cmd ran as administrator and by typing in
```$ npm install --save react-router-dom```
5. Run ```$ npm run start```
5. Go to server directories and run backend server using ```$ py app.py```

## Features
List of features ready and TODOs for future development
* Ready: Web scraping by posting an url to the server
* Ready: Search documents (pptx, docx, doc, pdf, txt, html, json) by getting a keyword to the server
* Ready: Bahasa Indonesia and English supported
* TODO: Change CSV database to SQL database such as Postgresql or mysql
* TODO: Improve code efficiency
* TODO: Improve frontend UI/UX

## Inspiration
Project inspired by google, based on cosine similarity theory.