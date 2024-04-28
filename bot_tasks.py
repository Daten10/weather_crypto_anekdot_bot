import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
from pprint import pprint
'''получение значения крипты'''


def get_crypto_data():
    req = requests.get('https://yobit.net/api/3/ticker/ton_usd')
    response = req.json()
    # print(response)
    sell_price = response['ton_usd']['sell']
    return f'{datetime.now().strftime('Сегодняшняя дата %d-%m-%y\nВремя %H:%M')}\nSell TON price: {sell_price}💲'


def get_weather(city):
    load_dotenv()
    key = getenv('WEATHER_TOKEN')

    code_to_smile = {
        'Clear': "Ясно \U00002600",
        'Clouds': "Облачно \U00002601",
        'Rain': "Дождь \U00002614",
        'Drizzle': "Дождь \U00002614",
        'Thunderstorm': "Гроза \U000026A1",
        'Snow': "Снег \U0001F328",
        'Mist': "Туман \U0001F32B",
        'Fog': "Туман \U0001F32B"
    }

    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric')
        data = r.json()
        # pprint(data)

        city = data['name']
        temp = data['main']['temp']

        weather_desc = data['weather'][0]['main']
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = 'Посмотри сам, я хз'

        return f'Погода у нас в {city}\nТемпература на улице {temp}°\n{wd}\n'

    except Exception as ex:
        print(ex)
        print('ошибка')
        return ex
