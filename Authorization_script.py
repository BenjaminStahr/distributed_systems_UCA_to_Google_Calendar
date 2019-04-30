import requests
import mechanicalsoup
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import requests.utils, pickle

import requests.utils, pickle
def Uca_authorize(Session,Uca_login,Uca_password):
    url = 'https://campusvirtual.uca.es/es/intranet/login'
    browser = mechanicalsoup.StatefulBrowser(Session)
    # browser.session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'})
    browser.open(url)
    url = 'https://campusvirtual.uca.es/es/intranet/login'

    with open('Session.txt', 'wb') as f:
        pickle.dump(Session,f)

    browser.select_form()
    browser["username"] = Uca_login
    browser["password"] = Uca_password
    browser.submit_selected()  # Then there were some troubles with redirecting to another webpage
    # which supports only a few types of action
    # after some attempts the solution was found:
    browser.select_form()
    browser.submit_selected()
    with open('Session.txt', 'wb') as f:
        pickle.dump(Session,f)
    return Session


def Courses_list(Session):
    browser = mechanicalsoup.StatefulBrowser(Session)
    browser.open_relative('https://campusvirtual.uca.es/intranet/es/cursos/actuales/estudiante/')

    page_to_parse = browser.get_current_page()  #
    #print(page_to_parse)  # It's a webpage with our courses. To parse this web page will be the second step

    return page_to_parse



#ss = requests.Session()

#Uca_authorize(s,'u713474834','c240441')
#with open('Session.txt', 'rb') as f:
#    s = pickle.load(f)
#print(Courses_list(s))