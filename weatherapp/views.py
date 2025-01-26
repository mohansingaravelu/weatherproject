from django.shortcuts import render
from decouple import config
import requests
import datetime


# Create your views here.



def home(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Chennai'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config('API_KEY')}"
    parameter = {'units': 'metric'} 
    data = requests.get(url,parameter).json()
    description = data['weather'][0]['description']
    city_name = data['name']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.datetime.now()

    
    return render(request, 'home.html', {'description': description, 'city_name': city_name, 
                                         'icon': icon, 'temp': temp, 'day': day}) 