#easyread=>translator

# from googletrans import Translator,LANGUAGES
from easyread.translator import Translate
from openpyxl import Workbook
from datetime import datetime
# print(LANGUAGES)

# translator = Translator() #ตัวแปลคำศัพท์
# result = Translator.translate('cat',dest='th',encoding='uft=')
# print(result.text)
article = open('article.txt','r',encoding='utf-8')   # 'r'=read  , encoding='utf-8'
article = article.read()   #.read() อ่านทั้งหมด , readline=อ่านแค่บรรทัดนั้น
article = article.split()  # .split แยกเป็นคำๆเก็บไว้ในlist

print('Count: ',len(article))

result = []

for word in article:
	# print(word)
	# res = translator.translate(word,dest='zh-cn',src='th')  
	res = Translate(word) 
	#translator.translate() ตัวแปลคำศัพท์  => destination=dest='zh-cn' คือแปลเป็นภาษาจีน
	if res != None:
		# print(res['meaning']) # print เฉพาะความหมาย
		result.append([word,res['meaning']])

# print(result)
excelfile = Workbook()
sheet = excelfile.active

header = ['Vocab','Translate']
sheet.append(header)

for rs in result:
	sheet.append(rs)

dt =datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save(f'Vocab - {dt}.xlsx')  #เพิ่มวันที่ลงไปใน ชื่อไฟล์