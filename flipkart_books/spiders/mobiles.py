# -*- coding: utf-8 -*-
import scrapy


class MobilesSpider(scrapy.Spider):
    name = 'mobiles'
    #allowed_domains = ['https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree']
    start_urls = ['https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree/']

    def parse(self, response):

        mobiles= response.xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[*]/div/a/div[*]')
        for mobile in mobiles:
            yield{
                'Name':mobile.xpath('./div[1]/div[1]/text()').extract(),
                'Price':mobile.xpath('./div[2]/div[1]/div/div[1]/text()').extract(),
                'Feature':mobile.xpath('./div[1]/div[4]/ul/li/text()').extract()}
        next_page= response.xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/a/@href').extract()
        if next_page is not None:
                   try:
                       link=next_page[1]
                   except IndexError:
                       link=next_page[0]


                   yield scrapy.Request(response.urljoin(link))
