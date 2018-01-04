import urlopen
import json
from urllib.request import urlopen
#newsapi provides news paper api which are in the form of json objects
"""
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
"""
def times_of_india():
    try:
        jsonObj=urlopen('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=######')
        data=json.load(jsonObj)
        i=1
        print('''             ==============TIMES OF INDIA============'''
              + '\n')
        for item in data['articles']:
            print(str(i) + '. ' + item['title'] + '\n')
            print(item['description'] + '\n')
            i += 1
    except Exception as e:
        print(str(e))
def cnn():
    try:
        jsonObj=urlopen("https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=######")
        data=json.load(jsonObj)
        print("                ============CNN News==================")
        i=1
        for item in data['articles']:
            print(str(i)+'.'+item['title']+'\n'+item['description']+'\n')
            i+=1
    except Exception as e:
        print(str(e))
def google_india_news():
    try:
        jsonObj=urlopen('https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=######')
        data=json.load(jsonObj)
        i=1
        print('                   ==================Google India News============')
        for item in data['articles']:
            print(str(i)+'.'+item['title']+'\n'+item['description']+'\n')
            i+=1
    except Exception as e:
        print(str(e))
def talk_sport():
    try:
        jsonObj=urlopen('https://newsapi.org/v2/top-headlines?sources=talksport&apiKey=######')
        data=json.load(jsonObj)
        i=1
        print('                   ==================Talk Sport============')
        for item in data['articles']:
            print(str(i)+'.'+item['title']+'\n'+item['description']+'\n')
            i+=1
    except Exception as e:
        print(str(e))
def new_scientist():
    try:
        jsonObj=urlopen('https://newsapi.org/v2/top-headlines?sources=new-scientist&apiKey=######')
        data=json.load(jsonObj)
        i=1
        print('                   ==================New Scientist============')
        for item in data['articles']:
            print(str(i)+'.'+item['title']+'\n'+item['description']+'\n')
            i+=1
    except Exception as e:
        print(str(e))
