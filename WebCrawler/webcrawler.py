# LEGAL DISCLAIMER:
# This software is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this program. 
# By using this software, you agree to take full responsibility for your actions and ensure that your usage complies with applicable laws and 
# regulations. It is recommended to only use this tool on systems for which you have explicit permission.

# This program doesn't work properly

# imports
import requests
import sys
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



try:
  userUrl = sys.argv[1]
except IndexError:
  print("Error")
  exit("Usage: python webcrawler.py your_url")

found_links = []
invalid_words = ["facebook", "linkedin", "instagram", "twitter", "youtube", "x.com", "javascript", "mailto", "tel:"]

def get_source(sourceURL):
  session = requests.Session()
  retry = Retry(connect=3, backoff_factor=0.2)
  adapter = HTTPAdapter(max_retries=retry)
  session.mount('https://', adapter)
  session.mount('http://', adapter)
  response = session.get(sourceURL)
  soup = BeautifulSoup(response.text, "html.parser")
  return soup

# Error handling on getting source will be added.
def crawl(sourceURL):
  soup = get_source(sourceURL)
  # print("check 0")
  if(soup.find_all('a') == None):
    print("Error on getting source.")
  for link in soup.find_all('a'):
    invalid_flag = False
    problem_href = ""
    # print("check 1")
    try:
      href = link.get('href')
      problem_href = href
      # print("check 2")
      if(href and href not in found_links and "#" not in href):
        if(href.startswith("/")):
          # print("check 3")
          if(href == "/"):
            # print("check 4")
            continue
          href = userUrl + href
        for word in invalid_words:
          if(word in href):
            invalid_flag = True
            # print("check 5")
            break
        if(invalid_flag == True):
          # print("check 6")
          continue
        found_links.append(href)
        print(href)
        # print("check 7")
        if(href not in found_links):
          crawl(href)
    except requests.exceptions.ConnectionError:
      print("Problem on: " + problem_href)
      continue


crawl(userUrl)