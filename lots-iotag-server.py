import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

app = Flask(__name__)
cors = CORS(app)

@app.route('/write',  methods=['POST'])
def writeToDocument():
    data_array = request.json
    arrayString = ''
    for item in data_array['apnt']:
        arrayString += "\n" + "Veiculo:" + item['vehicle'] + ",Tipo:" + item['type_ap'] + ",Lat:" + str(item['lat']) + ",Lng:" + str(item['lng']) + ",Time:" + str(item['timestamp'])

    
    f = open("apontamentos.txt", "a")
    f.write(arrayString)
    f.close()

    f = open("apontamentosPy.py", "a")
    f.write(arrayString)
    f.close()
    return jsonify({"write": "success"})

@app.route('/',  methods=['GET', 'POST', 'OPTIONS'])
def check():
    f = open("apontamentos.txt", "r")
    return jsonify({"answer": f.read()})

@app.route('/py',  methods=['GET', 'POST', 'OPTIONS'])
def checkPy():
    f = open("apontamentosPy.py", "r")
    return jsonify({"answer": f.read()})

@app.route('/erase-document-4679',  methods=['POST', 'OPTIONS'])
def erase():
    f = open('apontamentos.txt', 'w').close()
    return jsonify({"answer": 'apagado'})

@app.route('/erasePy',  methods=['GET', 'POST', 'OPTIONS'])
def erasePy():
    f = open('apontamentosPy.py', 'w').close()
    return jsonify({"answer": 'apagado'})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)