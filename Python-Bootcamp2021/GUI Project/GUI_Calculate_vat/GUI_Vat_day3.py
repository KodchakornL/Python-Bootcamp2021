from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Calculate Expense')
GUI.geometry('450x425+100+100')

FONT1 = ('Angsana new',14,'bold')

####-------Fill up------- ####
#--Product--
L = ttk.Label(GUI,text='ชื่อสินค้า',font=FONT1).pack()

v_product = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_product,font=FONT1,width=40)
E1.pack()

#--Price--
L = ttk.Label(GUI,text='ราคาสินค้า',font=FONT1).pack()

v_price = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_price,font=FONT1,width=40)
E2.pack()
#--Quantity--
L = ttk.Label(GUI,text='จำนวนสินค้า',font=FONT1).pack()

v_quantity = StringVar()
E3 = ttk.Entry(GUI,textvariable=v_quantity,font=FONT1,width=40)
E3.pack()

###### radio เลือกประเภท vat #####
F1 = Frame(GUI)
F1.pack(pady=10)

v_radio = StringVar()

R1 = ttk.Radiobutton(F1,text='ราคารวม VAT แล้ว', variable=v_radio,value='ic')
R1.grid(row=0,column=0)

R1.invoke()  #เลือกเป็น DEFUALT

R2 = ttk.Radiobutton(F1,text='ราคา VAT + vat 7%', variable=v_radio,value='av')
R2.grid(row=0,column=1)

R3 = ttk.Radiobutton(F1,text='ราคาไม่รวม VAT 7%', variable=v_radio,value='nic')
R3.grid(row=0,column=2)

#--Button--
def Calc(event=None):  
#เวลาใช้คำสั่ง .bind() Function จะต้องใช้ event=None ถึงจะใช้ได้ท้ังปุ่ม+enter
#กรณีไม่ check enter ไม่เป็นไรไม่ใส่ก็ได้ มีแค่ปุ่มอย่างเดียว เช่น check แค่ E3 อย่างเดียวซึ่งมี
# แต่ keyboard ให้พิมพ์ไม่มีปุ่ม ใส่ event => ไม่ต้องใส่ None ก็ได้ *****โดยเพื่อความชัวร์ใส่ไปเลยก็ได้******
    # print('Radio: ', v_radio.get())


    product = v_product.get()
    price = float(v_price.get())
    quantity = float(v_quantity.get())
    total = price * quantity

    
    ####1.) ราคารวม VAT แล้ว#### 
    if v_radio.get() == 'ic':    
    # vat7 = round(total * (7/107),2)
    # nettotal =  round(total * (100/107),2)
        vat7 = total * (7/107)   # Vat 7%
        nettotal =  total * (100/107)

        # print(f'ราคาก่อน vat: {nettotal:,.2f} (vat 7%: {vat7:,.2f})')

        v_result.set(f'สินค้า : {product} \nราคาสินค้า {price:,.2f} บาท/ชิ้น จำนวน {quantity:,} ชิ้น \nทั้งหมด {total:,.2f} บาท\nสรุป ราคาสินค้า : {nettotal:,.2f} บาท (vat 7% = {vat7:,.2f})')
    ####2.) ราคา VAT  + 7% ####
    elif v_radio.get() == 'av':
        vat7 = (total * (7/100))
        nettotal = total
        sumtotal = total + vat7
        v_result.set(f'สินค้า : {product} \nราคาสินค้า {price + (vat7 / quantity) :,.2f} บาท/ชิ้น จำนวน {quantity:,} ชิ้น \nทั้งหมด {sumtotal:,.2f} บาท\nสรุป  ราคาสินค้า : {nettotal:,.2f} บาท (vat 7% = {vat7:,.2f})')
    
    ####3.) ราคาไม่รวม VAT ####
    else:
        v_result.set(f'สินค้า : {product} \nราคาสินค้า {price:,.2f} บาท/ชิ้น จำนวน {quantity:,} ชิ้น \nทั้งหมด {total:,.2f} บาท')



B1 = ttk.Button(GUI,text='Calculate',command=Calc)
B1.pack(ipadx=20,ipady=10,pady=10)

E3.bind('<Return>',Calc) # .bind()  ใส่กับ E3 = ช่อง Quantity, .bind() เช็คว่า keyboard มีการกดอะไรบ้าง ##### เพื่อที่เราจะได้ใส่ Function event เพื่อให้หลังพิมพ์ในกล่อง E3 จะได้กด enter แทนคลิกส์เมาส์ที่ปุ่มได้เลย

#--Result--
v_result = StringVar()
v_result.set('<<<<  Result this place >>>>')

R1 = ttk.Label(GUI,textvariable=v_result,font=FONT1)
R1.pack()


GUI.mainloop()