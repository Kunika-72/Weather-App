#from logging.handlers import DEFAULT_HTTP_LOGGING_PORT
#from multiprocessing.connection import deliver_challenge
#from random import sample
import requests
from bs4 import BeautifulSoup

#taking input from user
#city = str(input("Enter city name"))

url = {
    "delhi":"https://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396",
    "mumbai": "https://www.accuweather.com/en/in/mumbai/204842/weather-forecast/204842",
    "Kolkata": "https://www.accuweather.com/en/in/kolkata/206690/weather-forecast/206690",
    "bangalore": "https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108"
}



def TemparatureFinder(url):
    
    header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept Lang":"en"
    }  
    r=requests.get(url,headers=header)
    soup=BeautifulSoup(r.text,"lxml")
    print(soup)
    #Temperature
    temp= soup.find("div",class_ = "temp")
    return temp

city = str(input())
if (city=='delhi'):
    temp = TemparatureFinder(url["delhi"])
elif (city== 'mumbai'):
    temp = TemparatureFinder(url["mumbai"])
elif (city== 'kolkata'):
    temp = TemparatureFinder(url["kolkata"])
elif (city== 'bangalore'):
    temp = TemparatureFinder(url["bangalore"])
else:
    print("Wrong input")






    


