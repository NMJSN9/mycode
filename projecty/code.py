#!/usr/bin/python3
""" Daily Horoscope | Author 
   Credit: """
import requests

url = "https://daily-horoscope3.p.rapidapi.com/api/1.0/get_daily_horoscope.php"

payload = "sign=ARIES&date=2022-10-27&api_key=4deeabbd6fmshd1e696851295694p15d9d7jsnf08ec58ea134&timezone=8"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "4deeabbd6fmshd1e696851295694p15d9d7jsnf08ec58ea134",
	"X-RapidAPI-Host": "daily-horoscope3.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
