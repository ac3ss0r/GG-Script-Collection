import requests
from bs4 import BeautifulSoup
from requests.utils import quote
from os.path import join, exists
from os import makedirs
import re

""" Game Guardian script downloader made by github.com/ac3ss0r """

# prevent invalid filenames
def sanitize(name : str) -> str:
    return re.sub(r'[^\w\-_.() ]', '', name)

# get the page count for a search request
def count_pages(request : str) -> int:
    response = requests.get(f"https://gameguardian.net/forum/search/?&q={quote(request)}&search_and_or=or&sortby=relevancy")
    if response.status_code != 200:
        print(f"Get page count failed: {response.status_code}")
        return 0
    soup = BeautifulSoup(response.content, 'html.parser')
    count = soup.find('input', {'class': 'ipsField_fullWidth', 'type':'number'})
    if count: # no count field = 1 page
        return int(count.get("max"))
    return 1 

# fetch list of search results as urls
def fetch_page(request : str, page : int) -> list:
    downloads = []
    response = requests.get(f"https://gameguardian.net/forum/search/?&q={quote(request)}&page={page}&search_and_or=or&sortby=relevancy")
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return downloads
    soup = BeautifulSoup(response.content, 'html.parser')
    # both are URL's (posts & files)
    for url in soup.find_all('span', {'class': 'ipsContained ipsType_break'}):
        downloads.append(url.find('a').get('href'))
    for url in soup.find_all('span', {'class': 'ipsType_break ipsContained'}):
        downloads.append(url.find('a').get('href'))    
    return downloads
    
# fetch results from ALL pages
def fetch_all(request : str):
    urls = []
    pages = count_pages(request)
    print(f"{pages} pages to process. Fetching...")    
    for i in range(0, pages):
        parsed_urls = fetch_page(request, i)
        for url in parsed_urls:
            urls.append(url)
    return urls

# parse script download and download it
def download(url : str):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Download file for {url} failed")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('span', {'class':'ipsType_break ipsContained'}) 
    # detect post (different button View File)
    viewfile = soup.find('a', {'class':"ipsButton ipsButton_primary ipsButton_fullWidth ipsButton_small"})
    if viewfile and "View File" in viewfile.text:
        download(viewfile.get('href'))
        return
    # regular download button (File)
    file_url = soup.find('a', {'class': 'ipsButton ipsButton_fullWidth ipsButton_large ipsButton_important'})
    if not file_url or not name:
        print(f"Not a download. Skipping {url}")
        return
    name = name.text.strip().replace(" ", "_") + ".lua.txt"
    file_response = requests.get(file_url.get("href"), cookies=response.cookies)
    if file_response.status_code != 200:
        print(f"Failed to download the file {name}. ({file_response.status_code})")
        return
    if not exists("saved"):
        makedirs("saved")       
    with open(join("saved", sanitize(name)), 'wb') as file:
        file.write(file_response.content)
    print(f"Saved {url}...")
        
# fetch all pages and download
def download_all(prompt : str):
    urls = fetch_all(prompt)
    print(f"Fetched {len(urls)} downloads.")
    for url in urls:
        download(url)