from math import sqrt

plot1 = [1, 3]
plot2 = [2, 5]

def euc_dist(pt1, pt2):
	assert len(pt1) == len(pt2)
	s = [(pt1[i] - pt2[i])**2 for i in range(len(pt1))]
	dist = sqrt(sum(s))
	return dist 

dist = euc_dist(plot1, plot2)
print(dist)
