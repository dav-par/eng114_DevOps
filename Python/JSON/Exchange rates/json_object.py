import json

class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info['base']
        self.date = rates_info['date']
        self.rates = rates_info['rates']
        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)


rate_reader = RatesParser("exchange_rates.json")

print(rate_reader.gbp)
print(rate_reader.rates)