# Must run this test in `pipenv shell`
import requests

url = "http://localhost:9696/problem4"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
response = requests.post(url, json=client).json()

print(response)
# returns a probability of 0.928