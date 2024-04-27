from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                         '=submit&searchTextSrc=ft&searchTextText=%22Microsoft+.net%22&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text,'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    days = published_date.split()[1]
    if int(days) <= 2:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills_needed = job.find('span', class_='srp-skills').text.strip()
        print(f'''
        company: {company_name}
        skills: {skills_needed}
        posted before: {days} day/s
        ''')
        print('')
