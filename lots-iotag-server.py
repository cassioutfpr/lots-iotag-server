import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto
import calendar;
import time;
import os

app = Flask(__name__)
cors = CORS(app)

@app.route('/write',  methods=['POST'])
def writeToDocument():
    data_array = request.json
    arrayString = ''
    for item in data_array['apnt']:
        arrayString += "\n" + "Veiculo:" + item['vehicle'] + ",Tipo:" + item['type_ap'] + ",Lat:" + str(item['lat']) + ",Lng:" + str(item['lng']) + ",Time:" + str(item['timestamp'])


    ts = calendar.timegm(time.gmtime())
    print(ts)
    conn = S3Connection(os.environ['AWS_ID'], os.environ['AWS_PASSWORD'])
    b = conn.get_bucket('apontamentos')
    k = Key(b)
    k.key = str(ts) + '.txt'
    k.set_contents_from_string(arrayString)

    f = open("apontamentos.txt", "a")
    f.write(arrayString)
    f.close()

    return jsonify({"write": "success"})

@app.route('/',  methods=['GET', 'POST', 'OPTIONS'])
def check():
    f = open("apontamentos.txt", "r")
    return jsonify({"answer": f.read()})


@app.route('/erase-document-4679',  methods=['POST', 'OPTIONS'])
def erase():
    f = open('apontamentos.txt', 'w').close()
    return jsonify({"answer": 'apagado'})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)