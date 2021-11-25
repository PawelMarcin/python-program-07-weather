
from datetime import date
from datetime import timedelta
import requests

# ponizsze importy potrzebne do metody testowej get_api_forecast_from_file -
# odkomentowac importy oraz definicje metody get_api_forecast_from_file

# import json
# from classesAndFunctions.filehandling import FileHandling

class CheckWeather:
    def __init__(self, args, saved_forecast):
        self.args = args
        self.saved_forecast = saved_forecast
        self.forecast = {}
        self.api_forecast = {}

    def check_date(self):
        if not self.args[1]:
            self.args[1] = (date.today() + timedelta(1)).strftime('%Y-%m-%d')

    def check_saved_forecast(self):
        if self.saved_forecast.get(self.args[1]):
            self.forecast.update({self.args[1]: self.saved_forecast[self.args[1]]})

    def get_api_forecast(self):
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
        qstr = {"lat": "52.06931644938404", "lon": "19.48030183891317",
                "units": "metric", "lang": "pl"}
        headers = {
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
            'x-rapidapi-key': self.args[0]
        }
        response = requests.request("GET", url, headers=headers, params=qstr)
        self.api_forecast = response.json()

    # do celow testowych odkomentowac ponizsza metode oraz odpowiednie importy

    # def get_api_forecast_from_file(self):
    #     fff = FileHandling('pogoda.json')
    #     fff.open_json()
    #     self.api_forecast = fff.object

    def check_api_forecast(self):
        for day_forecast in self.api_forecast['data']:
            if day_forecast['valid_date'] == self.args[1]:
                self.forecast.update({self.args[1]: 'Będzie padać: ' +
                                   day_forecast['weather']['description'] + '.'
                                   if day_forecast['weather']['code']
                                      in range(300, 700)
                                   else 'Nie będzie padać.'})

    def add_to_saved_forecast(self):
        self.saved_forecast.update(self.forecast)

    def print_forecast(self):
        print()
        print(self.args[1], ' - ', self.forecast[self.args[1]]) if \
            self.forecast else print(self.args[1], ' - ', 'Nie wiem.')
        print()
        print('Koniec programu.')
