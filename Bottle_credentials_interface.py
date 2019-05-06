from bottle import run, get, template, post, request
import Course_parsed

@get('/')
def form():
    return template('formular')


@post('/')
def processForm():
    userNameCampus = request.forms.get('userNameCampus')
    passWordCampus = request.forms.get('pwdCampus')
    userNameGoogle = request.forms.get('userNameGoogle')
    print('<p>'+ userNameCampus+ ' ' + passWordCampus+ userNameGoogle +'</p>')
    f=open('Uca_creds.txt','w')
    f.write(str(userNameCampus))
    f.write('\n')
    f.write(str(passWordCampus))
    f.write('\n')
    f.write(str(userNameGoogle))
    f.close()
    Course_parsed.get_campus()
    return '<p>'+ userNameCampus+ ' ' + passWordCampus+ ' ' + userNameGoogle +'</p>'


def webpage():
    run(host='127.0.0.1', port=3333)