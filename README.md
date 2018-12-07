# Ece143-Project-BostonMarathon

Team Members:
* Chenghung Ma
* Lyu Jishi
* Roya Karimian
* Chih-Yen Lin

Whether you are a beginner to running or not, how to prevent yourself from  IT band syndrome or to break
your own personal best are always big issues for runners. 
By analyzing the datasets from Boston Marathon, one of the world’s best-known road racing 
events,we try to build a personal marathon pacer for you, as well as give insights to where these runners come
from and their characteristics.

[Data](https://www.kaggle.com/rojour/boston-results) 
The data contains information on finishers of the Boston Marathon from 2015, 2016 and 2017. 
It has information on  age, country and state of origin of the runners, plus their times at 5k intervals 
throughout the course.


We will try to explore correlations by plotting and analysing different features of the data.
* Age demographic, influence on time (How the ages of runners affect their performance)
* Gender demographic
* Country and state demographic
* Pace in different phases and how can they affect the final performance
(How can the runners choose strategy to get best finish time.)


The data is in three files containing the runner's data (should be places in the current path)

marathon_results_2015.csv
marathon_results_2016.csv
marathon_results_2017.csv

And one .gpx data (also in the current path)

boston-marathon-course.gpx

Files to run:
* To get the splits chart: Splits.py
* To get the elevation chart: elevation.py

