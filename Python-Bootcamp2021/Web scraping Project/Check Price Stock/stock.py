
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

code = 'AOT'
quantity = 100
txt,price = CheckPrice(code)
cal = price * quantity
print(f'หุ้น: {code} จำนวน {quantity:,.0f} ราคา: {cal:,.0f} บาท')