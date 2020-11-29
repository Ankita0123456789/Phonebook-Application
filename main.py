from tkinter import*
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self,root):
        self.root = root

        #frames

        self.top = Frame(root, height=180,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(root,height=600,bg='#34eb95')
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image = PhotoImage(file='icons/contact.png')
        self.top_image_label=Label(self.top,image=self.top_image,bg='white')
        self.top_image_label.place(x=120,y=10)

        self.heading = Label(self.top,text=' My Phonebook App ',font='arial 20 bold',bg='white',fg='#22853d')
        self.heading.place(x=280,y=55)

        self.date_lbl = Label(self.top, text=" Date: "+date, font='arial 12 bold',fg = '#22853d', bg='white')
        self.date_lbl.place(x=430,y=148)


        #button - View People
        self.viewButton = Button(self.bottom, text= "   My contacts ", fg="#000000", bg='white', font='arial 20 bold',command=self.my_people)
        self.viewButton.place(x=200,y=70)

        #button - Add People
        self.addButton = Button(self.bottom, text=" Add Contacts", fg= "#000000", bg='white', font='arial 20 bold', command = self.addpeoplefunction)
        self.addButton.place(x=200,y=184)

        #button - About us
        self.aboutButton = Button(self.bottom, text="    About us    ",fg="#000000", bg='white', font='arial 20 bold',command=self.about_us)
        self.aboutButton.place(x=200,y=300)

        #button - Exit
        self.ExitButton = Button(self.bottom, text="        Exit         ", fg= "#000000",bg='white',font='arial 20 bold',command=self.root.destroy)
        self.ExitButton.place(x=200,y=410)

    def my_people(self):
        people = MyPeople()

    def about_us(self):
        aboutpage = About()    


    def addpeoplefunction(self):
        addpeoplewindow = AddPeople()

    def exit(self):
        ask=messagebox.askyesno("exit","Do you really want to exit")
        if ask>0:
             self.root.destroy()    

def main():
    root=Tk()
    app=Application(root)
    root.title("Phonebook App")
    root.geometry("600x750+350+200")
    root.resizable(False,False)
    root.mainloop()
    
if __name__ == '__main__':
    main()