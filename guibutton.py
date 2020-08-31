import tkinter as tk

root = tk.Tk()

def myClick():
	myLabel= tk.Label(root, text="Look! I clicked a Button!!")
	myLabel.pack()

myButton = tk.Button(root, text="Click Me!", padx=50, pady=50, bg="black", fg = "red", command=myClick)
myButton.pack()

root.mainloop()