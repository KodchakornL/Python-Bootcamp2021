from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup


def NEWS(cat):
    
    url = f'https://www.matichon.co.th/{cat}'

    #ให้ urllib.request จัดเรียงแถวของ web แล้วให้ beautifulSoup scan
    webopen = req(url)    #เปิดเว็ปโดยไม่เปิด Web Browser urllib.request ทำการดึง(request)
    page_html = webopen.read() # สั่ง read เป็น text , Code html ไปใช้งานต่อ
    webopen.close() # ปิดการ request 

    #BeautifulSoup as soup ทำการสแกน page_html
    data = soup(page_html,'html.parser') # soupทำการอ่านข้อมูลอัตโนมัติ #แปลงเป็น soup

    #print(type(data)) #type is <class 'bs4.BeautifulSoup'>

    news = data.find_all('h3',{'class':'entry-title td-module-title'})  #ได้หัวข้อข่าว
    # print(len(new1))
    news = news[:12] # news < 12 

    topics = []

    for n in news:
        dt = [n.a['title'],n.a['href']]
        topics.append(dt)
    
    # print(topics)
    return topics
    # title = new[0]
    # print(title.a['title'])
    # print(title.a['href'])

'''
<h3 class="entry-title td-module-title"><a href="https://www.matichon.co.th/economy/news_2633428" 
rel="bookmark" title="ส.ค.นี้ &#8216;รฟท.&#8217; เล็งเปิดประมูลพื้นที่ย่านสถานีธนบุรี ให้เอกชนเช่า 30 ปี คาดเพิ่มรายได้กว่า 3.58 พันล้าน
" data-href="https://www.matichon.co.th/economy/news_2633428" class="ud-module-link">ส.ค.นี้ &#8216;รฟท.&#8217; 
เล็งเปิดประมูลพื้นที่ย่านสถานีธนบุรี ให้เอกชนเช่า 30 ปี คาดเพิ่มรายได้กว่า 3.58 พันล้าน</a></h3>
'''

data = NEWS('economy')

for d in data:
    print(d[1])
    print('-'*10)