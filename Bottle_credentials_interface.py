from bottle import run, route, template

@route('/')
def index():
    return template('formular')

if __name__ == '__main__':
    run()
