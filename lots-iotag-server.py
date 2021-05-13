import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

app = Flask(__name__)
cors = CORS(app)

@app.route('/',  methods=['GET', 'POST'])
def nao_entre_em_panico():
    print(request.data)
    print('ioa')
    app.logger.warning('testing warning log')
    data = request.json
    f = open("apontamentos.txt", "a")
    f.write("\n" + "Tipo: " + data['ap_type'] + ", Lat: " + str(data['lat']) + ", Lng: " + str(data['lng']))
    f.close()
    return jsonify({"42": "a resposta para a vida, ouniverso e tudo mais"})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)