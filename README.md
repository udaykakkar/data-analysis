# data-analysis

Instructions

- Go to the folder
- Run below command in the terminal
  command for venv: python3 -m venv venv
- Then activate venv with the following command in the termianl for mac
  source venv/bin/activate
- Run pip install scrapy
- Run scrapy startproject glassdoor

Open scrapy shell by using command in terminal scrapy shell

- Once the shell is open, use fetch command and add the url that you want to use.
  fetch('https://www.glassdoor.ca/Job/ottawa-software-developer-jobs-SRCH_IL.0,6_IC2286068_KO7,25.htm')

jobs = response.css('li.react-job-listing.css-wp148e.eigr9kq3')

city= jobs.css('span.pr-xxsm.css-1ndif2q.e1rrn5ka0::text').get()

job_age = jobs.css('div.d-flex.align-items-end.pl-std.css-mi55ob::text').get()

company_ratings = jobs.css('span.css-19pjha7.e1cjmv6j1::text').get()

title = jobs.css('a.jobLink.css-1rd3saf.eigr9kq2')

job_title = title.css('span::text').get()

name = jobs.css('a.css-l2wjgv.e1n63ojh0.jobLink')

company_title = name.css('span::text').get()

link = jobs.css('a.jobLink.css-1rd3saf.eigr9kq2').attrib['href']

job_link = 'www.glassdoor.ca'+link

To run a spider to check the results in terminal run scrapy crawl glassdoor (glassdoor is the spider name)

Run this command scrapy crawl glassdoor -O glassdoor.json to get json result
