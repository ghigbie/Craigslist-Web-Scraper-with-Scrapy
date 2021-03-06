# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['http://newyork.craigslist.org/search/egr']

    def parse(self, response):
        listings = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for listing in listings:
            yield {'Listing': listing}
        print('***********************')