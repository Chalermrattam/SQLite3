# python bootcamp ep4

import sqlite3

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
View_Member()
#View_OneMember('C1002')
 
