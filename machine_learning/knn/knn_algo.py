#!/usr/bin/env python3
import numpy as np
import warnings
from collections import Counter
import pandas as pd
import random

def k_nearest_neighbors(data, predict, k=3):
	if len(data) >= k:
		warnings.warn('k is set to a value less than total voting groups')
	distances = []
	for group in data:
		for features in data[group]:
			euc_dist = np.linalg.norm(np.array(features) - np.array(predict))
			distances.append([euc_dist, group])

	votes = [i[1] for i in sorted(distances)[:k]]	
	vote_result = Counter(votes).most_common(1)[0][0]
	confidence = Counter(votes).most_common(1)[0][1] / k

	return vote_result, confidence

df = pd.read_csv("../datasets/breast-cancer-wisconsin.data.txt")
df.replace('?', -99999, inplace=True)
df.drop(['id'], axis=1, inplace=True)
# for some reason there are strings in some of the columns, probably due to '?'
# being used as a place holder for missing data
# To remedy this issue, change all values to type 'float' 
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size = 0.2
split = -int(test_size * len(full_data))
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:split]
test_data = full_data[split:]

for i in train_data:
	train_set[i[-1]].append(i[:-1])
for i in test_data:
	test_set[i[-1]].append(i[:-1])

correct = 0
total = 0
for group in test_set:
	for data in test_set[group]:
		vote, confidence = k_nearest_neighbors(train_set, data, k=5)
		if group == vote:
			correct += 1
		else:
			print(confidence)
		total += 1

print("Accuracy:", correct/total)

