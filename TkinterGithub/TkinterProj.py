import tkinter
import sqlite3
cnt=sqlite3.connect("university.db")
from tkinter import messagebox
#---------------------------sqlite3---------------------------
# sql=''' CREATE TABLE students(
#         number INTEGER PRIMARY KEY ,
#         user VARCHAR(20) NOT NULL ,
#         password VARCHAR(30) NOT NULL,
#         course1 VARCHAR(20),
#         course2 VARCHAR(20),
#         course3 VARCHAR(20),
#         course4 VARCHAR(20),
#         course5 VARCHAR(20),
#         course6 VARCHAR(20)
#         )'''
# cnt.execute(sql)

#---------------------------main win---------------------------    
def login():
    global session ,count,pw
    user=txt_user.get()
    pas=txt_pass.get()
    
    sql=''' SELECT * FROM students WHERE user=? and password=?'''
    result=cnt.execute(sql,(user,pas))
    rows=result.fetchall()
    
    if (len(rows)>0):
        lbl_msg.configure(text='welcome to your account!', fg='green')
        btn_login.configure(state='disable')
        btn_logout.configure(state='active')
        btn_selection.configure(state='active')
        txt_user.delete(0,'end')
        txt_pass.delete(0,'end')
        session=user
        pw=pas
        count=0
        
    else:
        lbl_msg.configure(text='wrong Name or Password!' , fg='red')
        count+=1
        if count==3:
            lbl_msg.configure(text='Unfortunately,You have entered the wrong Name or Password more than three times!' , fg='red')
            btn_login.configure(state='disabled')
            
def validate(user,pas):
    if user=='' or pas=='':
        lbl_msg.configure(text='please fill the textbox',fg='red')
        return False
    if len(pas)<8:
        lbl_msg.configure(text='password length at least 8')
        return False
    
    if user.lower()=='admin':
        lbl_msg.configure(text='admin is restricted!',fg='red')
        return False
    
    return True

def submit():
    user=txt_user.get()
    pas=txt_pass.get()
    result=validate(user,pas)
    if result:
        sql=''' INSERT INTO students (user,password) 
        VALUES(?,?)'''
        
        cnt.execute(sql,(user,pas))
        cnt.commit()
        lbl_msg.configure(text='submit done!' , fg='green')
        txt_user.delete(0,'end')
        txt_pass.delete(0,'end')       
def delete():
    global session ,pw
    if session==False:
        lbl_msg.configure(text='please Login first!', fg='red')
        return
    confirm=messagebox.askyesno(message='are you sure to delete your account?')
    if confirm:
        if session=='admin':
            lbl_msg.configure(text='admin acc is not removable!', fg='red')
            return
        sql=''' DELETE FROM students WHERE user=? and password=?'''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        lbl_msg.configure(text='your acc deleted!', fg='green')
        session=False
        btn_logout.configure(state='disabled')
        btn_selection.configure(state='disabled')
        btn_login.configure(state='active')
        
  
def logout():
    global session
    session=False
    lbl_msg.configure(text='you are logout!', fg='green')
    btn_login.configure(state='active')
    btn_logout.configure(state='disabled')
    btn_selection.configure(state='disabled')
 #-----------------------------------------------------------------
def selection():
#--------------------------------new win---------------------------------
    confirm=messagebox.askyesno(message='If you have made any choices in the past,they will be deleted upon entring the panel ! Do you confirm? ')
    if confirm:
        txt=''
        sql=''' UPDATE students SET course1=null WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        sql=''' UPDATE students SET course2=null WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        sql=''' UPDATE students SET course3=null WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        sql=''' UPDATE students SET course4=null WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        sql=''' UPDATE students SET course5=null WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        sql=''' UPDATE students SET course6=null WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
    else:
        return
    
    #----------------------------courses--------------------------
    def course1():
        global txt , session ,pw
        sql=''' UPDATE students SET course1="course 1" WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        txt+="course 1 ,"
        lbl_selected.configure(text=txt ,fg="yellow")
        btn_course1.configure(state="disabled")
       
    def course2():
        global txt , session ,pw
        sql=''' UPDATE students SET course2="course 2" WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        txt+="course 2 ,"
        lbl_selected.configure(text=txt ,fg="yellow")
        btn_course2.configure(state="disabled")
        
    def course3():
        global txt , session ,pw
        sql=''' UPDATE students SET course3="course 3" WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        txt+="course 3 ,"
        lbl_selected.configure(text=txt ,fg="yellow")
        btn_course3.configure(state="disabled")
        
    def course4():
        global txt , session ,pw
        sql=''' UPDATE students SET course4="course 4" WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        txt+="course 4 ,"
        lbl_selected.configure(text=txt ,fg="yellow")
        btn_course4.configure(state="disabled")
        
    def course5():
        global txt , session ,pw
        sql=''' UPDATE students SET course5="course 5" WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        txt+="course 5 ,"
        lbl_selected.configure(text=txt ,fg="yellow")
        btn_course5.configure(state="disabled")
        
    def course6():
        global txt , session ,pw
        sql=''' UPDATE students SET course6="course 6" WHERE user=? AND password=? '''
        cnt.execute(sql,(session,pw))
        cnt.commit()
        
        txt+="course 6 ,"
        lbl_selected.configure(text=txt ,fg="yellow")
        btn_course6.configure(state="disabled")   
    
    def ok():
        global txt
        if txt=='':
            lbl_selected.configure(text="You have not selected any courses yet!",fg="red")
            return
        confirm=messagebox.askyesno(message='Do you approve of this function?')
        if confirm:
            global session , pw
            sql=''' SELECT * FROM students WHERE user=? and password=?'''
            result=cnt.execute(sql,(session,pw))
            rows=result.fetchall()
            print("a user with the following profile entered and selected:"+str(rows))
            print("These were the user's choices : " +txt)
            lbl_selected.configure(text="your selected courses were successfully registered : "+txt ,fg="green")
            lbl_choosed.configure(text='')
            btn_course1.configure(state="disabled")
            btn_course2.configure(state="disabled")
            btn_course3.configure(state="disabled")
            btn_course4.configure(state="disabled")
            btn_course5.configure(state="disabled")
            btn_course6.configure(state="disabled")
            btn_reset.configure(state="disabled")
            btn_ok.configure(state="disabled")
            
    def reset():
        global txt , session  , pw 
        confirm=messagebox.askyesno(message='Do you want to choose again? This will erase all your choices!')
        if confirm:
            txt=''
            lbl_selected.configure(text="Your past choices have been deleted." , fg="red")
            
            btn_course1.configure(state="active")
            sql=''' UPDATE students SET course1=null WHERE user=? AND password=? '''
            cnt.execute(sql,(session,pw))
            cnt.commit()
            
            btn_course2.configure(state="active")
            sql=''' UPDATE students SET course2=null WHERE user=? AND password=? '''
            cnt.execute(sql,(session,pw))
            cnt.commit()
            
            btn_course3.configure(state="active")
            sql=''' UPDATE students SET course3=null WHERE user=? AND password=? '''
            cnt.execute(sql,(session,pw))
            cnt.commit()
            
            btn_course4.configure(state="active")
            sql=''' UPDATE students SET course4=null WHERE user=? AND password=? '''
            cnt.execute(sql,(session,pw))
            cnt.commit()
            
            btn_course5.configure(state="active")
            sql=''' UPDATE students SET course5=null WHERE user=? AND password=? '''
            cnt.execute(sql,(session,pw))
            cnt.commit()
            
            btn_course6.configure(state="active")
            sql=''' UPDATE students SET course6=null WHERE user=? AND password=? '''
            cnt.execute(sql,(session,pw))
            cnt.commit()

    
    #--------------------------------------    
    selection=tkinter.Toplevel(win)
    selection.title('selection of courses')
    selection.geometry('800x380')
    
    lbl_select=tkinter.Label(selection,text='Please choose your courses and finally click OK : ')
    lbl_select.pack()
    
    btn_course1=tkinter.Button(selection,text='course 1' ,command=course1)
    btn_course1.pack()
    
    btn_course2=tkinter.Button(selection,text='course 2' ,command=course2)
    btn_course2.pack()
    
    btn_course3=tkinter.Button(selection,text='course 3' ,command=course3)
    btn_course3.pack()
    
    btn_course4=tkinter.Button(selection,text='course 4' ,command=course4)
    btn_course4.pack()
    
    btn_course5=tkinter.Button(selection,text='course 5' ,command=course5)
    btn_course5.pack()
    
    btn_course6=tkinter.Button(selection,text='course 6' ,command=course6)
    btn_course6.pack()
    
    lbl_choosed=tkinter.Label(selection,text='Selected courses : ')
    lbl_choosed.pack()
    
    lbl_selected=tkinter.Label(selection, text='')
    lbl_selected.pack()
    
    btn_ok=tkinter.Button(selection,text='OK' ,command=ok)
    btn_ok.pack()
    
    btn_reset=tkinter.Button(selection,text='Reset' ,command=reset)
    btn_reset.pack()
     
    selection.mainloop()   


    
#------------------------Main----------------------
      
#---------------win-------------
session=False
win=tkinter.Tk()
win.title('Login , Submit')
win.geometry('350x360')
#-------------------------user , pass------------------------
txt=''
count=0

lbl_user=tkinter.Label(win,text='Name: ')
lbl_user.pack()

txt_user=tkinter.Entry(win)
txt_user.pack()

lbl_pass=tkinter.Label(win,text='Password: ')
lbl_pass.pack()

txt_pass=tkinter.Entry(win)
txt_pass.pack()

lbl_msg=tkinter.Label(win, text='')
lbl_msg.pack()

#---login ,submit , delete , logout , selection of courses---

btn_login=tkinter.Button(win,text='Login', command=login)
btn_login.pack()

btn_submit=tkinter.Button(win,text='submit' ,command=submit)
btn_submit.pack()

btn_delete=tkinter.Button(win,text='delete account' ,command=delete)
btn_delete.pack()

btn_logout=tkinter.Button(win,text='Logout' ,command=logout , state='disabled')
btn_logout.pack()

btn_selection=tkinter.Button(win,text='selection of courses' ,command=selection , state='disabled')
btn_selection.pack()

win.mainloop()

