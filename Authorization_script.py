import requests
import mechanicalsoup
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import requests.utils, pickle

import requests.utils, pickle
def Uca_authorize(Session,Uca_login,Uca_password):
    url = 'https://campusvirtual.uca.es/es/intranet/login'
    browser = mechanicalsoup.StatefulBrowser(Session)
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

    page_to_parse = browser.get_current_page()
    return page_to_parse
