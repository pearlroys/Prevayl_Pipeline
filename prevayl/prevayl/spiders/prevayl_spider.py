import scrapy
import requests
from bs4 import BeautifulSoup


class PrevaylSpider(scrapy.Spider):
    name = "sportswear"

    def start_requests(self):
        urls = [
            "https://shop.prevayl.com/collection/mens-performance-wear",
            "https://shop.prevayl.com/collection/womens-performance-wear",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sportswear in response.xpath("//div[@class='ProductCardSimple_root__xCduQ']"):
            product_name = sportswear.xpath(".//h2[contains(@class, 'Heading_root__RsZIY')]/text()").get()
            product_description = sportswear.xpath(".//div[@class='ProductCardSimple_description__FIQ0r']/p/text()").get()
            product_price = sportswear.xpath(".//div[@class='flex flex-row justify-between items-baseline w-full gap-5 md:gap-7']/p/text()").get()

            # Print the extracted data
            print("Product Name:", product_name)
            print("Product Description:", product_description)
            print("Product Price:", product_price)

            yield {
                'product_name': product_name,
                'product_description': product_description,
                'product_price': product_price
            }

            