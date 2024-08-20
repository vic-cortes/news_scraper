import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    pagination_url = "https://books.toscrape.com/catalogue/"

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            yield {
                "name": book.css("h3 a::text").get(),
                "price": book.css(".product_price .price_color::text").get(),
                "url": book.css("h3 a").attrib["href"],
            }

        if next_page := response.css(".next a::attr(href)").get():
            # We split the URL and get the last part of it
            # since sometimes the URL is not complete
            next_page = next_page.split("/")[-1]
            next_page_url = self.pagination_url + next_page
            print(f"{next_page_url = }")
            yield response.follow(next_page_url, callback=self.parse)
