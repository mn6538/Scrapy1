import  urllib.parse
import  time
import  pickle
import requests
import  random

headers = {
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
			'Connection': 'keep-alive',
			'Content-Length': '19',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Host': 'www.lagou.com',
			'Origin': 'https://www.lagou.com',
			'X-Anit-Forge-Code': '0',
			'X-Anit-Forge-Token': 'None',
			'X-Requested-With': 'XMLHttpRequest'
			}


# 定义爬虫
def Crawler(savefile='info.pkl'):
	url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city={}&needAddtionalResult=false'
	infoDict = {}
	for city in ['上海', '北京', '广州', '南京', '深圳', '杭州', '成都', '武汉', '天津']:
		infoDict[city] = []
		city_quote = urllib.parse.quote(city)
		headers['Referer'] = 'https://www.lagou.com/jobs/list_?px=new&city=%s' % city_quote
		url_now = url.format(city_quote)
		for page in range(1, 31):
			print('[INFO]: Get <%s>-<Page.%s>' % (city, page))
			data = 'first=true&pn={}&kd=python'.format(page)
			try:
				res = requests.post(url_now, data=data.encode('utf-8'), headers=headers)
				res_json = res.json()['content']['positionResult']['result']
			except:
				print('[Warning]: <%s>-<Page.%s> lost...' % (city, page))
				break
			for rj in res_json:
				infoDict[city].append([rj.get('companyFullName', '无'), 
									   rj.get('companyShortName', '无'), 
									   rj.get('positionName', '无'), 
									   rj.get('positionAdvantage', '无'), 
									   rj.get('industryField', '无'), 
									   rj.get('companySize', '无'), 
									   rj.get('jobNature', '无'), 
									   rj.get('education', '无'), 
									   rj.get('workYear', '无'), 
									   rj.get('salary', '无')])
			time.sleep(random.randint(40, 60))
	f = open(savefile, 'wb')
	pickle.dump(infoDict, f)




if __name__ == '__main__':
	Crawler()