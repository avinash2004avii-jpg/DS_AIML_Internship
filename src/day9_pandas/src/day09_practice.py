# intro to pandas
import pandas as pd
s1=pd.Series([40,30,20])
s2=pd.Series([90,80,70],index=["a","b","c"])
print(s1)
print(s2)

#indexing and section in series
marks=pd.Series([80,90,95],index=["maths","physics","chemistry"])
print(marks)
print(marks["maths"])
print(marks[["maths","chemistry"]])

#BOOLEAN MASKING
score=pd.Series([55,60,76,55,80,22,78])
passed=score[score>60]
print(passed)

#handling missing data
data=pd.Series([20,30,None,50,None,None])
print(data.isnull())
print(data.fillna(6.6))

#vectorized srting operation
names=pd.Series(["Alice","bob","CHARLIE"])
print(names.str.lower())
print(names.str.contains("a"))


