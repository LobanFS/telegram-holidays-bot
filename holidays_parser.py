from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_today_holidays():
    url = "https://kakoysegodnyaprazdnik.ru/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    holidays = []
    for holiday in soup.select('[itemprop="text"]'):
        holidays.append(holiday.get_text(strip=True))
    return holidays

