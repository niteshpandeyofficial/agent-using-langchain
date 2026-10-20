from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from dotenv import load_dotenv
import requests
import os
load_dotenv()

def search_tool():
    """This is the inbuilt tools used for searching any input from web app"""
    search_tool=DuckDuckGoSearchRun()
    return search_tool

@tool
def get_weather_data(city:str)-> str:
    """
    This function return the latest weather data from given city
    https://weatherstack.com/dashboard
    """
    url = f"https://api.weatherstack.com/current?access_key={os.getenv('WEATHER_API_KEY')}&query={city}"
    response=requests.get(url)
    result=response.json()
    return result

# final_result=get_weather_data.invoke({'city':'Mumbai'})
# print(final_result)