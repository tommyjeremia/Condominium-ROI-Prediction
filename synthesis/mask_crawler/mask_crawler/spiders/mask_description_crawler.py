import scrapy
import pandas as pd


class MaskDescriptionCrawlerSpider(scrapy.Spider):
    name = 'mask_description_crawler'
    allowed_domains = [
        'https://au.iherb.com/pr/Hwipure-Disposable-KF94-N95-KN95-FFP2-Mask-1-Mask/103205',
        'https://au.iherb.com/pr/Zidian-Disposable-Protective-Mask-50-Pack/102734']

    df = pd.read_csv(
        '~/Documents/Github/synthesis/Data/Raw/products.tsv', delimiter='\t')
    start_urls = list(df.product_url)
    print(start_urls)

    def parse(self, response):
        description = response.css(
            'div.container.product-overview').css('div.col-xs-24').css('p::text').getall()
        list_description = response.css(
            'div.container.product-overview').css('div.col-xs-24').css('li::text').getall()
        yield {'description': description, 'list': list_description}
        pass

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)


# reviews-mypage product-reviews
