pip and packages

pip is Python's package manager and installer

import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.status_code)
print(requests_bbc.content)










