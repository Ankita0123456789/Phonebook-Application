from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+350+200")
        self.title("About Us")
        self.resizable(False,False)

        self.top = Frame(self, height=550, width =550, bg='#4c1663')
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text='Hey, this is about us page',font = "monoscope 18 bold underline" ,bg='#4c1663',fg='#cbd663')
        self.text.place(x=140, y=60)

        self.text = Label(self.top, text='This application is made by  the '
                           '\n MCA students for the educational purpose.'
                           '\n'
                           '\n This application is the project for'
                           '\n software Engineering.'
                           '\n'
                           '\n you can contact us on'
                           '\n'
                           '\n Facebook - https://facebook.com/MCA'
                           '\n'
                           '\n Instagram - MCA_GROUP',font = "monoscope 14", bg='#4c1663',fg="white")
        self.text.place(x=100, y=130)
                            

                        
                          