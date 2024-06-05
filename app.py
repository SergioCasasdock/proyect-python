from flask import Flask
app = Flask(__name__)

@app.route('/getapplication')
def getapplication():
    return 'Running status K8s'

@app.route('/Sergiocasas')
def getWeatherOnline():
    return 'Running test sergio casas'