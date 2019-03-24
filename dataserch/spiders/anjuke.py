# Author: Charles

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from dataserch.items import DataserchItem


# 定义爬虫类
class anjuke(scrapy.spiders.CrawlSpider):
	name = 'anjuke'
	start_urls = ['https://cd.zu.anjuke.com/']
	rules = (
				Rule(LinkExtractor(allow=r'fangyuan/p\d+/'), follow=True),
				Rule(LinkExtractor(allow=r'https://cd.zu.anjuke.com/fangyuan/\d{10}'), callback='parse_item'),
			)
	def parse_item(self, response):
		item = DataserchItem()
		# 租金
		item['price'] = int(response.xpath("//ul[@class='house-info-zufang cf']/li[1]/span[1]/em/text()").extract_first())
		# 出租方式
		item['rent_type'] = response.xpath("//ul[@class='title-label cf']/li[1]/text()").extract_first()
		# 户型
		item['house_type'] = response.xpath("//ul[@class='house-info-zufang cf']/li[2]/span[2]/text()").extract_first()
		# 面积
		item['area'] = int(response.xpath("//ul[@class='house-info-zufang cf']/li[3]/span[2]/text()").extract_first().replace('平方米',''))
		# 朝向
		item['towards'] = response.xpath("//ul[@class='house-info-zufang cf']/li[4]/span[2]/text()").extract_first()
		# 楼层
		item['floor'] = response.xpath("//ul[@class='house-info-zufang cf']/li[5]/span[2]/text()").extract_first()
		# 装修
		item['decoration'] = response.xpath("//ul[@class='house-info-zufang cf']/li[6]/span[2]/text()").extract_first()
		# 住房类型
		item['building_type'] = response.xpath("//ul[@class='house-info-zufang cf']/li[7]/span[2]/text()").extract_first()
		# 小区
		item['community'] = response.xpath("//ul[@class='house-info-zufang cf']/li[8]/a[1]/text()").extract_first()
		yield item