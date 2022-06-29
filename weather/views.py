from django.shortcuts import render
import requests
from datetime import datetime

API_KEY = 'b23164b6b608a3f5c35ca3deb487c738'

def get_weather_info(cityname: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}&units=metric'
    res = requests.get(url).json()

    return res

def index(request):

    if request.method == "POST":
        cityname = request.POST.get('city')

        data = get_weather_info(cityname)

        if data['cod'] == '404':
            error = 'City not found'
            return render(request, 'weather/index.html', {'error': error})
        else:
            params = {
                'city' : data['name'],
                'country' : data['sys']['country'],
                'date' : datetime.now(),
                'temperature' : data['main']['temp'],
                'pressure' : data['main']['pressure'],
                'humidity' : data['main']['humidity'],
                'wind' : data['wind']['speed'],
                'description' : data['weather'][0]['description'],
                'icon' : data['weather'][0]['icon'],
            }

            return render(request, 'weather/index.html', {'data': params})

    else:
        return render(request, 'weather/index.html')