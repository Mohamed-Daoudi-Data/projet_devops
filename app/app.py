from bottle import route, run

@route('/')
def home():
    return 'Bienvenue sur notre application web simple avec Bottle!'

if __name__ == '__main__':
    run(host='0.0.0.0', port=5000, debug=True)
