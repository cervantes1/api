from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

@app.route("/")
def hello():
    return "<h1>Property Testing</h1><br><h3>/properties</h3><br><h3>/properties/{record}</h3>"

@app.route('/properties/<record>', methods=['GET'])
def get_records(record):
    with open('../flask/Data/data.json') as f:
        data = json.load(f)

    if record in data:
        return {record : data[record]}, 200

class properties(Resource):
    def get(self):
        with open('../flask/Data/data.json') as f:
            data = json.load(f)

        return {'Properties': data}, 200


api.add_resource(properties, '/properties')

if __name__ == "__main__": 
    app.run()  

    print("Testing")
 
