num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
op=input("enter the operand (+,-,*,/)")

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("invalid operand")


name="avinash"
msg="welcome"
print(f"hi{name},{msg} everyone")

#**  TASK --01 "THE AGE IN 2030 IN CALCULATOR"

name=input("enter the name   :")
age=int(input("enter the current age :  "))
age_2030=4 + age
print(f"Hii {name},you will be {age_2030} years old in 2030")

#**  TASK --02 "THE BILL SPLITER"
Amount = float(input("Enter the Total Bill Amount : "))
People =int(input("Enter the number of the peoples : "))
share=Amount/People
print(f'Total Bill : {Amount}. Each person pays: {share:.2f}')

#**  TASK --03 "THE ROW DATA FORMATTER"

item_name="Mobile"
quantity=4
price=2999.99
in_stock=True

print("item:",item_name,", Qty:",quantity,", Price:",price,", Available:",in_stock)
total_cost=quantity*price
print("Total Cost: ",total_cost)




















