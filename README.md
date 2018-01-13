# 30 days 30 DataScience commits
### This repository is a 30 Days, 30 Commits Challenge. 
- Having just finished an accelerated Master's of Data Science, I am using this challenge to review a years worth of Data Science.
- I started this project on January 1st, 2018 as a New Year's resolution. 30 days seemed fitting to match the average life expectancy of New Year's resolutions.
- To start, I jump right in with a refresher of Machine Learning. 
+ In the [Machine Learning directory](machine_learning/): 
	+ Algorithms from scratch: 
		+ [Linear Regression](machine_learning/lin_reg/) (Day 1).
		+ [KNN (K-Nearest Neighbors)](machine_learning/knn/) (Day 1).
		+ [Support Vector Machines](machine_learning/svm/) (Day 2).
	+ [Object Oriented Programming](machine_learning/oop/) Implementing the Above Algorithms as a Python Class:
        + [Linear Regression](machine_learning/oop/linregclass.py) (Day 7).
		+ [Support Vector Machines (SVM)](machine_learning/oop/svm.py) (Day 2).
        + *Debugging of the SVM class (Day 3).
            + The issue was due to TAB width inconsistency. 
            + Was remedied by setting a custom vimrc (configuration).
            + More detailed explanation can be found in the [Object Oriented Programming directory](machine_learning/oop/).
        + [K-Nearest Neighbors (KNN)](machine_learning/oop/knn.py) (Day 4).
            + This class makes a prediction for the UCI Machine Learning [Breast Cancer Dataset](machine_learning/datasets/citation.txt).

- After implementing KNN as a class, my mind returned to a spatial project, [Yield Imputations](https://github.com/adamszabunio/yield_imputations), that I put on hold for the holidays.
    + This was my final project during the last month of a Data Science internship with [Granular](www.granular.ag).
    + The goal of the project was to explore a variety of techniques to impute missing data, with spatial methods producing some of the best results. Specifically, the Ball Tree algorithm. The sklearn implementation was used to quickly build distance matrices for the project.
    + An example of how I used the Ball Tree algorithm for the yield imputations project can be found [here (python Class)](https://github.com/adamszabunio/yield_imputations/blob/master/spatial_lookup.py) (Day 5) 
    + I continued analysis of the [1000 Bootstrap samples](https://github.com/adamszabunio/yield_imputations/blob/master/bootstrap/) (Day 6).
    + Complete overhaul of the Yield Imputations Repo (Day 8).

- Another repository that needed some cleaning and resuscitation, [ShakeShakeShake](https://github.com/adamszabunio/ShakeShakeShake), is my final project for the Data Engineering class (back in March and April of 2017). 
    + Since I was already practicing one of my biggest interests for the Yield Imputations project, spatial analysis, I thought it would be wise to work on both of these projects simultaneously. 
    + [ShakeShakeShake](https://github.com/adamszabunio/ShakeShakeShake) is an end-to-end pipeline that queries all earthquakes recorded by [UGGS.gov](https://earthquake.usgs.gov) daily. 
    + The overarching goal of the project is to compare daily earthquakes in two locations, California and Oklahoma.
    + At the moment, state "boundaries" are determined by using the max/min latitude and longitude (rectangular) coordinates for each state.
    + To address this problem, I need to efficiently query more precise boundaries using polygons. To that end, Geopandas stands out as a promising soultion. 
    + First, I needed to upgrade the EC2 instance so that I could install Geopandas and its necessary geopsatial dependencies (Day 9).
    + Switching gears, I am experimenting with Django Geos in place of Geopandas (Day 10).
    + Reformatting the earthquake database to query Points in Polygons using Django (Day 11).
    + Reading in shapefiles using geodjango (Day 12).
    + postgresql database
