from bottle import run, get, template, post, request

@get('/')
def form():
    return template('formular')

@post('/')
def processForm():
    userNameCampus = request.forms.get('userNameCampus')
    passWordCampus = request.forms.get('pwdCampus')
    return '<p>'+ userNameCampus+ ' ' + passWordCampus+'</p>'

if __name__ == '__main__':
    run()
