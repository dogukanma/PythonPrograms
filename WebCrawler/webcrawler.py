# LEGAL DISCLAIMER:
# This software is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this program. 
# By using this software, you agree to take full responsibility for your actions and ensure that your usage complies with applicable laws and 
# regulations. It is recommended to only use this tool on systems for which you have explicit permission.

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
social_media = ["facebook", "linkedin", "instagram", "twitter", "youtube", "x.com"]

def get_source(sourceURL):
  session = requests.Session()
  retry = Retry(connect=3, backoff_factor=0.2)
  adapter = HTTPAdapter(max_retries=retry)
  session.mount('https://', adapter)
  session.mount('http://', adapter)
  response = session.get(sourceURL)
  soup = BeautifulSoup(response.text, "html.parser")
  # print(soup.find_all('a'))
  return soup

def crawl(sourceURL):
  soup = get_source(sourceURL)
  for link in soup.find_all('a'):
    social_flag = False
    href = link.get('href')
    if(href and href not in found_links and "#" not in href):
      if(href.startswith("/")):
        href = userUrl + "/" + href 
      for social in social_media:
        if(social in href):
          social_flag = True
          break
      if(social_flag == True):
        continue
      found_links.append(href)
      print(href)
    crawl(link)

crawl(userUrl)

# def crawl(url):


# def crawl(url):
#   links = get_source(url)
#   for link in links.find_all('a'):
#     link = link.get('href')
#     if link:
#       part_link = link.split("#")
#       link = part_link[0]
#       if link not in found_links and target_url in link:
#         found_links.append(link)
#         print("Found URL --> " + link)
#         crawl(link)


# crawl(target_url)
