import requests
import bs4
from fake_useragent import UserAgent

obj = UserAgent()

header = {'user-agent': obj.chrome }

response = requests.get("https://papershub.co.tz/resources/", header)
# print(response.text)
# print(response.content)
# print(response.status_code)

soup = bs4.BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

for key,value in response.headers.items():
    print(f"{key} --> {value}")


#accessing tags 
# file_path = 'C:/Users/Admin/Desktop/web_scrap/index.html'
# with open(file_path, 'r') as f:
#     html_response = f.read()

# soup = bs4.BeautifulSoup(html_response, 'html.parser')
# print(soup.a.text)




