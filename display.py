from tkinter import*
import sqlite3
from tkinter import messagebox
from addpeople import AddPeople

con = sqlite3.connect('database.db')
cur = con.cursor()
class Display(Toplevel):
    def __init__(self,person_id):

        Toplevel.__init__(self)
        self.geometry("600x700+350+200")
        self.title("Display Person")
        self.resizable(False,False)
        
        print("person_id =",person_id)

        query = "select * from addressbook where person_id = '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        print(result)
        self.person_id = person_id
        person_name = result[1]
        person_sname = result[2]
        person_email = result[3]
        person_mob = result[4]
        address = result[5]

        print("person name",person_name)

        self.top = Frame(self, height=180, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=600, bg='#17c2a8')
        self.bottom.pack(fill=X)
        
        self.top_image = PhotoImage(file='icons/people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=100,y=10)

        self.heading = Label(self.top,text=' Display Contact ',font='arial 23 bold',bg='white',fg='#10778f')
        self.heading.place(x=280,y=55)
        
        #id
        
        #name
        self.label_name =Label(self.bottom, text="Name:",font='sans 15 bold',bg='#17c2a8',fg='white')
        self.label_name.place(x=140,y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=8)
        self.entry_name.insert(0,person_name)
        self.entry_name.config(state = "disabled")
        self.entry_name.place(x=250,y=40)
        #id 
        self.label_sname =Label(self.bottom, text="Surname:",font='sans 15 bold',bg='#17c2a8',fg='white')
        self.label_sname.place(x=140,y=90)

        self.entry_sname = Entry(self.bottom, width=30, bd=8)
        self.entry_sname.insert(0,person_sname)
        self.entry_sname.config(state = "disabled")
        self.entry_sname.place(x=250,y=90)
        #email
        self.label_email =Label(self.bottom, text="E-mail id:",font='sans 15 bold',bg='#17c2a8',fg='white')
        self.label_email.place(x=140,y=140)

        self.entry_email = Entry(self.bottom, width=30, bd=8)
        self.entry_email.insert(0,person_email)
        self.entry_email.config(state = "disabled")
        self.entry_email.place(x=250,y=140)
        #mobile
        self.label_mob =Label(self.bottom, text="Mobile no.:",font='sans 15 bold',bg='#17c2a8',fg='white')
        self.label_mob.place(x=140,y=190)

        self.entry_mob = Entry(self.bottom, width=30, bd=8)
        self.entry_mob.insert(0,person_mob)
        self.entry_mob.config(state = "disabled")
        self.entry_mob.place(x=250,y=190)
        
        #address
        self.label_add =Label(self.bottom, text="Address:",font='sans 15 bold',bg='#17c2a8',fg='white')
        self.label_add.place(x=140,y=240)

        self.entry_add = Text(self.bottom, width=24, height=8)
        self.entry_add.insert(1.0,address)
        self.entry_add.config(state = "disabled")
        self.entry_add.place(x=250,y=240)

        