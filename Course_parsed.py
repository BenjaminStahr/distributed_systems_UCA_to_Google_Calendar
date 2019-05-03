import mechanicalsoup
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from Authorization_script import Uca_authorize, Courses_list
import requests.utils, pickle
import requests
import datetime
import send_event_to_queue
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
    #print(link)
    for i in link[1].split('='):
        link.append(i)

    return link


def Get_camp_page(Session,link):
    #print(link)
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

    return entregas_links, entregas_links['Name']

def Event_parse(s,link):
    page = Get_camp_page(s,link)


    table = page.find('table', attrs={'class': 'generaltable'})
    table_body = table.find('tbody')
    j = table_body.find_all('td')
    text='Tiempo restante'
    m=[]
    for a in j:
        if a.text.strip()==text:
            break
        else:
            m.append(a.text.strip())
    return m


def to_json(summary, description, start_date, end_date, user):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_date,
            'timeZone': 'Europe/Madrid',
        },
        'end': {
            'dateTime': end_date,
            'timeZone': 'Europe/Madrid',
        },
        'attendees': [
            {'email': user}
        ]
    }
    return event

def date_transform(a):

    b = a.split()
    # start_date = datetime.datetime(2019, 4, 25, 14, 20, 0, 0, tzinfo=None, fold=0).isoformat()
    year=int(b[5].split(',')[0])
    hours=int(b[6].split(":")[0])
    mins=int(b[6].split(":")[1])

    s = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abríl': 4,'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
         'septiembre': 9, 'octubre': 10,
         'noviembre': 11, 'diciembre': 12}
    month=int(s[b[3]])
    day=int(b[1])

    date=datetime.datetime(year,month,day,hours,mins,0,0, tzinfo=None, fold=0).isoformat()
    return date

def sendmessage(message):
    pass

def get_campus(Uca_login, Uca_password,email):
    s=requests.Session()
    events_list=list()
    s =Uca_authorize(s,Uca_login,Uca_password)
    lists=Courses_links(s)
    Courses=lists[0]
    s =lists[1]
    #print(Courses)
    for link in Courses:
        events=list()
        #print(link)
        Course_page=Get_camp_page(s,link)
        print(link)
        evl=Event_links(s,Course_page)
        ev=evl[0]
        evnm=evl[1]

        for j in ev.keys():
            if j!='Name':
                #print(j,ev[j])

                event=Event_parse(s,j)
                summary=evnm+' '+ev[j]
                start_date=date_transform(event[5])
                description=str(event[1]+' '+ event[3])
                end_date=start_date
                user=email
                message=to_json(summary, description, start_date, end_date, user)
                print(message)
                #send_event_to_queue.send_event(message)

        events_list.append(events)




    return events_list



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
email='evfim1234@gmail.com'
print(get_campus('u713474834','c240441',email))

