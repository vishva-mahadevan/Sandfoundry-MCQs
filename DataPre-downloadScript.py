from bs4 import BeautifulSoup
import html
import requests
import re
import json
url = 'https://www.sanfoundry.com/'
def questiontoCsv(link):
    data=requests.get(link)
    soup=BeautifulSoup(data.text,'html.parser')
    page_source=soup.findAll('p')
    text=page_source[1].text
    question = re.sub('adver.+|\n\s+[a-z].+|\n\t\n', '', text)
    question = re.sub('(\.)\n(\d)','\g<1>\n\n\g<2>', question)
    with open('CS_DS-AI.txt','a',errors="ignore") as file:
        file.write(question)
    # # print(question)
def courseStream_subject_topic(url):
    data=requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    pageheader=soup.select('div div h4')
    for i in range(0,len(pageheader)):
        page_source=soup.select('div article div table tr')
        topiclink=page_source[i].findAll('a')
        for j in range(0, len(topiclink)):
            link=topiclink[j]['href']
            questiontoCsv(str(link))
def courseStream_subject(url):
    data=requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    page_source=soup.select('tr td li a')
    for i in range(0,len(page_source)):
        link=page_source[i]
        courseStream_subject_topic(str(link['href']))
def courseStream(url):
    data=requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    page_source=soup.select('li a')
    for i in range(3,24):
        if i!=3 and i!=7:
            link=page_source[i]
            courseStream_subject(str(link['href']))
courseStream(url)