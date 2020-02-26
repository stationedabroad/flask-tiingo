from flask import Flask, jsonify
import requests
import os

key = os.getenv('TIINGO_KEY')
tiingo_url = os.getenv('TIINGO_URL')
headers = {
	'Content-Type': 'application/json',
}

app = Flask(__name__)

@app.route('/fxticker/<string:basepair>')
def get_fx(basepair):
	req = tiingo_url.format(basepair, key)
	res = requests.get(req, headers)
	results = res.json()
	print(req, results)
	return jsonify(results)

app.run(port=5000)	

