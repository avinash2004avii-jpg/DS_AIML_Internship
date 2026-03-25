import pandas as pd
data = {
    "House_ID": [1,2,3,4,5,6,7,8,9,10],
    "City": ["Mumbai","Delhi","Mumbai","Chennai","Delhi",
             "Mumbai","Chennai","Delhi","Mumbai","Chennai"],
    "Price": [250000,270000,300000,320000,350000,
              360000,400000,420000,450000,900000]
}
# to create csv file
df = pd.DataFrame(data)
df.to_csv('housingg.csv')



