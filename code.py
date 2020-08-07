from tkinter import *

#create root window
root=Tk()

#dimension and title
root.title("Python.GUI.Proj")
root.geometry('350x200')

#adding menu bar in root window
#new item in menubar labelled as 'New'

menu=Menu(root)
item=Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

#adding a label to the root window
lbl=Label(root,text= "Are you a coding nerd?")
lbl.grid()

#entry field
txt=Entry(root,width=10)
txt.grid(column=1,row=0)

def clicked():
    res="You wrote" + txt.get()
    lbl.configure(text=res)
    
btn=Button(root, text="Click me", fg="red",command="clicked")
btn.grid(column=2, row=0)
root.mainloop()