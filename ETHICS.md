ETHICAL CONSIDERATIONS:
  Project 1: Ninja Kiwi API
    The OAK token is a privacy first approach in where developers are able to access general information about a user's account however this does not permit any tracking of personal informatoin (i.e. email, username, location) of a user rather a general profile for information access being made easier
    The information part of the OAK token can contain information from the following games:
      Bloons TD 6
      Bloon Blitz
      Bloons TD Battles 2

    There is not a listed rate limit for this API however the project respects that it still can cause issues if high rates are used and thus respects any timeout and undocumented limitations as well as minimizing the number of requests. 
    
  Project 2: Weather.gov API
    The Weather.gov API allows for fully free and near unlimited access to the usage of it's API. Though the exact latitude and longitude is required to get information about the forcast of a region this is only used to know what weather station to look up for in more accurate forcasts.
    There is a stated rate-limit that is undisclosed and this program respects any rate-limit imposed upon it by limiting the amount of requests to a single time once per program being ran.
    In order to respect the ethical guidelines there is a useragent header sent along with the requests being made that is strictly to prevent any abuse of the API. In order to ensure privacy while also respecting ethical considerations the header is a string of characters stating "786" which is vague enough to not have much meaning unless you know it's part of this class

