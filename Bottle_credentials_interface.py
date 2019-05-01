from bottle import run, get, template, post, request


@get('/')
def form():
    return template('formular')


@post('/')
def processForm():
    userNameCampus = request.forms.get('userNameCampus')
    passWordCampus = request.forms.get('pwdCampus')
    userNameGoogle = request.forms.get('userNameGoogle')
    print('<p>'+ userNameCampus+ ' ' + passWordCampus+ userNameGoogle +'</p>')
    return '<p>'+ userNameCampus+ ' ' + passWordCampus+ userNameGoogle +'</p>'


if __name__ == '__main__':
    run()
