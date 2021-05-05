import scrapy

class IndeedSpider(scrapy.Spider):
    name = 'indeed'

    start_urls = ['https://ca.indeed.com/jobs?q=full+stack+developer&l=Ottawa%2C+ON']

    def parse(self, response):
        for job in response.css('div.jobsearch-SerpJobCard'):
            yield{
                 'title' : job.css('a.jobtitle::attr(title)').get(),
                 'company' : job.css('span.company::text').get(),
                 'rating': job.css('span.ratingsContent::text').get(),
                 'location' : job.css('div.location::text').get(),
                 'salary' : job.css('span.salaryText::text').get(),
                 'description': job.css('div.summary ul li::text').getall()
             }


        next_page = response.css('ul.pagination-list li a::attr(aria-label)').getall()
        next_page_link = response.css('ul.pagination-list li a::attr(href)').getall()
        print("link", next_page_link)

        # if next_page[-1].lower == "next":
        #     yield response.follow(url=next_page_link[-1], callback=self.parse)        

## scrapy crawl indeed -o indeed.json            


