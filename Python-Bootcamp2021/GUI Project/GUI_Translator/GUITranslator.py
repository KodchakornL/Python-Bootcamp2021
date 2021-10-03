from tkinter import *     # จากไลบราลี่ tkinter; * คือให้ดึงความสามารถทั้งหมด 
from tkinter import ttk # ttk is theme of tk

# ----------Google Translate ------------
from googletrans import Translator
translator = Translator()   # สร้างฟังก์ชันแปลขึ้นมา

GUI = Tk()  # สร้างหน้าต่างหลัก
GUI.geometry('500x300')  #กว้าง x สูง
GUI.title('โปรแกรมแปบภาษา by Uncle Engineer') #ชื่อที่หัวโปรแกรม
# ----------Config ------------
FONT = ('Angsana New',15)
# ----------Label ------------
L = ttk.Label(GUI,text = 'กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)  # show passage in GUI
L.pack()
# ----------Entry (ช่องกรอกข้อความ)------------
v_vocab = StringVar() #กล่องเก็บข้อความ
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40) # textvariable = v_vocab คือหากกรอกข้อความในช่องนี้จะเก็ยในv_vacab เพื่อนำไปใช้กับ Function def Translate
E1.pack(pady = 20)  # เว้นพื้นที่กล่องกรอก กับ ปุ่ม

# ----------Button (ปุ่มแปล)------------
#B1 = Button(GUI,text='Translate') #สร้างปุ่มขึ้นมา
#B1.pack() # โชว์ปุ่มขึ้นมาวางจากบนลงล่าง

def Translate():
    vocab = v_vocab.get() # .get คือสั่งให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print(vocab + ' : ' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text)  # สั่งโชว์ GUI  เชื่อม result กับ translate ให้แสดงผลใน ส่วนแสดงผลของ result
    
B1 = ttk.Button(GUI,text='Translate',command = Translate) #สร้างปุ่มขึ้นมา  #command = name Function def Translate
B1.pack(ipadx=20,ipady=10) # show ปุ่มขึ้นมาวางจากบนลงล่าง # ipadx(internal pading axis X)=20,ipady(internal pading axis Y)=10

# ----------Label ------------
L = ttk.Label(GUI,text = 'คำแปล',font=FONT)
L.pack()

# ----------Result------------
v_result = StringVar()   #คือกล่องสำหรับเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2, foreground='green')  # textvariable = ข้อความปป.ตามผลลัพธ์ที่กรอก
R1.pack()



GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด อยู่บรรทัดสุดท้ายเท่านั้น



