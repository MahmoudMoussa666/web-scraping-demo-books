import scrapy


class BooksBasicSpider(scrapy.Spider):
    name = 'books_basic'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath('//article[@class="product_pod"]')
        for book in books:
            yield response.follow(book.xpath('.//h3/a/@href').get(), callback=self.book_parsing)

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page)

    def book_parsing(self, response):
        yield {
            'title': response.xpath('//div[contains(@class, "product_main")]/h1/text()').get(),
            'price': response.xpath('//div[contains(@class, "product_main")]/p/text()').get(),
            'image_url': response.urljoin(response.xpath('//div[contains(@class, "item")]/img/@src').get()),
            'category': response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        }
