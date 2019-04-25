import requests
import mechanicalsoup
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from Authorization_script import Uca_authorize, Courses_list
import requests.utils, pickle
import requests
import logging
def Courses_links(Session):
    browser = mechanicalsoup.StatefulBrowser(Session)
    browser.open_relative('https://campusvirtual.uca.es/intranet/es/cursos/actuales/estudiante/')

    page = browser.get_current_page()


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

    with open('Session.txt', 'wb') as f:
        pickle.dump(Session,f)
    return links


def prepare(link):
    link=[i for i in link.split('?')]
    for i in link[1].split('='):
        link.append(i)
    #print(link)
    return link


def Get_camp_page(Session,link):

    link=prepare(link)

    id = {}
    id[link[2]]=link[3]

    browser = mechanicalsoup.StatefulBrowser(Session)
    browser.open_relative(link[0], params=id)
    browser.select_form()
    browser.submit_selected()
    browser.open_relative(link[0], params=id)
    page= browser.get_current_page()
    #browser.launch_browser()

    print(  browser.get_url())
    with open('Session.txt', 'wb') as f:
        pickle.dump(Session,f)
    return page


def Event_links(Session,page):
    entregas_links={}

    entregas_links['Name']=str(page.title.string)
    url = "https://av03-18-19.uca.es/moodle/theme/image.php/boostuca/assign/1553847905/icon"
    for i in page.find_all('img'):
        if url == str(i.get('src')):
            a = i.previous_element
            if a.get('href') != None and a.span != None:
                entregas_links[str(a.get('href'))]=str(a.span.contents[0])



    return entregas_links

def Event_parse(page):



s = requests.Session()
Uca_authorize(s,'u713474834','c240441')
with open('Session.txt', 'rb') as f:
    s = pickle.load(f)
#Courses_links(s)

f=open('courses_links.txt','r')
links = [line.strip() for line in f]
#print(links)
#print(links[0])
f.close()
with open('Session.txt', 'rb') as f:
    s = pickle.load(f)

page=Get_camp_page(s,str('https://av03-18-19.uca.es/moodle/mod/assign/view.php?id=84345'))
#for i in links:
#    page=Course_page(s,str(i))
#    print(Event_links(s,page))
table=page.find('table',attrs={'class':'generaltable'})
table_body = table.find('tbody')
j=table_body.find_all('td')
m=[a.text.strip() for a in j ]
print(m)
