# import tkinter as tk
# from tkinter import filedialog, Text
# import os
#
# root = tk.Tk()
#
# canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# canvas.pack()
#
# root.mainloop()

# ///////////////////////////////////////////////////////////////////////////

# print("Dasindu Bimlaka Hewagamage")
# print("0----")
# print(" ||||")
# print("*" * 10)
# print(10/2)
# name = "hi"
# print(name)
#
# price = 10  <---- int
# rating = 4.9 <---- double
# name = 'Dasindu' <---- String
# is_published = True <--- boolean
#
# input() <--- function for user input,
#          parenthesis athule print krnn ona text eka danna plwn
#
# full_name = 'John Smith'
# age = 20
# is_exists = True
#
# name = input('What is your name? ')
# print('Hi ' + name + ' !')

# name = input('Enter your name : ')
# color = input('Enter your favorite color : ')
# print(name + ' likes ' + color)

#
# birth_year = input('Enter your birth year : ')
# calculate_age = 2022 - int(birth_year)
# print('Your age is : ' + str(calculate_age))

# weight_in_pounds = input('Enter your weight is pounds : ')
# convert_pounds_to_kg = int(weight_in_pounds) *  0.45359237
# print('Your weight in Kilograms is : ' + str(convert_pounds_to_kg))

# course = '''
# Hi there!
#             I'm Dasindu, this is to show how to print more than one line
#             in python.
# Bye....'''
# print(course)

# position = 'Python for Developers'
#             0123456789101112131415
# print(position[-2]) <--- position eka print krnn plwn
# print(position[0:3]) <-- range ekakata print krnn plwn
#
# name = input("Enter ur name : ")
# print("Hi "+name+" !")

# print("==================== DATE OF BIRTH (DOB) PRINTER ====================")
# year = input("Enter year : ")
# month = input("Enter month : ")
# day = input("Enter day : ")
# print("Processing........")
# print("Your DOB is : " + day + "/" + month + "/" + year)
# print("======================================================================")

# x = input()
# y = input()
# print(x*int(y))

for i in range(10):
  if not i % 2 == 0:
    print(i+1)