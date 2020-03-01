from flask import Flask, jsonify, request
import requests
import os

from tiingo_resources.tiingo_resources import Tiingo

api_token = os.getenv('TIINGO_KEY')

headers = {
	'Content-Type': 'application/json',
}

app = Flask(__name__)

@app.route('/fxticker/<string:basepair>&<string:date>&<string:freq>')
def get_fx(basepair, date, freq):
	"""
	e.g. call
	http://127.0.0.1:5000/fxticker/audusd&2019-01-01&1day
	"""

	tiingo = Tiingo(api_token)
	req = tiingo.intraday_historical_prices_resource(basepair, date, freq)
	res = requests.get(req, headers)
	print(req)
	status = res.status_code
	return jsonify({'results': res.json()}) #jsonify({'status': status})

app.run(port=5000)	

