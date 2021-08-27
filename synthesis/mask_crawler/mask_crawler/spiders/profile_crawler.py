import scrapy


class ProfileCrawlerSpider(scrapy.Spider):
    name = 'profile_crawler'
    allowed_domains = ['https://au.iherb.com/me/buckeroomama']
    start_urls = ['https://au.iherb.com/me/buckeroomama/']

    def parse(self, response):
        fav_items = response.css(
            'div.product-title').css('strong::text').getall()
        profile = response.css(
            'div.me-profile-picture').css('img::attr(src)').get()
        for item in fav_items:
            yield {'url': response.meta['url'], 'fav_items': item, 'profile': profile}
        pass

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            print(url)
            yield scrapy.Request(url=url, callback=self.parse, meta={'url': url})
