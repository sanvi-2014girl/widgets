from tkinter import *
#screen
window = Tk()
window.title("tkinter GUI")
window.geometry('500x500')
window.configure(bg='pink')
#add widgets
x = Label(text = "Hey welcome to codingal!",bg="#ff0000", fg = "white")
x.pack()
#entry
e = Entry(window,width= 30)
e.pack()
#label
L = Label(window,text="",bg = "blue",fg="white",width = 50)
L.pack()
#btn function
def sayhello():
    name = e.get()
    L.config(text="hey"+name+"How are you?")
#btn
b = Button(window, text="click here!",command= sayhello)
b.pack()
window.mainloop()