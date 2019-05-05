from bottle import run, get, template, post, request
import Course_parsed
import threading
import from_queue_to_drive
import Add_To_Calender

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
    threading.Thread(target=from_queue_to_drive.setup_queue_consumer()).start()
    threading.Thread(target=Add_To_Calender.process_event()).start()
    threading.Thread(target=Course_parsed.get_campus()).start()

    return '<p>'+ userNameCampus+ ' ' + passWordCampus+ ' ' + userNameGoogle +'</p>'


#if __name__ == '__main__':
def webpage():
    run()
webpage()