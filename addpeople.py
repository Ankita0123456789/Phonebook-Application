from tkinter import *
import sqlite3
from tkinter import messagebox
con = sqlite3.connect('database.db')
cur = con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("600x700+350+200")
        self.title("Add new People")
        self.resizable(False,False)

        self.top = Frame(self, height=180, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=600, bg='#d2a5e6')
        self.bottom.pack(fill=X)
        
        self.top_image = PhotoImage(file='icons/team.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=100,y=10)

        self.heading = Label(self.top,text=' Add New Contacts ',font='arial 23 bold',bg='white',fg='#0e7387')
        self.heading.place(x=280,y=55)
        
        #id
        
        #name
        self.label_name =Label(self.bottom, text="Name",font='sans 15 bold',bg='#d2a5e6',fg='white')
        self.label_name.place(x=49,y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=5)
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=160,y=40)
        #id 
        self.label_sname =Label(self.bottom, text="Surname",font='sans 15 bold',bg='#d2a5e6',fg='white')
        self.label_sname.place(x=49,y=80)

        self.entry_sname = Entry(self.bottom, width=30, bd=5)
        self.entry_sname.insert(0,"Enter Surname")
        self.entry_sname.place(x=160,y=80)
        #email
        self.label_email =Label(self.bottom, text="E-mail id",font='sans 15 bold',bg='#d2a5e6',fg='white')
        self.label_email.place(x=49,y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=5)
        self.entry_email.insert(0,"Enter E-mail")
        self.entry_email.place(x=160,y=120)
        #mobile
        self.label_mob =Label(self.bottom, text="Mobile no.",font='sans 15 bold',bg='#d2a5e6',fg='white')
        self.label_mob.place(x=49,y=160)

        self.entry_mob = Entry(self.bottom, width=30, bd=5)
        self.entry_mob.insert(0,"Enter number")
        self.entry_mob.place(x=160,y=160)
        
        #address
        self.label_add =Label(self.bottom, text="Address",font='sans 15 bold',bg='#d2a5e6',fg='white')
        self.label_add.place(x=49,y=200)

        self.entry_add = Text(self.bottom, width=24, height=8)
        self.entry_add.place(x=160,y=200)

        #button
        button = Button(self.bottom, text="Add person",font='sans 15 bold',command=self.add_people)
        button.place(x=250, y=450)
    def add_people(self):
        name = self.entry_name.get()
        sname = self.entry_sname.get()
        email = self.entry_email.get()
        mob = self.entry_mob.get()
        add = self.entry_add.get(1.0, 'end-1c')    
        
        if name and sname and email and mob and add !="":
            try:
                 #add it to database

                 #insert into 'addressbook' (person_name,person_email,person_mobile,address,surname) values ()
                  
                query = "insert into 'addressbook' (person_name,person_sname,person_email, person_mob1,address) values (?,?,?,?,?)"
                cur.execute(query, (name, sname, email, mob, add))
                con.commit()
                messagebox.showinfo("success","contact added")
                
                self.destroy()
                

            except EXCEPTION as e:    
                messagebox.showerror("Error",str(e)) 
        else:
            messagebox.showerror("Error", "fill all the fields", icon='warning')
 