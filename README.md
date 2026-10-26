This repository contains 2 projects:
  1) project using the ninkakiwi API for usage of an API that requests a private access token
  2) Project using the weather.gov API for usage of a more gneral API that is highly useful without the need for a private access token

Project 1)
  The NinjaKiwi API retrives information about a person's bloons TD6 account - requiring the user to supply their own access token called an OAK (Open Access Key)
  The information the user can select 52 option related to their personal Bloons TD6 account/play history including many information that is typically not available through other usage (i.e. through the in game information itself) and only available through this API
  In order to run this file the following python packages need to be installed:
    'json'
    'requests'
    'dotenv'
    'os'
  All of these can be found in the requirements.txt file 
  
  The user also need to create their own .env file formated in the following way:
    NINJAKIWI_OAK=*token*
  an example of how the .env file should be setup and created can be found in the _env_example file 

Project 2)
  The weather.gov API retrives weather information for Dakota State University. 
  It lets the user select between 2 options:
    A: A general weeklong forcast including overall temperature, windspeed and direction, chance of precipitation, and a general description of the weather for each 12 hour period
    B: An indepth hour-by-hour forcast for the next 24 hours including temperature, windspeed and direction, chance of precipitation, and a short description of the weather every hour 

  In order to run this file the following python packages need to be installed:
    'json'
    'requests'
  with these files being found in the requirements.txt file. 
