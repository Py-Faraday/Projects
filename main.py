import requests
from datetime import datetime
from config import API

code_to_smile = {
    'Clear': "Ясно \U00002600",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U00002614",
    "Drizzle": "Дождь \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U0001F32B"
}


def get_weather(city):
    try:
        a = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
        )
        data = a.json()
        sity = data['name']
        cur_weather = data['main']['temp']
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data['wind']['speed']
        sunrise_timepesmp = datetime.fromtimestamp(data["sys"]['sunrise'])
        sunset_timepesmp = datetime.fromtimestamp(data["sys"]['sunset'])
        length_of_the_day = sunset_timepesmp - sunrise_timepesmp

        weather_description = data['weather'][0]['main']

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что за погода там!"

        return f"""
            Дата: {datetime.now().strftime("%Y-%m-%d  %H:%M:%S")}
            Погода в городе: {sity}
            Температура: {cur_weather} °C {wd}
            Влажность: {humidity}
            Давление: {pressure} мм.рт.ст
            Скорость ветра: {wind}
            Восход: {sunrise_timepesmp}
            Продолжительность дня: {length_of_the_day}
            Закат: {sunset_timepesmp}
            """

    except Exception as ex:
        return "Введите корректный город!!!"
