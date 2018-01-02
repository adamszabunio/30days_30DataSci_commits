import numpy as np
import pandas as pd
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split

df = pd.read_csv("../datasets/breast-cancer-wisconsin.data.txt")
df.replace("?", -99999, inplace=True)
df.drop(["id"], axis=1, inplace=True)

X = np.array(df.drop(["class"], axis=1))
y = np.array(df["class"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

# two ways to deal with reshaping errors 
# either make the prediction samples a list of lists
example_measures = np.array([[4,2,1,1,1,2,3,2,1]]) # unique sample DNE in dataset
# or
example_measures = np.array([[4,2,1,1,1,2,3,2,1], [4,2,1,2,1,2,3,2,1]])
# reshape your numpy array for predictions (for more than one sample)
# example_measures = example_measures.reshape(len(example_measures), -1)

prediction = clf.predict(example_measures)
print(prediction)
