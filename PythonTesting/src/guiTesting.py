from tkinter import *

root = Tk()

# Create Label

# windowLabel1 = Label(root, text="This is the Label")
# windowLabel2 = Label(root, text="My name is Bob")
# windowLabel3 = Label(root, text="I'm using a grid")
# windowLabel4 = Label(root, text="   Empty   ")
# Put Label on Screen

#windowLabel1.pack()

# Put on screen using grid

# windowLabel2.grid(row=0, column=0)
# windowLabel3.grid(row=1, column=3)
# windowLabel4.grid(row=2, column=1)

#Making Buttons

myButton1 = Button(root, text="Click Me!")
myButton1.pack()
myButton2 = Button(root, text="Click Me!", state=DISABLED)
myButton2.pack()
myButton3 = Button(root, text="Click Me!", padx=25,pady=50)
myButton3.pack()
myButton4 = Button(root, text="Click Me!", padx=25,pady=50, fg="yellow", bg="#5E514E")
myButton4.pack()

# Make button do stuff
def clicking():
    windowLabel1 = Label(root, text="I clicked the button")
    windowLabel1.pack()

myButton5 = Button(root, text="Click Me!", padx=50,pady=10, command=clicking)
myButton5.pack()





root.mainloop()