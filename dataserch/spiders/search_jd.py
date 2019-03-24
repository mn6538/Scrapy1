import scrapy
from dataserch.items import DataserchItem

class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["search.jd"]
    start_urls = [
        "https://search.jd.com/Search?keyword=%E6%98%BE%E7%A4%BA%E5%99%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=3.his.0.0&page=3&s=53&click=0"
        #"https://search.jd.com/Search?keyword=显示器&enc="+
        #"utf-8&suggest=3.his.0.0&pvid=3c0df64a9a3544c0aea06d3f5c3a30a8"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul[@class="gl-warp clearfix"]/li/div[@class="gl-i-wrap"]'):
            item = DataserchItem()
            item['name1'] = sel.xpath('.//div[@class="p-name p-name-type-2"]//em/text()').extract_first()
            item['price2'] = sel.xpath('.//div[@class="p-price"]/strong/i/text()').extract_first()
            print(item)
            yield item
