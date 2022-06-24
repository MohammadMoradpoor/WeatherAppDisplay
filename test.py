from bs4 import BeautifulSoup
import requests

city = 'tehran'
value = 'celsiuc'

address = """https://www.google.com/search?q={}+weather+{}&oq={}+weather+{}&aqs=chrome..69i57j0i13j0i8i13i30j0i390l4.14288j1j7&client=ubuntu&sourceid=chrome&ie=UTF-8""".format(city, value, city, value)
source = requests.get(address)
soup = BeautifulSoup(source.content, 'html.parser')

cityName = soup.find('span', class_='BNeawe tAd8D AP7Wnd')
date = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
degree = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
print("the weather in {} on {} is {}".format(cityName.text, date.text, degree.text))