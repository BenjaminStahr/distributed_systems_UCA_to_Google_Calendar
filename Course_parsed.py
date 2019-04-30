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


    links=[]
    for link in page.find_all('a'):
        pat='https://av'
        l=str(link.get('href'))
        if pat in l: #find the links of the courses
            links.append(l)
        links=list(dict.fromkeys(links)) #remove the same links
    f=open('courses_links.txt','w')
    #print(links)
    for link in links:
        f.write(link+'\n')
    f.close

    with open('Session.txt', 'wb') as f:
        pickle.dump(Session,f)
    return [links,Session]


def prepare(link):
    link=[i for i in link.split('?')]
    print(link)
    for i in link[1].split('='):
        link.append(i)

    return link


def Get_camp_page(Session,link):
    print(link)
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

    #print(browser.get_url())
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

def Event_parse(s,link):
    page = Get_camp_page(s,link)

    table = page.find('table', attrs={'class': 'generaltable'})
    table_body = table.find('tbody')
    j = table_body.find_all('td')
    m = [a.text.strip() for a in j]
    return m




def get_campus(Uca_login, Uca_password):
    s=requests.Session()
    events=list()
    s =Uca_authorize(s,Uca_login,Uca_password)
    lists=Courses_links(s)
    Courses=lists[0]
    s =lists[1]
    print(Courses)
    for link in Courses:
        print(link)
        Course_page=Get_camp_page(s,link)
        for j in Event_links(s,Course_page):

            events.append(Event_parse(s,j))




    return events



#s = requests.Session()
#Uca_authorize(s,'u713474834','c240441')
#with open('Session.txt', 'rb') as f:
#    s = pickle.load(f)
#Courses_links(s)

#f=open('courses_links.txt','r')
#links = [line.strip() for line in f]
#print(links)
#print(links[0])
#f.close()
#with open('Session.txt', 'rb') as f:
#    s = pickle.load(f)


#rint(m)
print(get_campus('u713474834','c240441'))

