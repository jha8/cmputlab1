import requests

# References used: 
# curl manpage
# https://requests.readthedocs.io/en/master/ for python request library

# Q2
# print(requests.__version__)

# Curl 5)
# test = requests.get('http://www.google.com')
# print(test.status_code)

# Curl 10)
test = requests.get('https://raw.githubusercontent.com/jha8/cmputlab1/main/lab1.py')
print(test.text)

