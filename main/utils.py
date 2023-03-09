from newsapi import NewsApiClient
import os
import requests


NEWSAPI_KEY = "527b22e84e7e41108f5459472f473b18"

class News():

    newsapi = NewsApiClient(api_key=NEWSAPI_KEY) #os.getenv("NEWSAPI_KEY")
    
    def getSources(self, newsapi):
        return newsapi.get_sources()

    def topheadlines(self, newsapi, sources, query):
        # /v2/top-headlines
        top_headlines = newsapi.get_top_headlines(q=query,
                                          sources=sources,
                                          category='business',
                                          language='en',
                                          country='ng')
        return 


class Weather:
    def hourly(longitude, latitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,apparent_temperature,precipitation,rain,weathercode"
        response = requests.request("GET", url)
        return response.json(), response.status_code

    def daily(longitude, latitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,rain_sum,precipitation_hours"
        response = requests.request("GET", url)
        return response.json(), response.status_code
