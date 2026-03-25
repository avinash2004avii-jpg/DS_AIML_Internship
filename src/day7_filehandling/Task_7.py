# #**TASK-1 THE PERSONAL LOGGER
name=input("enter the name:  ")
daily_goal=input("enter the daily goal:  ")
with open("journal.txt","a")as file:
    file.write(f"name:{name}daily_goal:{daily_goal}\n")
    file.close()

#** TASK--2 THE CSV STUDENT LIST
import csv
with open("students.csv","w",newline="")as file:
     write = csv.writer(file)
     write.writerow(['Name','Grade','Status'])
     write.writerow(['Alice','A','Pass'])
     write.writerow(['Bob','B','Pass'])
     write.writerow(['Charlie','F','Fail'])
with open('students.csv','r') as read: 
    reads = csv.reader(read)
    for row in reads:
        if row[2] == "Pass":
            print(row[0])
    
#** TASK--3 THE SAFE OPENER
filename = input("Enter the File Name (write only file name without Extension) : ")
try :
    file = open(f'{filename.txt}','r') 
    readers = file.read()
    print(readers)
except:
    print("Oops! That file doesn't exist yet")