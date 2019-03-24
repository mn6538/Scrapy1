# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dataserch.items import DataserchItem

class TopSpider(CrawlSpider):
    name = 'ymxbb'
    allowed_domains = ['www.amazon.com']
    #TOP100链接
    # start_urls = ['https://www.amazon.com/Best-Sellers-Beauty-Cosmetic-Bags/zgbs/beauty/11062771/ref=zg_bs_pg_1?_encoding=UTF8&pg=1']
    #类目产品链接
    start_urls = ['https://www.amazon.com/b/ref=sr_aj?node=11062771&ajr=0']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='a-row a-spacing-none a-spacing-top-mini']/a",)), callback='parse_item'),
        #翻页
        Rule(LinkExtractor(restrict_xpaths=("//span[@class='pagnLink']",)), follow=True),

        #TOP100
         Rule(LinkExtractor(restrict_xpaths=("//li[@class='zg-item-immersion']/span/div/span/a",)), callback='parse_item'),
        # #翻页
        # Rule(LinkExtractor(allow=r'Best-Sellers-Beauty-Cosmetic-Bags/zgbs/beauty/11062771/ref=zg_bs_pg_\d+\?_encoding=UTF8&pg=\d+'),follow=True),

    )

    def parse_item(self, response):
        # print(response)
        item=DataserchItem()
        # 标题
        title_text = response.xpath("//h1/span[@id='productTitle']/text()").extract_first()
        if title_text is not None:
            item['title'] = title_text.strip()
        else:
            item['title']='AAA'

        # 图片


        # 价格
        price_text = response.xpath("//span[@id='priceblock_ourprice']/text()").extract_first()
        if price_text != None:
            item['price1'] = price_text.strip()
        elif price_text == None:
            item['price1'] = response.xpath("//span[@id='price_inside_buybox']/text()").extract_first()
        else:
            item['price1'] = response.xpath("//span[@id='priceblock_saleprice']/text()']/text()").extract_first()

        # 评论
        item['reviews'] = response.xpath("//span[@id='acrCustomerReviewText']/text()").extract_first()

        # ASIN
        asin = response.xpath("//*[@id='productDetails_detailBullets_sections1']/tr[5]/td/text()").extract_first()
        if asin != (None):
            item['ASIN']=asin.strip()
        else:
            asin1 = response.xpath("//*[@id='detailBullets_feature_div']/ul/li[3]/span/span[2]/text()").extract_first()
            if asin1 !=(None):
                item['ASIN'] = asin1.strip()
            else:
                asin2=item['ASIN']=response.xpath("//b[text()='ASIN: ']/../text()").extract_first()
                if asin2!=(None):
                    item['ASIN'] = asin2.strip()
                else:
                    item['ASIN'] = response.xpath("//div[@id='detailBullets_feature_div']/ul/li[2]/span/span[2]/text()").extract_first()

        # BSR排名
        bsr=response.xpath("//*[@id='productDetails_detailBullets_sections1']//tr/td/span/span[1]/text()[1]").extract_first()
        if bsr!=[]:
            bsr=str(bsr)
            item['BSR']=(bsr.split('#')[-1].split(" (")[0])
        else:
            bsr1=response.xpath("//li[@id ='SalesRank']/text()").extract_first()
            if bsr1!=[]:
                bsr1=str(bsr1)
                item['BSR'] = (bsr1.split('#')[-1].split(" (")[0])
            else:
                item['BSR']='aaa'

        #星级
        star_text=response.xpath("//span[@id='acrPopover']/@title").extract_first()
        if star_text==(None):
            #A+页面星级
            item['star']=response.xpath("//*[@id='prodDetails']/div/div[2]/div[1]/div[2]/div/div/table/tbody/tr[2]/td[2]/span/span[1]/a[2]/i/span/text()").extract_first()
        else:
            item['star'] = star_text

        #分类排名
        item["rank"] = ",".join(response.xpath("//li[@class='zg_hrsr_item']//span//text()").extract_first())

        #上架时间
        item['launch_date'] = response.xpath("//*[@id='detailBullets_feature_div']/ul/li[5]/span/span[2]/text()").extract_first()
        #item接受时间规定
        
        #链接
        url=str(response)
        item["url"]= (url.split('https://')[-1].split(">")[0])
        print(item)
        yield item




