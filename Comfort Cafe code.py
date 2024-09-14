from Category_For_Cafe import Category
import sqlite3
import os
import csv #We have to modify code to include CSV FIles

#Have to be soon Modified into Operable CSV Files instead of Stagnant Data
Menu_Dictionary_Form = {"CFE" : "Coffee", "CHCFE" : "Chilled Coffee", "T": "Tea", "CHT" : "Chilled Tea"}
Cost_Dictionary_Form = {"CFE" : "3", "CHCFE" : "4", "T": "3", "CHT" : "4"}
Menu_list = ["Coffee - {CFE} ($3)", "Chilled Coffee {CHCFE} ($4)", "Tea {T} ($3)", "Chilled Tea {CHT} ($4)"]
Admin_Dictionary = {"Fish" : "Cockeral", "Richard" : "Dick"}

Bill = Category("Bill")
file = open("Bill.txt", "w")

price = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Menu_Func():#This is basically for the menu
 A = len(Menu_list)
 for n in range(0,A):
  x = Menu_list[n]
  print(x)

Ordered_List = []

def Order_Func():
 Order = input("\nAre you ready to order?? Please Input the Code for the Dish that you would like [If ordering is done, please type 2]: ")

 while Order != "2": #Order Loop
  Ordered_List.append(Order.upper())
  a = Order.upper()
  Bill.deposit(int(Cost_Dictionary_Form[(a)]), Menu_Dictionary_Form[a])
  Order = input("\nAdd one more!! Please Input the Code for the Dish that you would like [If ordering is done, please type 2]: ")

def ItemAdd_Func():
 X = str(input("Please enter the Item that you would like to add: "))
 Y = str(input("Please enter the Item Code: "))
 Z = str(input("Please enter the Price!"))
 Z_With_Dollar = "$"+Z
 Sentence = X +" " +  "-" + " " + f"{{{Y}}}" + " " +  f"({Z_With_Dollar})"
 Menu_list.append(Sentence)
 Menu_Dictionary_Form[Y] = X
 Cost_Dictionary_Form[Y] = Z

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customer_Checking = (input("Are you a customer?? [Yes - 1 | No - 2]")) #Asking Customer if he/she is ready to order and it is used later on to see if they still wanna order

if Customer_Checking == "1":
 print("Here's the Menu!!")
 Menu_Func()
 Order_Func()
 print("\n")
 print(Bill)

 file.write(str(Bill))
 file.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if Customer_Checking == "2":

 Admin_Checking = input("Are you an Admin?? [Yes - 1 | No - 2]")
 if Admin_Checking == "1":
  Login_ID = str(input("Please enter your Login-ID: "))

 while Login_ID not in Admin_Dictionary.keys():
   Login_ID = str(input(" Invalid ID! Please enter your Correct Login-ID: "))

 if Login_ID in Admin_Dictionary.keys():
   Password = str(input("Please enter the Password for the corresponding Login-ID:"))

 while Password != Admin_Dictionary.get(Login_ID):
   Password = str(input("Incorrect Password. Please re-enter the Password for the corresponding Login-ID:"))

 if Password == Admin_Dictionary.get(Login_ID):
   Options = input(str("Welcome in! What would you like to?? [Add Item to Menu - 1 | Update Item - 2 | Delete Item - 3]"))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 if Options == "1":
  ItemAdd_Func()


 if Options == "3":
  Menu_Func()
  X = input("Please enter the item code to delete!: ")
  A = f"{{{X}}}"
  for n in Menu_list:
   if A in n:
    Menu_list.remove(n)
    Menu_Dictionary_Form.pop(X)
    Cost_Dictionary_Form.pop(X)
  Menu_Func()
  print(Menu_Dictionary_Form)
  print(Cost_Dictionary_Form)


 if Options == "2":
  Menu_Func()
  X = input("Please enter the item code to update!: ")
  Edit_Options = str(input("What would you like to update? [Name - 1 | Code - 2 | Price - 3]"))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  if Edit_Options == "1":
   New_Name = str(input("Please enter the new name you intend to give update!: "))
   A = f"{{{X}}}"
   for n in Menu_list:
    if A in n:
     Z = Cost_Dictionary_Form[X]
     Z_With_Dollar = "$"+Z
     Position = Menu_list.index(n)
     Menu_list.remove(n)
     New_Sentence = New_Name +" " +  "-" + " " + f"{{{X}}}" + " " +  f"({Z_With_Dollar})"
     Menu_list.insert(Position, New_Sentence)
     Menu_Dictionary_Form[X] = New_Name
   print("end")
   print(Menu_list)
   print(Menu_Dictionary_Form)

  if Edit_Options == "2":
   New_Code = str(input("Please enter the new codey you intend to give update!: "))
   Name = Menu_Dictionary_Form.get(X)
   A = f"{{{X}}}"
   for n in Menu_list:
    if A in n:
     Z = Cost_Dictionary_Form[X]
     Y = Menu_Dictionary_Form[X]
     Z_With_Dollar = "$"+Z
     Position = Menu_list.index(n)
     Menu_list.remove(n)
     New_Sentence = Name +" " +  "-" + " " + f"{{{New_Code}}}" + " " +  f"({Z_With_Dollar})"
     Menu_list.insert(Position, New_Sentence)
     Menu_Dictionary_Form.pop(X)
     Cost_Dictionary_Form.pop(X)
     Menu_Dictionary_Form[New_Code] = Y
     Cost_Dictionary_Form[New_Code] = Z
   Menu_Func()
   print(Menu_Dictionary_Form)
   print(Cost_Dictionary_Form)

  if Edit_Options == "3":
    Cost_New = str(input("Please enter the new price!: "))
    Cost_New_Dollar = "$"+Cost_New
    Name = Menu_Dictionary_Form.get(X)
    A = f"{{{X}}}"
    for n in Menu_list:
     if A in n:
      Position = Menu_list.index(n)
      Menu_list.remove(n)
      New_Sentence = Name +" " +  "-" + " " + f"{{{X}}}" + " " +  f"({Cost_New_Dollar})"
      Menu_list.insert(Position, New_Sentence)
      Cost_Dictionary_Form[X] = Cost_New
      Menu_Func()
      print(Cost_Dictionary_Form)
    Menu_Func()
    print(Menu_Dictionary_Form)
    print(Cost_Dictionary_Form)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~