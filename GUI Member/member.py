# python bootcamp ep4

import sqlite3
from tkinter import *
from tkinter import ttk , messagebox

conn = sqlite3.connect('member.sqlite3') # connect กับ db (ใส่ชื่อได้เลยมันจะสร้าง db อัตโนมัติ) ถ้าไม่เปิด project เป็น Folder ต้องระบุ path ถึงจะอยู่ใน Folder เดียวกัน
c = conn.cursor()

# เป็น grammar คำสั่ง sql ยกเว้น memberinfo ที่เป็นชื่อตารางที่ตั้งเองได้
c.execute("""CREATE TABLE IF NOT EXISTS memberinfo (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                memberid TEXT,
                first_name TEXT,
                last_name TEXT,
                tel TEXT,
                points INTEGER,
                note TEXT ) """)

def Insert_NewMember(memberid,first_name,last_name,tel,points,note): 
    ID = None
    with conn:
        command = 'INSERT INTO memberinfo VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(None,memberid,first_name,last_name,tel,points,note))
    conn.commit()  
    print('Saved')

def View_Member():
    with conn:
        command = 'SELECT * FROM memberinfo'
        c.execute(command)
        result = c.fetchall() # c.fetchone() , c.fetchmany(5)
    print(result)
    return result

def View_OneMember(memberid):
    with conn:
        command = 'SELECT * FROM memberinfo WHERE memberid=(?)'
        c.execute(command,([memberid]))
        result = c.fetchall() # c.fetchone() , c.fetchmany(5)
    print(result)
    return result

def Delete_Member(ID):
    with conn:
        command = 'DELETE FROM memberinfo WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('{}: deleted'.format(ID))

def Delete_Memberid(memberid):
    with conn:
        command = 'DELETE FROM memberinfo WHERE memberid=(?)'
        c.execute(command,([memberid]))
    conn.commit()
    print('{}: deleted'.format(memberid))

def Update_Member(ID,field,data):
    with conn:
        command = 'UPDATE memberinfo SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command,([data,ID]))
    conn.commit()
    print('{}: {}={} update'.format(ID,field,data))


#Insert_NewMember('C1002','สมศรี','ดีจัง','0809876543',50,'สมาชิกขาประจำ')
#Delete_Member(1)
#Delete_Memberid('C1002')
#Update_Member(1,'first_name','สมหญิง')
#View_Member()
#View_OneMember('C1002')
 

GUI = Tk()
GUI.geometry('900x600')
GUI.title('โปรแกรมบันทึกสมาชิก')

v_search = StringVar()
search = ttk.Entry(GUI,textvariable=v_search,font=(None,20),width=15) # รับหรือแสดงค่า v_search ที่กล่องข้อความ
search.place(x=50,y=50)

def SearchMember():
    search = v_search.get() # รับค่า v_search เก็บที่ตัวแปร
    data = View_OneMember(search)
    if len(data) >= 1:
        data = data[0]
        v_memberid.set(data[1]) # set ค่า v_memberid
        v_first_name.set(data[2]) # set ค่า v_first_name
        v_last_name.set(data[3])
        v_tel.set(data[4])
        v_points.set(data[5])
        v_note.set(data[6])
        #print(search)
    else:
        messagebox.showwarning('Not found','ไม่มีสมาชิกคนนี้ กรุณาตรวจสองรหัสสมาชิก')

FB1 = Frame(GUI)
FB1.place(x=90,y=100)
bsearch = ttk.Button(FB1,text='ค้นหาชื่อสมาชิก',command=SearchMember)
bsearch.pack(ipadx=30,ipady=20)

##########

F2 = Frame(GUI)
F2.place(x=400,y=100)

v_memberid = StringVar()
L = Label(F2,text='รหัสสมาชิก',font=(None,15)).pack()
E1 = ttk.Entry(F2,textvariable=v_memberid,font=(None,20),width=25)
E1.pack()

v_first_name = StringVar()
L = Label(F2,text='ชื่อ',font=(None,15)).pack()
E2 = ttk.Entry(F2,textvariable=v_first_name,font=(None,20),width=25)
E2.pack()

v_last_name = StringVar()
L = Label(F2,text='นามสกุล',font=(None,15)).pack()
E3 = ttk.Entry(F2,textvariable=v_last_name,font=(None,20),width=25)
E3.pack()

v_tel = StringVar()
L = Label(F2,text='เบอร์โทร',font=(None,15)).pack()
E4 = ttk.Entry(F2,textvariable=v_tel,font=(None,20),width=25)
E4.pack()

v_points = StringVar()
L = Label(F2,text='คะแนน',font=(None,15)).pack()
E5 = ttk.Entry(F2,textvariable=v_points,font=(None,20),width=25)
E5.pack()

v_note  = StringVar()
L = Label(F2,text='อื่นๆ ',font=(None,15)).pack()
E6 = ttk.Entry(F2,textvariable=v_note,font=(None,20),width=25)
E6.pack()

##########

FB2 = Frame(GUI)
FB2.place(x=510,y=510)
bsave = ttk.Button(FB2,text='บันทึก/อัพเดท')
bsave.pack(ipadx=30,ipady=20)


GUI.mainloop()