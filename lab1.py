import requests
# Q2
# print(requests.__version__)

# Curl 5)
test = requests.get('http://www.google.com')
print(test.status_code)

