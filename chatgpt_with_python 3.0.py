import requests
import parameter as parm
import argparse


api_endpoint = parm.OPENAI_API_ENDPOINT
api_key = parm.OPENAI_API_KEY
args = input("Enter your program need ")
http_request_header = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+api_key}
request_data = {
  "model": "text-davinci-003",
  "prompt": f"Write a python programe to {args}",
  "max_tokens": 150,
  "temperature": 0.5}
response = requests.post(api_endpoint, headers=http_request_header, json=request_data)
if response.status_code == 200:
    print(response.json()["choices"][0]["text"])
else:
    print(f"Error in Post method {response.status_code}")
