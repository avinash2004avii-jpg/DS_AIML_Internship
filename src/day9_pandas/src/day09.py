#TASK--1 THE PRODUCT CATALOG
import pandas as pd
products=pd.Series([700,150,300],index=["laptop","mouse","keyboard"])
print(products["laptop"])
print(products[["laptop","mouse"]])
print(products)

#TASK--2 the grade filter
import pandas as pd
grades=pd.Series([85,None,92,45,None,78,55])
print(grades.isnull())
print(grades.fillna(0))
scores=grades[grades>60]
print(scores)

#TASK--3 THE USERNAME FORMATTER
import pandas as pd
usernames=pd.Series(['Alica','bOB','Charlie_Data','daisy'])
print(usernames.str.strip())
print(usernames.str.lower())
print(usernames.str.contains("a"))
