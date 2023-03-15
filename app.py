import requests

url = 'https://www.w3schools.com'


for i in range(10):
    x = requests.get(url)
    print(len( x.text))