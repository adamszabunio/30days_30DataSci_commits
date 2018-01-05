#!/usr/bin/env python3

from collections import Counter
import numpy as np
import pandas as pd

# define two distance metrics to be used when instantiating the KNearestNeighbors Class
def euclidean_distance(train, pred):
    a = np.array(train)
    b = np.array(pred)
   # return np.sqrt((a-b).dot(a-b)) # alternative, slightly slower. left it in for easy interpretation
    return np.linalg.norm(a - b)

def cosine_distance(train, pred):
    a = np.array(train)
    b = np.array(pred)
    mag = lambda x: x**2
    mag_a, mag_b = sum(mag(a)), sum(mag(b))
    return a.dot(b) / (mag_a * mag_b)

class KNearestNeighbors(object):
    '''
    This Class fits a training set of features and associated class in
    the "fit" method and returns a dictionary of class membership
    "predict" uses this membership dictionary with a predefined "distance"
    metric to return the majority vote of the "k" nearest neighbors as well
    as the confidence of each predicition. A confidence of "1.0" indicates
    homogenous "k" nearest neighbors.
    '''
    def __init__(self, k=3, distance=euclidean_distance):
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        self.classes, idx = np.unique(y, return_inverse=True)
        train_dict = {}
        for i, c in enumerate(self.classes):
            train_dict[c] = X[idx==i]
        return train_dict

    def predict(self, train_dict, test_set):
        predictions, confidences = [], []
        for i in test_set:
            distances = []
            for c in train_dict:
                for xi in train_dict[c]:
                    dist = self.distance(xi, i)
                    distances.append([dist, c])

            votes = [j[1] for j in sorted(distances)[:self.k]]
            vote_result = Counter(votes).most_common(1)[0][0]
            confidence = Counter(votes).most_common(1)[0][1] / self.k
            predictions.append(vote_result)
            confidences.append(confidence)

        return predictions, confidences

    def accuracy(self, true, pred):
        return sum(np.array(true) == np.array(pred)) / len(true)

# Using the breast cancer dataset from uci
df = pd.read_csv("../datasets/breast-cancer-wisconsin.data.txt")
df.replace('?', -99999, inplace=True)
df.drop(['id'], axis=1, inplace=True)
# for some reason there are strings in some of the columns, probably due to '?'
# being used as a place holder for missing data
# To remedy this issue, change all values to type 'float'
full_data = df.astype(float).values.tolist()

# another way to shuffle data besides random.shuffle(full_data)
perm = np.random.permutation(len(full_data))
Xy = np.array(full_data)[perm]
X = Xy[:, :-1]
y = Xy[:, -1]

test_size = 0.2
split = -int(test_size * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

clf = KNearestNeighbors()
class_dict = clf.fit(X_train, y_train)
pred, conf = clf.predict(class_dict, X_test)
print("Accuracy: {:.2f}%".format(clf.accuracy(y_test, pred)*100))
print("Confidences:", np.round(conf, 2))

for i in range(3, 33, 2):
    clf = KNearestNeighbors(k=i)
    class_dict = clf.fit(X_train, y_train)
    pred, conf = clf.predict(class_dict, X_test)
    print("Accuracy for {} neighbors: {:.2f}%".format(i, clf.accuracy(y_test, pred)*100))
