import pandas as pd
import numpy as np

row = ['Person1','Person2','Person3']
data = [['Vlad','Harutyunyan',50,'Armenia'],['Vlad','Harutyunyan',30,'Armenia'],['Vlad','Harutyunyan',20,'Armenia']]
col = ['Name','Surname','Age','Country']

df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

c1 = df.reset_index() #indexation , inplace=true for saving result
print(c1)

c2 = df.reset_index(level=0) 
print(c2)
c3 = c1.drop([0,2])
print(c3)
print(df.shape)
print(c2[c2['Age'] < 30])
df['Country'].replace({'Armenia':'Arm'},inplace=True)
print(df)