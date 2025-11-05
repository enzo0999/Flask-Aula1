from flask import Flask

app = Flask(__name__) 

@app.route('/')
def index():
    return("hello")

@app.route('/info')
def info():
    return("Página info")

@app.route('/info')
def index():
    modulo = "flask" 
    aula = "1"
    return "<h1>modulo:{modulo}, Aula:{aula} </h1>"
