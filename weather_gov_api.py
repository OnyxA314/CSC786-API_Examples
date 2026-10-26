import json #reading the json output
import requests #usage of the API
#no key needed here 

#gotten below from: https://latitude.to/articles-by-country/us/united-states/30197/dakota-state-university
DSU_Lat = 44.00
DSU_Lon = -97.06

#NOTE: if making it nice actually allow user to type in address or select on map and SAFELY AND SECURELY use that info to get lat and long
    #I am not 100% sure if any open source or python packages let me do that 


#Step 1 - looking at the API this initial endpoint leads to a lot more links for finer details on specific weathers 
    #in order to get the actual weather and windspeed and whatnot we need to get the 'forcast' from 'properties'
        #NOTE: might be fun to play with forcastHourly

    #have to do this intermediate step as looking at the API myself there seems to be seemingly arbitrary numbering with what weather station we have. 
    #Theoretically can hardcode and skip this intermediate step but I want to have this code be generalizable
url = f"https://api.weather.gov/points/{DSU_Lat},{DSU_Lon}"
response = requests.get(url, timeout=15) #15 just seems to be standard 
response.raise_for_status()
 


if not response:
    print("LOCATION API ERROR")
    #print out error num
    exit()




#ask if user wants weekly forcast or hour-by-hour for 24 hours 
print("Do you want the forcast for the next week or a detailed hour-by-hour forcast for the next 24 hours")
wanted = int(input("Enter '1' for the weekly forcast, '2' for the detailed hour-by-hour forcast: "))


if wanted == 1:
    #Step 2 - get the actual forcast data from the intermediate step above when supplies the latitude and longitude
        #data is located under 'properties' titled 'forcast'
    forecast_url = response.json()["properties"]["forecast"] #woah this was a lot easier code than I thought :) 

    # Retrieve the actual forecast
    response = requests.get(forecast_url, timeout=15)
    response.raise_for_status()

    if not response:
        print("FORCAST API ERROR")
        #print out error num
        exit()


    periods = response.json()["properties"]["periods"]

    for period in periods:
        print(period["name"])
        print("Estimated Temperature: ", period["temperature"], period["temperatureUnit"])
        print("Chance of precipitation: ", period["probabilityOfPrecipitation"]["value"], "%")
        print("Estimate Wind Speed: ", period["windSpeed"], period["windDirection"])
        print("Overall Forcast: ", period["detailedForecast"])
        print()


elif wanted == 2:
    #HOURLY FORCAST
    print("\n\n")
    url = f"https://api.weather.gov/points/{DSU_Lat},{DSU_Lon}"
    response = requests.get(url, timeout=15) #15 just seems to be standard 
    response.raise_for_status()

    

    if not response:
        print("LOCATION API ERROR")
        #print out error num
        exit()


    Hourlyforecast_url = response.json()["properties"]["forecastHourly"] 

    response = requests.get(Hourlyforecast_url, timeout = 15)
    response.raise_for_status()

    if not response:
        print("HOULY FORCAST ERROR")
        #print error
        exit()


    periods = response.json()["properties"]["periods"][0:24] #PROBLEM: Python slicing, I was doing , instead of :

    #now we have next 24 hours, time to print
    for period in periods:
        print(period["startTime"], "to", period["endTime"], ":")
        print("Temperature: ", period["temperature"], period["temperatureUnit"])
        print("Chance of precipitation: ", period["probabilityOfPrecipitation"]["value"], "%") #I don't even know what the other values mean
        print("Wind speed: ", period["windSpeed"], "Direction: ", period["windDirection"])
        print("Overall forcast: ", period["shortForecast"])
        print("")

else:
    print("INVALID CHOICE")
