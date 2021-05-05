import scrapy

class IndeedSpider(scrapy.Spider):
    name = 'indeed'

    start_urls = ['https://ca.indeed.com/jobs?q=full+stack+developer&l=Ottawa%2C+ON']

    def parse(self, response):
        for job in response.css('div.jobsearch-SerpJobCard'):
            yield{
                 'title' : job.css('h2.title a.jobtitle::attr(title)').get(),
                 'company' : job.css('div.sjcl div span.company a::text').get(),
                 'rating': job.css('div.sjcl div span.ratingsDisplay a span.ratingsContent::text').get(),
                 'location' : job.css('div.recJobLoc::attr(data-rc-loc)').get(),
                 'salary' : job.css('div.salarySnippet span.salary span.salaryText::text').get(),
                 'description': job.css('div.summary ul li::text').getall()
             }

        next_page = response.css('ul.pagination-list li a::attr(aria-label)').getall()
        next_page_link = response.css('ul.pagination-list li a::attr(href)').getall()

        if next_page[-1].lower() == "next":
            yield response.follow(url= 'https://ca.indeed.com' + next_page_link[-1], callback= self.parse)        
           


