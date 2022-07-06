import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a'))
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//div[contains(@class, "product_main")]/h1/text()').get()
        item['price'] = response.xpath('//div[contains(@class, "product_main")]/p/text()').get()
        item['image_url'] = response.urljoin(response.xpath('//div[contains(@class, "item")]/img/@src').get())
        item['category'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        return item
