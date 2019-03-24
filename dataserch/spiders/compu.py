
#encoding=utf-8
import scrapy
from dataserch.items import DataserchItem

class TapTop(scrapy.Spider):
    name = 'compu'
    allowed_domains = ['detail.tmall.com','list.tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.aVNGHZ&cat=53320010&sort=d&style=g&active=1&industryCatId=53320010&theme=663&type=pc']

    def parse(self,response):
        divs = response.xpath('//div[@id="J_ItemList"]/div')
        print("items len = %d" %len(divs))
        for div in divs:
            item = DataserchItem()
            # 价格
            price1txt = div.xpath('div/p[1]/em/text()').extract_first()
            if price1txt is not None:
                item['GOODS_PRICE'] = price1txt.strip()
            else:
                item['GOODS_PRICE'] = 'AAA'
            # 月销量
            sale1txe = div.xpath('div/p[3]/span[1]/em/text()').extract_first()
            if sale1txe is not None:
                item['MONTHLY_SALES'] = sale1txe.strip()
            else:
                item['MONTHLY_SALES'] = 'BBB'
            # url
            good_url = div.xpath('div/div[2]/a[1]/@href').extract_first()
            if not 'http' in good_url:
                good_url = response.urljoin(good_url)
            url1tex = good_url
            if url1tex is not None:
                item['GOODS_URL'] = url1tex.strip()
            else:
                item['GOODS_URL'] = 'CCC'

            # 进入店里面
            yield scrapy.Request(url=good_url, meta={'item':item}, callback=self.detail_parse)
        next_page = response.urljoin(response.xpath('//a[@class="ui-page-next"]/@href').extract_first())
        yield scrapy.Request(url=next_page,callback=self.parse)

    def detail_parse(self,response):
        # 获取item
        item = response.meta['item']
        # 商品名称
        title1tex = response.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/a/text()').extract_first()
        if title1tex is not None:
            item['GOODS_NAME'] = title1tex.strip()
        else:
            item['GOODS_NAME'] = 'DDD'
        print(item)
        yield item
