from django.shortcuts import render
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#For Scraping
import requests;
import bs4;



# Create your views here.

def index(request) :
    return render(request, 'webscrap/home.html')


def contact(request) :
    res = requests.get('https://stackoverflow.com/search?tab=newest&q=android%20features')  #Data from Stack Overflow

    soup = bs4.BeautifulSoup(res.text, 'lxml') #Building a lxml file from res.text

    #building the question and hyperlink arrays
    Count = 0
    ques = [None] * 10
    link = [None] * 10

    for i in soup.select('.question-hyperlink'):
        ques[Count] = i.text
        link[Count] = i.get('href')
        Count += 1
        if Count == 10:
            break

    return render(request, 'webscrap/basic.html', {'res': zip(link, ques)})
    #return render(request, 'webscrap/basic.html', {'ques' : [ques], 'link' : [link] })