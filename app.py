import requests

url = 'https://www.w3schools.com'
x = requests.get(url)

print(x.text)