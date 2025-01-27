import re
import requests
from bs4 import BeautifulSoup

def get_today_holidays():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        url = "https://my-calend.ru/holidays"
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.content, 'html.parser')
        holidays = []
        for holiday in soup.select('ul.holidays-items li'):
            line = holiday.get_text(strip=True)
            line = re.sub(r'\d+$', '', line)
            holidays.append("✨" + line)
        holidays.append("Ура!🎉🎉🎉")
        return holidays
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

