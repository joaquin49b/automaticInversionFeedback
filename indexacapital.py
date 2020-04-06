import requests

url = 'https://api.indexacapital.com/'

params = {
  "client_id": "123456789123456789a"
}
headers = {'Accept':'application/json'}
response = requests.post('https://sandbox-oba.revolut.com/register', data = params )
print(response.text)