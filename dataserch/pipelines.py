# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class DataserchPipeline(object):
    def __init__(self):
        self.conn= pymysql.connect(host="127.0.0.1", user="root" ,passwd="111111" ,db="anjuke")
    def process_item(self, item, spider):
        '''
        # jd显示器
        name1 = str(item["name1"])
        print(name1)
        price2 = str(item["price2"])

        sql2 = "insert into jcxsq(cname, cprice) values ('"+name1+"','"+price2+"')"
        print(sql2)
        self.conn.query(sql2)





        GOODS_NAME = item["GOODS_NAME"]
        GOODS_PRICE = item["GOODS_PRICE"] # 价格
        MONTHLY_SALES = item["MONTHLY_SALES"]  # 月销量
        GOODS_URL = item["GOODS_URL"] # 商品url

        sql = "insert into computer(GOODS_NAME, GOODS_PRICE, MONTHLY_SALES, GOODS_URL)values('"+GOODS_NAME+"','"+GOODS_PRICE+"','"+MONTHLY_SALES+"','"+GOODS_URL+"')"
        self.conn.query(sql)
        self.conn.commit()

    def close_spider(self, spider):
            # self.conn.commit()
        self.conn.close()

'''

        # 安居客房价
        price = str(item["price"])  #租金
        rent_type = str(item["rent_type"]) #出租方式
        house_type = str(item["house_type"]) #户型
        area = str(item["area"]) #面积
        towards = str(item["towards"]) #朝向
        floor = str(item["floor"]) #楼层
        decoration = str(item["decoration"]) #装修
        building_type = str(item["building_type"]) #住房类型
        community = str(item["community"]) #小区
        sql1 ="insert into anjuke(price, rent_type, house_type, area, towards, floor, decoration, building_type, community) values ('"+price+"','"+rent_type+"','"+house_type+"','"+area+"','"+towards+"','"+floor+"','"+decoration+"','"+building_type+"','"+community+"')"
        self.conn.query(sql1)
        self.conn.commit()

    def close_spider(self, spider):
            # self.conn.commit()
            self.conn.close()

'''

        # 亚马逊包
        title = str(item["title"])  #标题
        price1 = str(item["price1"]) #价格
        reviews = str(item["reviews"])#评论
        ASIN = str(item["ASIN"])#ASIN
        BSR = str(item["BSR"])#BSR排名
        star = str(item["star"])#星级
        rank = str(item["rank"])#分类排名
        launch_date = str(item["launch_date"])#上架时间
        url = str(item["url"])
        #url
        sql3="insert into ymxbb(title,price1, reviews, ASIN, BSR, star, rank, launch_date, url) VALUES ('"+title+"','"+price1+"','"+reviews+"','"+ASIN+"','"+BSR+"','"+star+"','"+rank+"','"+launch_date+"','"+url+"')"
        print(sql3)
        self.conn.query(sql3)
'''











