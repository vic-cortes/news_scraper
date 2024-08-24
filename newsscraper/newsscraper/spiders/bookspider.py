import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    pagination_url = "https://books.toscrape.com/catalogue/"

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            relative_url = book.css("h3 a ::attr(href)").get()
            book_url = self.pagination_url + relative_url

            yield response.follow(book_url, callback=self.parse_book_page)

        if next_page := response.css(".next a::attr(href)").get():
            # We split the URL and get the last part of it
            # since sometimes the URL is not complete
            next_page = next_page.split("/")[-1]
            next_page_url = self.pagination_url + next_page
            print(f"{next_page_url = }")
            yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
        """
        This method will parse the book page and extract the information
        """
        bread_crumb_xpath = "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        description_xpath = (
            "//div[@id='product_description']/following-sibling::p/text()"
        )

        title = response.css(".product_main h1::text").get()
        category = response.xpath(bread_crumb_xpath).get()
        description = response.xpath(description_xpath).get()
        price = response.css("p.price_color::text").get()

        table_rows = response.css("table tr")

        all_keys = table_rows.css("th ::text").getall()
        all_values = table_rows.css("td ::text").getall()

        table = dict(zip(all_keys, all_values))
        rating = response.css("p.star-rating").attrib["class"].split()[-1]

        yield {
            "title": title,
            "category": category,
            "price": price,
            "description": description,
            "rating": rating,
            "table": table,
        }
