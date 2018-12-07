
'''
This code analyses the splits
(the difference between the second half and the first half)
Roya Karimian
It uses three data files in the current path:

marathon_results_2015.csv
marathon_results_2016.csv
marathon_results_2017.csv

It produces two .png files. 
'''
import csv
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data2015 = pd.read_csv('marathon_results_2015.csv')
data2016 = pd.read_csv('marathon_results_2016.csv')
data2017= pd.read_csv("marathon_results_2017.csv")


timeData2015 = data2015[['Bib','Age','M/F','Half', 'Official Time', 'Overall']]
timeData2016 = data2016[['Bib','Age','M/F','Half', 'Official Time', 'Overall']]
timeData2017 = data2017[['Bib','Age','M/F','Half', 'Official Time', 'Overall']]

# Clean the Half column (removing the cells that contain illegal character)
timeData2015 = timeData2015[ ~ timeData2015['Half'].str.contains('-')]
timeData2016 = timeData2016[ ~ timeData2016['Half'].str.contains('-')]
timeData2017 = timeData2017[ ~ timeData2017['Half'].str.contains('-')]

# Clean the Oficial column (removing the cells that contain illegal character)

timeData2015 = timeData2015[ ~ timeData2015['Official Time'].str.contains('-')]
timeData2016 = timeData2016[ ~ timeData2016['Official Time'].str.contains('-')]
timeData2017 = timeData2017[ ~ timeData2017['Official Time'].str.contains('-')]


# Change type to timedelta
timeData2015['Official Time']= pd.to_timedelta(timeData2015['Official Time'])
timeData2015['Half']= pd.to_timedelta(timeData2015['Half'])
timeData2016['Official Time']= pd.to_timedelta(timeData2016['Official Time'])
timeData2016['Half']= pd.to_timedelta(timeData2016['Half'])
timeData2017['Official Time']= pd.to_timedelta(timeData2017['Official Time'])
timeData2017['Half']= pd.to_timedelta(timeData2017['Half'])

# Compute the time it took to finish second half
timeData2015['Second Half']=timeData2015['Official Time']-timeData2015['Half']
timeData2016['Second Half']=timeData2016['Official Time']-timeData2016['Half']
timeData2017['Second Half']=timeData2017['Official Time']-timeData2017['Half']


# The difference between Second half and First Half
timeData2015['Split Diff']=timeData2015['Second Half'].dt.total_seconds()-timeData2015['Half'].dt.total_seconds()
timeData2016['Split Diff']=timeData2016['Second Half'].dt.total_seconds()-timeData2016['Half'].dt.total_seconds()
timeData2017['Split Diff']=timeData2017['Second Half'].dt.total_seconds()-timeData2017['Half'].dt.total_seconds()

#If the second half is less (faster) it's a negative split
timeData2015['negative']=timeData2015['Split Diff']<0
timeData2016['negative']=timeData2016['Split Diff']<0
timeData2017['negative']=timeData2017['Split Diff']<0


#Divid all the runners based on their overall rank to 10 bins.
N=timeData2015['Overall'].max()
bins=(range(0,110,10)*N)/100
labels=range(10,110,10)
timeData2015['binned'] = pd.cut(timeData2015['Overall'], bins=bins, labels=labels)
N=timeData2016['Overall'].max()
bins=(range(0,110,10)*N)/100
labels=range(10,110,10)
timeData2016['binned'] = pd.cut(timeData2016['Overall'], bins=bins, labels=labels)
N=timeData2017['Overall'].max()
bins=(range(0,110,10)*N)/100
labels=range(10,110,10)
timeData2017['binned'] = pd.cut(timeData2017['Overall'], bins=bins, labels=labels)

#Calculate how many achieved a negative split in each bin
df2015=timeData2015.groupby(['binned'])['negative'].value_counts()
df2016=timeData2016.groupby(['binned'])['negative'].value_counts()
df2017=timeData2017.groupby(['binned'])['negative'].value_counts()

#Prepare x, y vectors to be plotted
x2015=[]
y2015=[]
for key,value in df2015.items():
    b, t = key
    if t == True:
        x2015.append(b)
        y2015.append(value)
x2016=[]
y2016=[]
for key,value in df2016.items():
    b, t = key
    if t == True:
        x2016.append(b)
        y2016.append(value)
x2017=[]
y2017=[]
for key,value in df2017.items():
    b, t = key
    if t == True:
        x2017.append(b)
        y2017.append(value)


# Plot how many runners in each bin (their percentile based on rank)
# did a negative split

from matplotlib.pyplot import subplots
fig, ax = subplots()

ax.plot(x2015, y2015, label="2015")
ax.plot(x2016, y2016, label="2016")
ax.plot(x2017, y2017, label="2017")
ax.legend()

ax.set_xlabel("Rank Percentile")
ax.set_ylabel("Number with Negative Split")

# The result chart will be saved in a file
fig.savefig("split-rank.png",dpi=500)
fig.show()




#The difference between second half and first half calculated as percent
# The data is similar in each year so only 2015 is showm
timeData2015['percent'] = (timeData2015['Split Diff']*100)/timeData2015['Half'].dt.total_seconds()
timeData2015['percentInt']=np.rint(timeData2015['percent'])
#timeData2016['percent'] = (timeData2016['Split Diff']*100)/timeData2016['Half'].dt.total_seconds()
#timeData2016['percentInt']=np.rint(timeData2016['percent'])
#timeData2017['percentInt']=np.rint(timeData2017['percent'])

splitChart2015 = timeData2015['percentInt'].value_counts().rename_axis('split percent').reset_index(name='counts')
#splitChart2016 = timeData2016['percentInt'].value_counts().rename_axis('split percent').reset_index(name='counts')
#splitChart2017 = timeData2017['percentInt'].value_counts().rename_axis('split percent').reset_index(name='counts')


fig, ax = subplots()
splitChart2015.plot.scatter(x='split percent',y='counts', color='r', ax=ax)
#splitChart2016.plot.scatter(x='split percent',y='counts', color='b', ax=ax)
#splitChart2017.plot.scatter(x='split percent',y='counts', color='g', ax=ax)

#The data is saved to a file
fig.savefig("percent-split.png",dpi=500)
