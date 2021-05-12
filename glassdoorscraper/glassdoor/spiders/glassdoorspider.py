import scrapy

class GlassdoorSpider(scrapy.Spider):
  name = 'glassdoor'
  start_urls = ['https://www.glassdoor.ca/Job/ottawa-software-developer-jobs-SRCH_IL.0,6_IC2286068_KO7,25.htm']

  def parse(self, response):
    for jobs in response.css('li.react-job-listing.css-wp148e.eigr9kq3'):
      yield {
        'job_title': jobs.css('a.jobLink.css-1rd3saf.eigr9kq2').css('span::text').get(),
        'company_name': jobs.css('a.css-l2wjgv.e1n63ojh0.jobLink').css('span::text').get(),
        'job_link':'www.glassdoor.ca'+ jobs.css('a.jobLink.css-1rd3saf.eigr9kq2').attrib['href'],
        'company_ratings': jobs.css('span.css-19pjha7.e1cjmv6j1::text').get(),
        'city':jobs.css('span.pr-xxsm.css-1ndif2q.e1rrn5ka0::text').get(),
        'job_age':jobs.css('div.d-flex.align-items-end.pl-std.css-mi55ob::text').get(),
      }
    next_page = 'www.glassdoor.ca'+ response.css('li.css-1yshuyv.e1gri00l3').css('a').attrib['href'][0:68]
    if next_page is not None:
      yield response.follow(next_page, callback=self.parse)


