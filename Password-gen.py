#importing Libraries

from tkinter import *
import random
import string
import pyperclip #for clipboard

#initialize window

root =Tk()
root.geometry("400x300")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
root.configure(bg='#e3e2e1')

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold', bg='#e3e2e1').pack()
Label(root, text= "TO COPY THIS PASWWORD TO YOUR CLIPBOARD,\n PRESS 'COPY TO CLIPBOARD'", fg="black",bg="cyan",font="Arial 12 bold").place(y=200)



#password length
pass_label = Label(root, text = 'PASSWORD LENGTH\n (min 8, max 32)', font = 'arial 10 bold', bg='#e3e2e1').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()



#generator func.

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   


#button

Button(root, text = "GENERATE PASSWORD", fg="RED", command = Generator ).pack(pady= 5)

Entry(root , text = pass_str).pack()

#copy to clip func.

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', fg = "red",  command = Copy_password).pack(pady=5)




# loop to run program
root.mainloop()
