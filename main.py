import requests
from bs4 import BeautifulSoup
import schedule
import time
# web scrape resource to fetch current info from a website
r = requests.get('https://weather.com/weather/today')
soup = BeautifulSoup(r.text, 'html.parser')
today_temp = soup.select('.today_nowcard-temp > span ')
current_temp = today_temp[0].contents[0]

# fuction to get current weather in montgomery AL


def montgomery_al_current_temp():
    print(f'The current Temp in Montgomery Al is {current_temp} degrees. ')
    # if statement to notify if you should turn on your heat or air
    if current_temp >= "77":
        print("Time to cut the are on!!!")
    elif current_temp <= "60":
        print('Might need to cut the heater on!!')
    else:
        print('This is perfect Weather')


schedule.every(30).seconds.do(montgomery_al_current_temp)
montgomery_al_current_temp()

while 1:
    schedule.run_pending()
    time.sleep(1)

# print(r.status_code)
