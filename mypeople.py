from tkinter import*
import sqlite3
from addpeople import AddPeople
from update import Update
from display import Display
from tkinter import messagebox
con = sqlite3.connect('database.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("600x750+350+200")
        self.title("My People")
        self.resizable(False,False)

        self.top = Frame(self, height=180,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self,height=600,bg='#18877c')
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image = PhotoImage(file='icons/people.png')
        self.top_image_label=Label(self.top,image=self.top_image,bg='white')
        self.top_image_label.place(x=120,y=10)

        self.heading = Label(self.top,text=' My Contacts ',font='arial 23 bold',bg='white',fg='#10778f')
        self.heading.place(x=280,y=55)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        

        self.listbox = Listbox(self.bottom, width=60, height=35)
        self.listbox.grid(row=0, column=0, padx=(30,0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        
       
        persons = cur.execute("select * from 'addressbook'").fetchall()
        print(persons)
        count = 0
        for person in persons:
            self.listbox.insert(count,str(person[0])+"."+person[1]+" "+person[2])
            count += 1
        self.scroll.grid(row=0,column=1,sticky=N+S)

        Addcontact = Button(self.bottom, text="Add" , width=12 , font='sans 12 bold',command = self.add_people)
        Addcontact.grid(row=0,column=2,padx=25,pady=20,sticky=N)

        upcontact = Button(self.bottom,text="Update" , width=12 , font='sans 12 bold',command = self.update_function)
        upcontact.grid(row=0,column=2,padx=25,pady=60,sticky=N)
        
        discontact = Button(self.bottom,text="Display" , width=12 , font='sans 12 bold',command = self.display_person)
        discontact.grid(row=0,column=2,padx=25,pady=100,sticky=N)

        delcontact = Button(self.bottom,text="Delete" , width=12 , font='sans 12 bold' ,command= self.delete_person)
        delcontact.grid(row=0,column=2,padx=25,pady=140,sticky=N)

        ExitButton = Button(self.bottom, text="Exit ",width=12, font='sans 12 bold',command=self.destroy)
        ExitButton.grid(row=0,column=2,padx=25,pady=180,sticky=N)

    def delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        query = "delete from addressbook where person_id = {}".format(person_id)
        string_for_mbox = "are you sure you wanna delete" , person.split(".")[1], "?"
        answer = messagebox.askquestion("warning","are you sure you wanna delete?" )
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("success","Deleted")
                self.destroy()

            except Exception as e:
                messagebox.showinfo("Info",str(e))    

    def add_people(self):
        add_page = AddPeople()       
        self.destroy()

    def update_function(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id =person.split(".")[0]
        

        update = Update(person_id)

    def exit(self):
        ask=messagebox.askyesno("exit","Do you really want to exit")
        if ask>0:
             self.destroy()    
        

    def display_person(self):   
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id =person.split(".")[0] 

        displaypage = Display(person_id)


        

        





        

    


        
        