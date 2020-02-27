from flask import Flask, jsonify
import requests
import os

from tiingo_resources import tiingo_resources

api_token = os.getenv('TIINGO_KEY')

headers = {
	'Content-Type': 'application/json',
}

app = Flask(__name__)

@app.route('/fxticker/<string:basepair>&<string:date>&<string:freq>')
def get_fx(basepair, date, freq):
	tiingo = Tiingo(api_token)
	req = tiingo.intraday_historical_prices_resource(basepair, date, freq)
	res = requests.get(req, headers)
	# results = res.json()
	print(req)
	return results.json()

app.run(port=5000)	

