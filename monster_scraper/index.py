from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def configure_driver():
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--incognito')
    driver = webdriver.Chrome(
        ChromeDriverManager().install())
    return driver


def getJobs(driver, job_position, location):
    driver.get(
        f'https://www.monster.ca/jobs/search?q={job_position}&where={location}&tm=1')
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'card-view-panel-full')))
    except TimeoutException:
        print('Time out!')
        return None

    soup = BeautifulSoup(driver.page_source, "lxml")
    for jobPost in soup.select('div.results-card'):
        for job in jobPost.select('div.title-company-location'):
            title_selector = 'h2.card-title'
            company_selector = 'h3[name="card_companyname"]'
            location_selector = 'span.card-job-location'
            print({
                'title': job.select_one(title_selector).text,
                'company': job.select_one(company_selector).text,
                'location': job.select_one(location_selector).text
            })


driver = configure_driver()
job_position = 'full stack developer'
location = 'Ottawa'
getJobs(driver, job_position, location)
driver.close()