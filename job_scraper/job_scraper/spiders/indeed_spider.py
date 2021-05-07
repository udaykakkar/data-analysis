
from __future__ import unicode_literals
import scrapy
from job_scraper.items import JobScraperItem
from scrapy.loader import ItemLoader

class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['ca.indeed.com']

    def start_requests(self):
        job = "full stack developer"
        location = "ottawa"

        for radius in range(25, 100, 10):
            start_url = f'https://ca.indeed.com/jobs?q={job}&l={location}&radius={radius}'
            yield scrapy.Request(start_url, self.parse)

    def parse(self, response):
        for job in response.css('div.jobsearch-SerpJobCard'):
            l = ItemLoader(item = JobScraperItem(), selector = job)
            l.add_css('title', 'h2.title a::attr(title)')
            l.add_css('company', 'div.sjcl div span.company')
            l.add_css(
                'rating', 'div.sjcl div span.ratingsDisplay a span.ratingsContent')
            l.add_css('location', 'div.recJobLoc::attr(data-rc-loc)')
            l.add_css('salary', 'span.salaryText')
            l.add_css('description', 'div.summary ul li')
            yield l.load_item()

        next_page_link = response.xpath(
            '//ul[@class=pagination-list]/li/a/@href/text()').getall()
        next_page = response.xpath(
            '//ul[@class=pagination-list]/li/a/@aria-label/text()').getall()

        if next_page:
            if next_page[-1].lower() == "next":
                yield response.follow(url='https://ca.indeed.com' +
                                      next_page_link[-1],
                                      callback=self.parse)
