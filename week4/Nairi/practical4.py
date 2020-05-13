import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import os 
from datetime import datetime as d

###########################
########problem1###########
###########################
data = [['Vlad','Harutyunyan',20,'student'],['Nairi','Hakobyan',30,'Tutor'],
        ['Vlad','Poghosyan',30,'Tutor'],['Ruzanna','Ordyan',99,'student'],
        ['Jora','Karyan',25,'student'],['Hayk','Sahakyan',25,'student'],
        ['Arthur','Mkrtchyan',20,'student'],['Sona','Kirakosyan',25,'student'],
        ['Lianna','Varosyan',20,'student'],['Salbina','Alaverdyan',25,'student'],
        ['Tathev','Alaverdyan',25,'student']]

col = ['name','surname','age','status','id_card']
row =  [x for x in range(len(data))]

for x in data:
    x.append(rd.randint(4214124,9898988) )
df1 = pd.DataFrame(data = data , columns=col,index = row)
print(df1)
df1 = df1.set_index('id_card')
print(df1)


###########################
########problem2###########
###########################
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'netflix_titles.csv')
df2 = pd.read_csv(initfile)
problem2 = (df2['release_year'] > 2014) & (df2['cast'].str.contains('Kevin Spacey') | (df2['cast'].str.contains('Leonardo DiCaprio')) )
print(df2[problem2])



###########################
########problem3###########
###########################
df3 = pd.read_csv(initfile)
directors = df3[df3['director'].notna()]
directors['count'] = directors.groupby(by='director')['director'].transform('count')
print(directors)

###########################
########problem4###########
###########################
df4 = pd.read_csv(initfile)
def split_cast(df, column, sep=',', keep=False):
    indexes = list()
    new_values = list()
    df = df.dropna(subset=[column])
    for i, presplit in enumerate(df[column].astype(str)):
        values = presplit.split(sep)
        if keep and len(values) > 1:
            indexes.append(i)
            new_values.append(presplit)
        for value in values:
            indexes.append(i)
            new_values.append(value)
    new_df = df.iloc[indexes, :].copy()
    new_df[column] = new_values
    return new_df  
newdf4 = split_cast(df4,'cast')
print(newdf4)


###########################
########problem5###########
###########################
df5 = pd.read_csv(initfile)
df5 = df5[df5['cast'].notna()]
p5 = (df5['cast'].str.contains('Antonio Banderas')) 
df5['duration'] = df5['duration'].apply(lambda x: int(x.split(' ')[0]))
res = df5[p5].sort_values(by='duration')
print(res)

###########################
########problem6###########
###########################
df6 = pd.read_csv(initfile)
df6['date_added'] = pd.to_datetime(df6['date_added'])
df6 = df6[df6['date_added'].notna()]
df6.sort_values('date_added',inplace=True)
times = df6['date_added']
cnt = 0 
startyear = 2008
infodata = {}
for x in times:
    if int(str(x).replace("00:00:00",'').split('-')[0]) == startyear:
        cnt+=1
        infodata[startyear] = cnt
    else :
        startyear += 1
        cnt = 0

f, ax = plt.subplots(figsize=(18,12)) 
ax.grid(zorder=0)
plt.bar([ str(i) for i in infodata.keys()], infodata.values(), width=0.3, align='center', color='skyblue', zorder=10)
plt.show()


###########################
########problem7###########
###########################
df7 = pd.read_csv(initfile)
df7['date_added'] = pd.to_datetime(df7['date_added'])
# 
# df7.sort_values('date_added',inplace=True)
df7 = df7[df7['date_added'].notna()]
df7['date_added'] = df7['date_added'].apply(lambda x:str(x).split(':')[0].split(' ')[0])
df7.reset_index(inplace=True)
df7['range'] = 0

for x in range(2,len(df7)):
        day1 = d.strptime(df7.date_added[x],"%Y-%m-%d")
        day2 = d.strptime(df7.date_added[x-1],"%Y-%m-%d")
        df7.at[x,'range'] = abs((day1-day2))
print(df7)

###########################
########problem8###########
###########################
df8 = pd.read_csv(initfile)
df8['date_added'] = pd.to_datetime(df8['date_added'])
df8 = df8[df8['date_added'].notna()]
directors = df8[df8['director'].notna()]
t = directors.sort_values(by='director')
t['range'] = 0
t['date_added'] = t['date_added'].apply(lambda x:str(x).split(':')[0].split(' ')[0])
t.reset_index(inplace=True)

for x in range(2,len(t)):
        day1 = d.strptime(t.date_added[x],"%Y-%m-%d")
        day2 = d.strptime(t.date_added[x-1],"%Y-%m-%d")
        t.at[x,'range'] = abs((day1-day2))
print(t)
