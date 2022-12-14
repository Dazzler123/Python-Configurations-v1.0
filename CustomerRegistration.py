from tkinter import *

root = Tk()
root.geometry("500x300")

# heading label
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0, column=3)

# save customer
def saveCustomer():
    print("Customer details saved.")

# input labels
Label(root, text="Customer ID").grid(row=1, column=2)
Label(root, text="Customer Name").grid(row=2, column=2)
Label(root, text="Customer Address").grid(row=3, column=2)
Label(root, text="Customer Salary").grid(row=4, column=2)

cusID = StringVar
cusName = StringVar
cusAddress = StringVar
cusSalary = DoubleVar

# input textfields
Entry(root, textvariable=cusID).grid(row=1, column=3)
Entry(root, textvariable=cusName).grid(row=2, column=3)
Entry(root, textvariable=cusAddress).grid(row=3, column=3)
Entry(root, textvariable=cusSalary).grid(row=4, column=3)

# save button
Button(text="Save Customer", command=saveCustomer).grid(row=5, column=3)

root.mainloop()
