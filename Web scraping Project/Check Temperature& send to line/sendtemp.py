from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup


def Temperature(pid):
    
    # ดึงข้อมูลจาก www.tmd.go.th
    url = f'https://www.tmd.go.th/province.php?id={pid}'

    #ให้ urllib.request จัดเรียงแถวของ web แล้วให้ beautifulSoup scan
    webopen = req(url)    #เปิดเว็ปโดยไม่เปิด Web Browser urllib.request ทำการดึง(request)
    page_html = webopen.read() # สั่ง read เป็น text , Code html ไปใช้งานต่อ
    webopen.close() # ปิดการ request 

    #BeautifulSoup as soup ทำการสแกน page_html
    data = soup(page_html,'html.parser') # soupทำการอ่านข้อมูลอัตโนมัติ #แปลงเป็น soup

    #print(type(data)) #type is <class 'bs4.BeautifulSoup'>
    temp = data.find_all('td',{'class':'strokeme'}) #tag, class
    #print(temp) #จะได้element code มันออกมา ดังนั้นจะให้ได้ตัวอุณหภูมิออกมาอย่างเดียว ต้องรู้ว่าข้อมูลนี้เป็น list ต้อง print ที่ตน.0
    #print(type(temp)) # <class 'bs4.element.ResultSet'>
    #print(temp[0])
    '''
    จะได้ result
    <td align="left" class="strokeme" style="FONT-SIZE:40px;
    color: #F6E207; padding-left:25px;"
    width="100%">32.5 °C</td>
    '''
    #print(temp[0].text)  #.text เป็นคำสั่งที่ใช้ในการตัด tag ออก # Resultได้แค่ Result อุณหภูมิออกมาจริงๆ
    temp = temp[0].text


    province = data.find_all('span',{'class':'title'})
    province = province[0].text
    province = province.strip() #ลบช่องว่างที่มากับข้อความ

    #print(f'จังหวัด {province} ขณะนี้อุณหภูมิ {temp}')
    return f'จังหวัด {province} ขณะนี้อุณหภูมิ {temp}'

alltext = ''  #เอาไว้สะสมข้อความเพื่อจะได้ส่งข้อความใน line ได้ในครั้งเดียว
for i in range(20,40): # id = 1-10
    #Try ทำข้างนอกหรือข้างใน def ก็ได้
    try:
        text = Temperature(i) # check temperature
        alltext = alltext + text + '\n' #เอาผลลัพธ์ที่ check temperature มาบวกค่าเก่า
        # ตัวเดิมมาบวกกับข้อความ f'จังหวัด {province} ขณะนี้อุณหภูมิ {temp}'
    except:
        print('Not found')

print(alltext)
#ได้ข้อความทั้งหมดแล้วส่ง line
from songline import Sendline
token ='FA33KVNMXUBC9Bq2DwYpj0nrMiLS3hew3eDRFOa08C9'
messenger = Sendline(token)
messenger.sendtext(alltext)







