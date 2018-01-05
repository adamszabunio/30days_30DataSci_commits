# Object Oriented Programming (OOP)

### In this directory, I code up the same algorithms from the [Machine Learning Directory](../) into Python Classes.

- K-Nearest Neighbors (KNN). (DAY 4)
    + [KNN](knn.py) makes a prediction for the uci ml [breast cancer database](../datasets/citation.txt)
        + However, this Class was designed to generalize to any dataset (i.e. any # of features and classes).
        + This Class fits a training set of features and associated class.
        + The "fit" method and returns a dictionary of class membership
        + The "predict" method uses this membership dictionary with a predefined "distance"  metric to return the majority vote of the "k" nearest neighbors as well as the confidence of each predicition.
            + A confidence of "1.0" indicates homogenous "k" nearest neighbors.


- Support Vector Machines (SVM). (DAY 2) 
    + For the first OOP exercise I follow parts 20 - 28 of the Machine Learning tutorials from the [sentdex youtube channel](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ) and build a [SVM](svm.py) from scratch.
    + This tutorial focuses on the process of how support vectors and decison boundaries are optimized for classifying linear data.
        + While watching the videos, I followed his code (with a few small changes and annotations). 
        + At the final stages, the algorithm was misfiring. At first, I thought it was my additions and deletions.
        + *After some debugging (besides the usual mispelings), I discovered the problem came from TABS. (DAY 3)
        + As an added challenge (to the 30Days 30Commits challenge), I chose to only use [vim](https://github.com/vim/vim) as a text editor.
            + This was in part a personal goal so that I may (eventually) complete work faster from the command line.
            + And also because all other more sophisticated editors were slowing down my machine more than I would like.
        + To make life easier down the road, I researched how to customize vimrc files (runtime configurations) to avoid future TAB issues.
            + HT to [Amix](https://github.com/amix/vimrc/) for creating some beautiful vimrc files.
            + Currently using Amix's [Basic vimrc](https://github.com/amix/vimrc/blob/master/vimrcs/basic.vim). I have also included the [vimrc file here](basic.vim).
                + *These configurations solve the tab issue I was facing earlier. Now TAB == 4 spaces. 
