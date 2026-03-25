#**write in the file
file=open("sample.txt","w")
file.write("hello,this is a filehandling example.")
file.close()
#**READ the file
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

with open("sample.txt","r")as file:
    content=file.read()
    print(content)

# try:
#    with open("missing.txt","r")as file:
#         print(file.read())
#    exceptFileNotFound
#         print("Filenot found,try with another file")
   
#**WRITING THE OWN CSV FILE
import csv
with open("day07.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["avi", 30, "India"])
    writer.writerow(["hemi", 25, "New york"])
    writer.writerow(["sharath", 28, "Chicago"])
with open("day07.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#*IMPORTING EXCLE  FILES
import pandas as pd

# Read Excel file
df = pd.read_excel("sample.xlsx")

# Display data
print(df)
df = pd.read_excel(r"C:\Users\achar\DS_AI_internship\src\sample.xlsx")
print(df[["NAME"]])
print(df.head())      # first 5 rows
print(df.tail())      # last 5 rows
print(df.shape)       # (rows, columns)
print(df.columns)     # column names
print(df.info())      # data types + non-null count
print(df.describe())  # statistics for numeric columns
