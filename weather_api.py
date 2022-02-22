import requests #install using pip install requests
import os #to access the environment variable

#store the api_key in the user environment variable for security purpose
user_api = os.environ["weather_key"]  


print("..........Current Weather Status of New Zealand's four major airports..........\n")
location = ["AKL","CHC","WLG","ZQN"]
for i in location:

    #get the api_link from https://www.weatherapi.com/api-explorer.aspx#current
    api_link = "http://api.weatherapi.com/v1/current.json?key="+user_api+"&q="+i+"&aqi=yes"
    requested_url = requests.get(api_link)
    api_data = requested_url.json() #store the response from api_link in json format

    if requested_url.status_code != 200:   #check if connection to api is successful or not
        print(requested_url.text)          
    else:
            print("Airport Name: ",api_data['location']['name'])
            print("Region: ",api_data['location']['region'])
            print("Temperature: ",api_data['current']['temp_c'],'deg C')
            print("Weather Condition: ",api_data['current']['condition']['text'])
            print("Wind: ",api_data['current']['wind_kph'],'kph' '\n')
            







