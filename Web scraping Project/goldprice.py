
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def GoldPrice():
	#ปป.แค่ symbol = GPSC
	url = f'https://www.goldtraders.or.th/'
	webopen = req(url)    #เปิดเว็ปโดยไม่เปิด Web Browser urllib.request ทำการดึง(request)
	page_html = webopen.read() # สั่ง read เป็น text , Code html ไปใช้งานต่อ
	webopen.close() # ปิดการ request 
	data = soup(page_html,'html.parser') # soupทำการอ่านข้อมูลอัตโนมัติ #แปลงเป็น soup


	allclass = ['DetailPlace_uc_goldprices1_lblBLSell',
				'DetailPlace_uc_goldprices1_lblBLBuy',
				'DetailPlace_uc_goldprices1_lblOMSell',
				'DetailPlace_uc_goldprices1_lblOMBuy']

	allprice = []

	# class = col-xs-6
	for al in allclass:
		rawdata = data.find_all('span',{'id':al}) # print('COUNT',len(rawdata))
		allprice.append(float(rawdata[0].text.replace(',','')))
	# print(allprice)
	header = ['ราคาทองคำแท่ง-ขายออก', 'ราคาทองคำแท่ง-รับซื้อ', 'ทองคำรูปพรรณ-ขายออก', 'ทองคำรูปพรรณ-รับซื้อ']
	
	result = {}

	for h,p in zip(header,allprice):  #แปลงจาก list เป็น Dictionary
		result[h] = p

	# print(result)
	return result

price = GoldPrice()
# print(price['ทองคำรูปพรรณ-รับซื้อ'])

for h,p in price.items():  #แปลงจาก dict มาคล้าย list
	# print(h,p)
	print(f'{h} ราคา {p} บาท')

# GoldPrice()
# print(GoldPrice())
