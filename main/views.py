from django.shortcuts import render 

#import json to load json data to python dictionary
import json

#urlib.request to make a request to api
import urllib.request

# Create your views here.

def index(request):
    if request.method=='POST':
        city = request.POST['city']
        #https://openweathermap.org/api ---> to get the api key
        
        # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'api_id').read()
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=*****************').read()

        #converting json data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data= {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data={}
    return render(request, "main/index.html", data)