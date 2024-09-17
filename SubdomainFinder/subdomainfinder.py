import requests
import sys

try:
  urlParam = sys.argv[2]
except IndexError:
  print("Error")
  exit("Usage: python subdomainfinder.py your_url")

checkUrls = []

file = open("wordlist.txt").readlines

def find_subdomain():
  for link in file:
    fullUrl = "https://" + link + urlParam.split("www")[1]
    response = requests.get(fullUrl)
    if(response.status_code >= 200 or response.status_code <= 299):
      print("Found subdomain --> " + fullUrl)
    elif(response.status_code > 400):
      continue
    else:
      checkUrls.append(fullUrl)

def print_check_urls():
  for check in checkUrls:
    print("Check: " + check)