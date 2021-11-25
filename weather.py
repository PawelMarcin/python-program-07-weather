"""
API:
    Weather (Watherbit.io) - prognoza szesnastodniowa

Dokumentacja API:
    https://www.weatherbit.io/api

Opis kodow uzywanych w API:
    https://www.weatherbit.io/api/codes

Klucz do API (miesieczny limit odpytan, bez podawania karty kredytowej):
    9cf0927b8msh41d6daf6ed703ddp1c08e0jsnf1da09660d90

Pliki z danymi:
    .\saved_forecast.json - plik produkcyjny, zawiera wynik wczesnejszych
        odpytan API w formacie uzywanym przez program
    .\pogoda.json - plik testowy, zawiera wynik odpytania API
        w formacie zwracanym przez API

"""
import sys

from classesAndFunctions.checkarguments import CheckArguments
from classesAndFunctions.checkweather import CheckWeather
from classesAndFunctions.filehandling import FileHandling

check_args = CheckArguments(sys.argv)

if check_args.check_arguments_count():
    check_args.return_arguments()

    saved_forecast = FileHandling('saved_forecast.json')
    saved_forecast.open_json()

    check_weather = CheckWeather(check_args.args, saved_forecast.object)
    check_weather.check_date()
    check_weather.check_saved_forecast()

    if not check_weather.forecast:
        # check_weather.get_api_forecast - metoda "produkcyjna"
        # check_weather.get_api_forecast_from_file - metoda tetowa, wymaga
        #   odkomentowania w pliku checkweather.py

        check_weather.get_api_forecast()
        # check_weather.get_api_forecast_from_file()
        check_weather.check_api_forecast()
        if check_weather.forecast:
            check_weather.add_to_saved_forecast()
            saved_forecast.save_json()

    check_weather.print_forecast()
