import os
import sys
import urllib.request
import ssl
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from sqlalchemy import create_engine


def Navermovie(moviename):
    client_id = "OKQPTGKiQf0V3yitzK6o"
    client_secret = "uIGSvzveCB"
    encText = urllib.parse.quote(moviename)
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    return response_body.decode('utf-8')

def Movierank():
    page = requests.get('https://movie.naver.com/movie/running/current.nhn')
    html = page.text
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all('dl', 'lst_dsc')

    movie_rank = []
    for temp in result:
        tt = temp.find('dt', 'tit')
        movie_rank.append(tt.find('a').text)

    pddata = pd.DataFrame(movie_rank)
    print(pddata)
    engine = create_engine('sqlite:///{}'.format('navermovie.db'))
    pddata.columns=['title']
    pddata.to_sql('rank', engine, if_exists='replace')


    return movie_rank
