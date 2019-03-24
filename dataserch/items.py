# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataserchItem(scrapy.Item):
    #天猫computer
    GOODS_NAME = scrapy.Field()  # 商品名称
    GOODS_PRICE = scrapy.Field()  # 价格
    MONTHLY_SALES = scrapy.Field()  # 月销量
    GOODS_URL = scrapy.Field()  # 商品url
    #安居客房价
    price = scrapy.Field()
    rent_type = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    towards = scrapy.Field()
    floor = scrapy.Field()
    decoration = scrapy.Field()
    building_type = scrapy.Field()
    community = scrapy.Field()
# 亚马逊包
    title = scrapy.Field()
    price1 = scrapy.Field()
    reviews = scrapy.Field()
    ASIN = scrapy.Field()
    BSR = scrapy.Field()
    star = scrapy.Field()
    rank = scrapy.Field()
    launch_date = scrapy.Field()
    url = scrapy.Field()
    #京东手机
    ititle = scrapy.Field()
    iprice = scrapy.Field()
    iurl = scrapy.Field()
    icomment_num=scrapy.Field()
    #京东显示器
    name1=scrapy.Field()
    price2=scrapy.Field()

