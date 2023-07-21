import requests
import fake_useragent
from bs4 import BeautifulSoup



# s = requests.Session()

# url = 'https://zno.testportal.com.ua/master/login'
# ua = fake_useragent.UserAgent().random

# header = {
#     'user-agent': ua
# }

# data = {
#   #  '_token':'LpYqx4OTukcpALlFINYUda0ciAiIVglZuqukH4Vk',
#     'master[CertNum]':'1234567',
#     'master[CertPIN]':'1234',
#     'master[CertYear]':'2023',
#     'master[captcha]':'58'
# }

# responce = s.post(url, data=data, headers=header).text
# profile_info = 'https://zno.testportal.com.ua/master'
# profile_responce = s.get(profile_info, headers=header).text
# #print(responce)

# cookies_dict = [
#     {"domain": key.domain, "name":key.name, "path": key.path, "value": key.value}
#     for key in s.cookies
# ]

# s2 = requests.Session()
# for cookies in cookies_dict:
#     s2.cookies.set(**cookies)

# resp = s2.get(profile_info, headers=header)
# print(resp.text)


with open('.data.txt') as file:
    login = ''.join(file.readlines()).strip().split('\n')
print(login)

#_token	"LpYqx4OTukcpALlFINYUda0ciAiIVglZuqukH4Vk"
#master[CertNum]	"1234567"
#master[CertPIN]	"1234"
#master[CertYear]	"2023"
#master[captcha]	"58"