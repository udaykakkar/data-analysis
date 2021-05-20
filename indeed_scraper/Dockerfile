FROM python:3
WORKDIR /data-analysis/indeed_scraper
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "scrapy crawl indeed"]

