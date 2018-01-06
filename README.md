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
		+ [Support Vector Machines (SVM)](machine_learning/oop/svm.py) (Day 2).
        + *Debugging of the SVM class (Day 3).
            + The issue was due to TAB width inconsistency. 
            + Was remedied by setting a custom vimrc (configuration).
            + More detailed explanation can be found in the [Object Oriented Programming directory](machine_learning/oop/).
        + [K-Nearest Neighbors (KNN)](machine_learning/oop/knn.py) (Day 4).
            + This class makes a prediction for the UCI Machine Learning [Breast Cancer Dataset](machine_learning/datasets/citation.txt).
    + After implementing KNN as a class, my mind returned to a spatial project, [[Yield Imputations](https://github.com/adamszabunio/yield_imputations)], that I put on hold for the holidays.
        + This was my final project during the last month of a Data Science internship with [Granular](www.granular.ag).
        + The goal of the project was to explore a variety of techniques to impute missing data, with spatial methods producing some of the best results. Specifically, the Ball Tree algorithm. The sklearn implementation was used to quickly build distance matrices for the project.
        + An example of how I used the Ball Tree algorithm for the yield imputations project can be found [here (python Class)](https://github.com/adamszabunio/yield_imputations/blob/master/spatial_lookup.py) and a [1000 Bootstrap sample test](https://github.com/adamszabunio/yield_imputations/blob/master/bootstrapping.py) (Day 6).
