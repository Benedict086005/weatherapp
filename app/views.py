import urllib.parse
from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        city = urllib.parse.quote(city)
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=74b5f452478de70c47d48d94fcb71b83').read()
        list_of_data = json.loads(source)
        
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}

    return render(request, "app/index.html", data)

