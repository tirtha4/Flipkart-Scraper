# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
#    allowed_domains = ['https://www.flipkart.com/books/pr?sid=bks&otracker=categorytree']
    start_urls = ['https://www.flipkart.com/books/pr?sid=bks&otracker=categorytree/']


    def parse(self, response):


        books= response.xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[*]/div[*]/div')
        for book in books:
                yield{
                'Title':book.xpath('.//a/text()').extract(),
                'Details':book.xpath('./div[1]/text()').extract(),
                'Price': book.xpath('.//a[3]/div/div[1]/text()').extract()}

        next_page = response.xpath('//div[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/a/@href').extract()
        if next_page is not None:
                try:
                    link=next_page[1]
                except IndexError:
                    link=next_page[0]


                yield scrapy.Request(response.urljoin(link))
