import scrapy
from newsscraper.helpers import standardize_data
from scrapy.selector.unified import SelectorList


class NewsSpider(scrapy.Spider):
    name = "news_spider"
    allowed_domains = ["informadocaribe.com"]
    start_urls = ["https://informadocaribe.com/category/nacional/"]

    def parse(self, response):
        articles = response.css("div.mg-blog-post-box")

        for article in articles:
            title_element: SelectorList = article.css("h4 a")

            url = title_element.attrib["href"]
            title = article.css("h4 a::text").get()
            string_date = article.css("span.mg-blog-date a::text").get().strip()

            yield {
                "title": title,
                "url": url,
                "date": standardize_data(string_date),
            }
