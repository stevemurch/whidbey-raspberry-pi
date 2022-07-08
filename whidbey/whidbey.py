# flask server to report voltage level
# to run:
# export FLASK_APP=voltageflask.py
# flask run --host=0.0.0.0
 
from gaugeread import get_tank_level 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_main_route():
    return "Hello world"

@app.route('/propane1')
def get_propane_level_1():
    tank_level = get_tank_level()
    result = {"val": tank_level}
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
