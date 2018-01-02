#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import warnings
from collections import Counter

plt.style.use("fivethirtyeight")

# test data
dataset = {'g': [[1,2], [2,3], [3,1]], 
	   'r': [[6,5], [7,7], [8,6]]}

new_features = [5,7] 

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

	return vote_result

result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)

# plot data
[[plt.scatter(j[0], j[1], s=100, c=i) for j in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], s=100, c=result, marker='+') 
plt.annotate('prediction',  np.array(new_features)-0.5)
plt.show()
