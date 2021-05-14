from selenium import webdriver
from selenium.webdriver.common.by import By

import time
DRIVER_PATH = '/usr/bin/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.monster.ca/jobs/search/pagination/?q=full+stack+developer&where=Ottawa%2C+Ontario&isDynamicPage=true&isMKPagination=true&page=3')


time.sleep(2);

'''
file = open('Failed.py', 'w')
file.write(driver.page_source)
file.close()
'''
Element = driver.find_element_by_xpath("//*[@id=\"card-view-panel-full\"]/div/div[1]")
print(Element.get_attribute('innerHTML'))

file = open('Failed.py', 'w')
file.write(Element.get_attribute('innerHTML'))
file.close()