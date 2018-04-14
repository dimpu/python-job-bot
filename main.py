from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from db import db, Job
from config import skillset,locations,site_url

def next_page(page):
    pages = page.find_all('span', attrs={'class':'pn'} )
    if(len(pages) > 0):
        lastPage = pages[len(pages) - 1]
        if 'Next' in lastPage.text:
            link = lastPage.parent.get('href')
            print(site_url + link)
            page = get(site_url + link)
            soup = BeautifulSoup(page.text, 'html.parser')
            save_job(soup)

def save_job(page):
    for result in page.find_all('div', attrs={'class':'result'}):
        job = result.find('a', attrs={'class':'turnstileLink'})
        title = job.text
        url = site_url + job.get('href')
        company = result.find('span', attrs={'class':'company'}).text
        location = result.find('span', attrs={'class':'location'}).text
        summary = result.find('span', attrs={'class':'summary'}).text
        Job.create(title=title,
        url=url,
        company = company,
        location = location,
        summary = summary,
        applied = False)
    next_page(page)

def init(q, l):
    url = site_url + '/jobs?q=' +q+ '&l=' + l
    page = get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    save_job(soup)

# init('React', 'New+York')

def main():
    for skill in skillset:
        for location in locations:
            # print(skill,location)
            init(skill, location)


main()