
import csv
from datetime import datetime


from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def CheckPrice(CODE):
	#ปป.แค่ symbol = GPSC
	url = f'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={CODE}&ssoPageId=10&selectPage=2'
	webopen = req(url)    #เปิดเว็ปโดยไม่เปิด Web Browser urllib.request ทำการดึง(request)
	page_html = webopen.read() # สั่ง read เป็น text , Code html ไปใช้งานต่อ
	webopen.close() # ปิดการ request 
	data = soup(page_html,'html.parser') # soupทำการอ่านข้อมูลอัตโนมัติ #แปลงเป็น soup

	# class = col-xs-6
	rawdata = data.find_all('div',{'class':'col-xs-6'}) # print('COUNT',len(rawdata))
	price = float(rawdata[2].text) # print('Price: ', price)

	date = data.find_all('span',{'class':'stt-remark'})
	# date = date[0].text = ข้อมูลล่าสุด 20/03/2021 03:19:56  ถ้าจะเอาแค่ 20/03/2021 03:19:56
	date = date[0].text[13:]

	text = f'STOCK: {CODE} PRICE: {price} BATH UPDATE:{date}'
	return (text,float(price))

def Write(data):
	dt = datetime.now().strftime('%Y-%m-%d %H%M')
	with open(f'Stock {dt}.csv','w',newline='',encoding='utf-8') as file: #'a' = append data เรื่อยๆ ,'w' = เขียนครั้งเดียวในเวลาที่กำหนด,  newline='' เป็นการขึ้นบันทัดใหม่เขียน''ติดกันเพื่อไม่ให้มีspace เว้นบรรทัด
	# create file writer 
		fw = csv.writer(file)
		fw.writerows(data)

		# fw.writerow(['A',20])
		# fw.writerows([['A',20],['B',30],['C',50]]) list ซ้อน list

	print('Successful')

# product = [['A',20],['AA',30],['AAAA',50]]
# Write(product)

allstock = ['AOT','CPALL','GPSC','GULF','BBL']


result = []
for st in allstock:
	data = CheckPrice(st)
	result.append(data)

print(result)
Write(result)