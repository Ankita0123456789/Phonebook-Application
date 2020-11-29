from tkinter import*
import sqlite3
from tkinter import messagebox
from addpeople import AddPeople

con = sqlite3.connect('database.db')
cur = con.cursor()
class Update(Toplevel):
    def __init__(self,person_id):

        Toplevel.__init__(self)
        self.geometry("600x700+350+200")
        self.title("Update Person")
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

        self.bottom = Frame(self, height=600, bg="#3287a8")
        self.bottom.pack(fill=X)
        
        self.top_image = PhotoImage(file='icons/team.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=100,y=10)

        self.heading = Label(self.top,text=' Update Contact ',font='arial 23 bold',bg='white',fg='#3287a8')
        self.heading.place(x=280,y=55)
        
        #id
        
        #name
        self.label_name =Label(self.bottom, text="Name",font='sans 15 bold',bg='#3287a8',fg='white')
        self.label_name.place(x=49,y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=5)
        self.entry_name.insert(0,person_name)
        self.entry_name.place(x=160,y=40)
        #id 
        self.label_sname =Label(self.bottom, text="Surname",font='sans 15 bold',bg='#3287a8',fg='white')
        self.label_sname.place(x=49,y=80)

        self.entry_sname = Entry(self.bottom, width=30, bd=5)
        self.entry_sname.insert(0,person_sname)
        self.entry_sname.place(x=160,y=80)
        #email
        self.label_email =Label(self.bottom, text="E-mail id",font='sans 15 bold',bg='#3287a8',fg='white')
        self.label_email.place(x=49,y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=5)
        self.entry_email.insert(0,person_email)
        self.entry_email.place(x=160,y=120)
        #mobile
        self.label_mob =Label(self.bottom, text="Mobile no.",font='sans 15 bold',bg='#3287a8',fg='white')
        self.label_mob.place(x=49,y=160)

        self.entry_mob = Entry(self.bottom, width=30, bd=5)
        self.entry_mob.insert(0,person_mob)
        self.entry_mob.place(x=160,y=160)
        
        #address
        self.label_add =Label(self.bottom, text="Address",font='sans 15 bold',bg='#3287a8',fg='white')
        self.label_add.place(x=49,y=200)

        self.entry_add = Text(self.bottom, width=24, height=8)
        self.entry_add.insert(1.0,address)
        self.entry_add.place(x=160,y=200)

        #button
        button = Button(self.bottom, text="Update Contact",font='sans 15 bold',command=self.update_people)
        button.place(x=250, y=450)

    def update_people(self):
        id = self.person_id
        name = self.entry_name.get()
        sname = self.entry_sname.get()
        email = self.entry_email.get()
        mob = self.entry_mob.get()
        add = self.entry_add.get(1.0, 'end-1c')  
        query = "update addressbook set person_name = '{}',person_sname = '{}', person_email = '{}', person_mob1 = '{}' , address = '{}' where person_id = {}".format(name, sname, email, mob, add, id) 
        

        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo("success"," contact updated")

        except Exception as e:
            print(e)    
        