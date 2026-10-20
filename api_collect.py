import json #reading the json output
import requests #usage of the API 
import os #for getting the OAK 
from dotenv import load_dotenv #OAK Token (not really that super private but good to get practice in anyway) - OAK = Open Access Key


#GOAL: Get information about my user profile  in BloonsTD6
#Want to get the following informatoin:
    #games played
    #how much monkey money have currently 
    #current XP, Rank, and Veteran XP, Veteran Rank
    #how many total trophies I ever earned NOTE: NOT AVIALABLE IN STANDARD GAME MUST USE API 
#what monkey names do I have NOTE: MAYBE NOT 
    #how many continues I used
#rouge legends stat - NOTE: MAYBE NOT 
#frontier stat  -NOTE: MAYBE NOT


load_dotenv()

oak = os.getenv("NINJAKIWI_OAK")

#make sure that the user actually has their oak correct
if (not oak):
    print("ERROR: OAK NOT FOUND")
    print("Make sure the OAK is in the .env file")
    exit()


#if here than we know there is at least an OAK token 
url = f"https://data.ninjakiwi.com/btd6/save/{oak}"


response = requests.get(url, timeout = 18) #arbitrary timeout
data = response.json() #puts the response into data var 


#check if response was successful 
if (not data.get("success")):
    print("ERROR: THERE WAS AN ERROR IN THE API")
    print("API ERROR:", data.get("error"))
    exit()


#here we now know the OAK existed and was valid
usersave = data["body"]


#get the features available and let user select which one to look at 
count = 0
for item in usersave.keys():
    print(count, "---",item)
    count += 1
options = list(usersave.keys()) #now options[0] is first value returned, options[1] is second, and so on 



wanted_stat = 0
while (wanted_stat != -1):
    #let the user get information about the stat they want
    wanted_stat = int(input("Enter the number associated with the stat you want, -1 to quit: "))



    #error handling if user tries being a troll or a mistake
    if wanted_stat >= 1 and wanted_stat <= len(options): #bounds checking 
        selected = options[wanted_stat]
        print(f"{selected}: {usersave[selected]}")




















