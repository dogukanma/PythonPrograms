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
  exit("Usage: python directoryfinder.py your_url")

checkUrls = []
file = open("wordlist.txt").readlines()

def print_check_urls():
  for check in checkUrls:
    print("Check: " + check)

def find_directories(url):
  if("https://" not in url and "http://" not in url):
    raise Exception("Invalid URL.")
  for line in file:
    word = line.strip()
    newUrl = url + "/" + word
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.2)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)

    try:
      response = session.get(newUrl, timeout=4)
    except requests.exceptions.Timeout:
      print("Timeout - Proceeding")
      continue
    except requests.exceptions.ConnectionError:
      print("Connection error - Proceeding")
      continue
    except requests.exceptions.ConnectTimeout:
      print("Unhandled timeout - Proceeding")
    except TimeoutError:
      print("Unhandled timeout - Proceeding")
    except KeyboardInterrupt:
      print_check_urls()
      exit()

    print(newUrl)
    if(200 <= response.status_code <= 299):
      print("Found URL --> " + newUrl)
    elif(response.status_code > 400):
      continue
    else:
      checkUrls.append(newUrl)

find_directories(userUrl)



# def find_directories(url):
#   with open("wordlist.txt", "r") as listFile:
#     for line in listFile:
#       word = line.strip()
#       testURL = url + "/" +  word
#       response = request_check(testURL)
#       if response:
#         print("Found directory --> " + testURL)
#         foundURLs.append(word)

# find_directories(targetURL)

# for word in foundURLs:
#   newURL = targetURL + "/" + word
#   find_directories(newURL)