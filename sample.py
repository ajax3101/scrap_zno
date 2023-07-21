import requests
from bs4 import BeautifulSoup
import time
headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

data = {'authenticity_token':'',
    'CertNum':'', # Номер
    'CertPIN':'', # Пин
    'CertYear':'2023',
    'captcha':'captcha'
    }

url = 'https://zno.testportal.com.ua/master/login'

session = requests.Session() # Сессия

def get_token():# Метод, для получения токена
  response = session.post(url,headers=headers)
  soup = BeautifulSoup(response.text,"html.parser")
  token = soup.find('input',{'name':'authenticity_token'}).get('value')
  return token # Возвращает токен


def auth(): # Метод, для авторизации
  response = session.post(url,headers=headers,data=data)
  return response.text

data['authenticity_token'] = get_token() # Вызывает метод для получения токена, и результат заносим в словарь

time.sleep(20) # Пауза 20 сек :)
html = auth() # Авторизируемся. В html будет наш ответ после авторизации

if 'Log Out' in html: # Если строка 'Log Out' есть в html, значит авторизация прошла успешно
  print('Login OK!')
else:
  print('Login Error!')