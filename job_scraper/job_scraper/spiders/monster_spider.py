import requests
from bs4 import BeautifulSoup

language = input("Language to search jobs for or leave blank and press ENTER: ")
location = input("City OR state to search for jobs or leave blank and press ENTER: ").replace(' ', '-')

if language:

    #Language and location
    if location:
        URL = f'https://www.monster.com/jobs/search/?q={language}&where={location}&stpage=1&page=3'

    #Only language
    else:
        URL = f'https://www.monster.com/jobs/search/?q={language}&stpage=1&page=3'

#if only location
elif location:
    URL = f'https://www.monster.com/jobs/search/?where={location}&stpage=1&page=3'

#if nothing
else:
    URL = f'https://www.monster.ca/jobs/search/pagination/?q=full+stack+developer&where=Ottawa%2C+Ontario&isDynamicPage=true&isMKPagination=true&page=3'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
print(soup)
results = soup.find("div", {"class": "results-page container"})
job_elems = soup.find_all("div", {"class": "results-card"})


print("\n", end='')
print("*" * 75, "\n")
input("Search results loaded. \nPress ENTER to print results:")


#Return results of job search
print("Printing jobs:")
# this will print every job posting as text
for job_elem in job_elems:

    title_elem = job_elem.find('h2', class_='title', string=lambda text: f'{language}' in text.lower())
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    link = job_elem.find('a')

    #monster has a Section html element that DOESN"T have info, so without this,
    #it'll return an error with the print statements afterwards
    if None in (title_elem, company_elem, location_elem, link):
        continue

    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(f"{location_elem.text.strip()}")
    print(f"Apply here: {link['href']}\n")
    print("-" * 75,'\n' )