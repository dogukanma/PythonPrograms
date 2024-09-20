# LEGAL DISCLAIMER:
# This software is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this program. 
# By using this software, you agree to take full responsibility for your actions and ensure that your usage complies with applicable laws and 
# regulations. It is recommended to only use this tool on systems for which you have explicit permission.

import requests
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

try:
  userUrl = sys.argv[1]
except IndexError:
  print("Error")
  exit("Usage: python subdomainfinder.py your_url")

checkUrls = []

file = open("wordlist.txt").readlines()

def domain_splitter(url):
  domain = ""
  if ("https://" in url):
    if("www" in url):
      domain = url.split("www.")[1]
    else:
      domain = url.split("https://")[1]
  elif("www" in url):
    domain = url.split("www.")[1]
  else:
    domain = url
  return domain

def find_subdomain(url):
  domain = domain_splitter(url)
  for link in file:
    fullUrl = "https://" + link.strip() + "." + domain
    print(fullUrl)
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.2)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)

    try:
      response = session.get(fullUrl, timeout=4)
    except requests.exceptions.Timeout:
      continue
    except requests.exceptions.ConnectionError:
      continue

    if(200 <= response.status_code <= 299):
      print("Found subdomain --> " + fullUrl)
    elif(response.status_code > 400):
      continue
    else:
      checkUrls.append(fullUrl)

def print_check_urls():
  for check in checkUrls:
    print("Check: " + check)

find_subdomain(userUrl)
print_check_urls()