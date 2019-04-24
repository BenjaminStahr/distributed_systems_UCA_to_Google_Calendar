import requests
import mechanicalsoup
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from Authorization_script import Uca_authorize, Courses_list
import requests.utils, pickle
import requests
import logging
def Courses_parse(Session):
    page=Courses_list(Session)

    #print(soup.find_all('a'))
    #print(page.find_all('href'))
    links=[]
    for link in page.find_all('a'):
        pat='https://av'
        l=str(link.get('href'))
        if pat in l: #find the links of the courses
            links.append(l)
        links=list(dict.fromkeys(links)) #remove the same links
    f=open('courses_links.txt','w')
    print(links)
    for link in links:
        f.write(link+'\n')
    f.close
    return links

def Events_parse(Session,link):

    browser = mechanicalsoup.StatefulBrowser(Session)
    #browser.open_relative('https://campusvirtual.uca.es/intranet/es/cursos/actuales/estudiante/')
    browser.open_relative(link)
    print(browser.get_url())
    browser.open_relative(link)
    page = browser.get_current_page()
    #print(page.find_all('a'))
    #browser.find_link('/')
    page=browser.get_current_page()
    browser.select_form('input[name="AuthState"]')
    browser.submit_selected()

    page = browser.get_current_page()
    print((page))
    print(page.find_all('input'))
    for lin in page.find_all('input'):
        a=[i for i in (str(lin.get('value'))).split(":")]
        print(a)
        #print((str(a[0])+":"+str(a[1])))
        print(a[0])




'''
#s = requests.Session()
#Uca_authorize(s,'u713474834','c240441')
with open('Session.txt', 'rb') as f:
    s = pickle.load(f)
#Courses_parse(s)

f=open('courses_links.txt','r')
links = [line.strip() for line in f]

f.close()

#Events_parse(s,str(links[1]))
'''