import os
import csv

with open('Dickhead.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(["A","b","c","D"])


with open('Dickhead.csv', 'r') as file2:
    read = csv.reader(file2)

    for x in read:
        print(x)

if os.path.exists("Dickhead.csv"):
  os.remove("Dickhead.csv")
  print("File is Deadge")
else:
  print("The file does not exist")