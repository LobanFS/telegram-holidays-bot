from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_today_holidays():
    url = "https://kakoysegodnyaprazdnik.ru/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        driver.implicitly_wait(1)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        holidays = []
        for holiday in soup.select('[itemprop="text"]'):
            p1 = holiday.get_text(strip=True).find('(')
            p2 = holiday.get_text(strip=True).find(')')
            if p1 != -1 and p2 != -1:
                line = (holiday.get_text(strip=True)[:p1] + holiday.get_text(strip=True)[p2 + 1:])
            else:
                line = (holiday.get_text(strip=True))
            if line.find('памяти') == -1 and line.find('Именины') == -1:
                holidays.append(line)
        holidays.append("\nУра!🎉🎉🎉")
        return holidays
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        driver.quit()

