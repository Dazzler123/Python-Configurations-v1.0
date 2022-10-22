from tkinter import *

root = Tk()
root.geometry("500x300")

# header label
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0, column=3)

# input labels
Label(root, text="Customer ID").grid(row=1, column=2)
Label(root, text="Customer Name").grid(row=2, column=2)
Label(root, text="Customer Address").grid(row=3, column=2)
Label(root, text="Customer Salary").grid(row=4, column=2)

root.mainloop()
