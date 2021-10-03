from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time


opt = webdriver.ChromeOptions() #สร้างoption
opt.add_argument('headless')

driver = webdriver.Chrome(options=opt)  # กรณี RUN ไม่ออกให้ใส่ path ใน .chrome(......) เพื่อบอกที่อยู่ chromedriver ใน Drive C
# web.get('https://www.google.com')  #http เข้าไปแค่ที่หน้าเว็บ แต่หน้าเว็ปเป็น Selenium
urllogin = 'http://www.uncle-machine.com/login/'
driver.get(urllogin)

email = driver.find_element_by_id('username')
email.send_keys('kodcha_21568@hotmail.com')

password = driver.find_element_by_id('password')
password.send_keys('123456789')

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()

# time.sleep(2)  #รอ 2 วินาที แล้วปิดหน้าใหม่ด้านล่างนี้*******************
# urlhomepage = 'http://www.uncle-machine.com/addproduct'
# driver.get(urlhomepage)

page_html = driver.page_source #ดึงโค้ดหน้าล่าสุดออกมา
# print(page_html)


driver.close()

data = soup(page_html,'html.parser')

product = data.find_all('div',{'class':'card-header'})
product = product[:21]
# print(product)

allproduct = []

for pd in product:
	allproduct.append(pd.text.replace('\n','').split(':')[1].strip())  
	# 1.replace เอามารวมบรรทัดเดียวไม่ขึ้นบรรทัดใหม่ 
	# 2.split เเยกคำออกากกัน
	# 3.เอาแค่ตัวข้อมูลที่จะเอา ['องุ่น', 'มะละกอ', 'ส้มป่อย', 'hahaha', '1', 'nothing', 'aaaaa', 
	#'ทดสอบ', 'ทดสอบ', 'GAI TOD', '???????', 'Donald Trump', 'Donald Trump', 'Cat Food', 
	#'durians from shanghai', 'ทุเรียนจากใต้', 'มังคุดจาก US', 'ประยุทธ์', 'durians from shanghai', 
	#'ทุเรียนจาก..', 'ทุเรียนจากเซี่ยงไฮ้']
	# 4.เอาspace ข้างหน้า-หลังออก

print(allproduct)
