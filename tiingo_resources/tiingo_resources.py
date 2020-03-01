from urllib.parse import urljoin


class Tiingo(object):

	INTRADAY_HIST_FOREX = "tiingo/fx/{base_pair}/prices?startDate={from_date}&resampleFreq={freq}&token={token}"

	def __init__(self, env_var_token):
		self.host = "https://api.tiingo.com"
		self.token = env_var_token

	def intraday_historical_prices_resource(self, base_pair, start_date, freq='1day'):
		resource = Tiingo.INTRADAY_HIST_FOREX.format(base_pair=base_pair, from_date=start_date, freq=freq, token=self.token)
		return urljoin(self.host, resource)

