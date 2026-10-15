import asyncio
from ninjakiwi_api import fetch
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




#EXAMPLE CODE 
async def start():
    data = await fetch("BTD6", "races")
    if data is not None:
        raw = await data.get_raw_data()
        example = await data.get_data("id")
        print(f"Successfully fetched race data: {raw}")
        if example is not None:
            print(f"Successfully fetched race data: {example}")
    else:
        print("Failed to fetch race data.")




async def userInfo():
    

def main():
    asyncio.run(start())

if __name__ == "__main__":
    main()
