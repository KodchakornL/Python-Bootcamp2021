from tkinter import *
from tkinter import ttk   # file ย่อยใน tkinter 
from tkinter import messagebox   #ไว้เป็น หน้าต่างเด้งออกมา try except Error

GUI = Tk()  #Class
GUI.title('Calculate Expense')
GUI.geometry('400x600+100+100')  #+0+0 เปิดโปรแกรมแล้วมาชิดขอบ
GUI.configure(bg='#5C9DC0')

#--------Config----------
FONT1 = ('Angsana New',16,'bold')
FONT2 = ('Angsana New',14,'bold')
#--------Image------------
pt = PhotoImage(file='amazon1.png').subsample(8)
amazonpic = ttk.Label(GUI,image=pt,background='#5C9DC0')
amazonpic.pack(pady=20)

#----text-# ต้องเอาไว้เหนือคำสั่ง ช่องค้นหาเพื่อให้มันอยู่ข้างบน กลับกันถ้าเอาไว้ด้านล่างคำสั่งมันก็จะอยู่ด้านล่าง
L = ttk.Label(GUI,text='Product calculation program',font=FONT1,background='#5C9DC0')
L.pack()

#-------- BOX PRODUCT ---------
L1 = ttk.Label(GUI,text='Product name',font=FONT2,background='#5C9DC0')
L1.pack()

m_product = StringVar() #ตัวแปรสำหรับเก็บชื่อสินค้าตอนพิมพ์ StringVar() is box that can flexible value
E1 = ttk.Entry(GUI,textvariable=m_product,font=FONT1,width=40)
E1.pack(pady=10)
#-------- BOX PRICE ---------
L2 = ttk.Label(GUI,text='Price',font=FONT2,background='#5C9DC0')
L2.pack()

m_price = StringVar()   #ตัวแปรสำหรับเก็บราคาสินค้าตอนพิมพ์ 
E2 = ttk.Entry(GUI,textvariable=m_price,font=FONT1,width=40)
E2.pack(pady=10)
#-------- BOX QUANTITIES---------
L3 = ttk.Label(GUI,text='Quantities',font=FONT2,background='#5C9DC0')
L3.pack()

m_quantity = StringVar()  #ตัวแปรสำหรับเก็บปริมาณสินค้าตอนพิมพ์ 
E3 = ttk.Entry(GUI,textvariable=m_quantity,font=FONT1,width=40)
E3.pack(pady=10)

#------------Buttom--------------
#Just add ttk # take mouse is Blue
#Function for store a programe
def Calculate():
    product = m_product.get()
    quantity = float(m_quantity.get())
    price = float(m_price.get())
    
    purchase = price * quantity
    tax = purchase * 0.07
    total = purchase + tax
    tax = round(tax,2)
    total = round(total,2)
    
    textshow0 = f'I bought {product} ,which quantities is  {quantity:,} pc.\n'
    textshow1 = f'I spend for product {purchase:,} USD\n'
    textshow2 = f'I spend for tax {tax:,} USD\n'
    textshow3 = f'Today, I spend {total:,} USD'
    v_result.set('Daily Note expense: '+textshow0+textshow1+textshow2+textshow3)
    messagebox.showinfo('Daily Note expense: ',textshow0+textshow1+textshow2+textshow3)

B1 = ttk.Button(GUI,text='Calculate',command=Calculate)
B1.pack(ipadx=20,ipady=10) # ipadx ขยายปุ่มแนวนอน   ipady ขยายปุ่มแนวตั้ง

# ----------Result-----------
v_result = StringVar()   # คือกล่องสำหรับเก็บคำแปล
FONT2 = ('Angsana New',16)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2, foreground='black',background='#5C9DC0')  # textvariable = ข้อความปป.ตามผลลัพธ์ที่กรอก
R1.pack()

GUI.mainloop()
