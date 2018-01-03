#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

class Support_Vector_Machine():
	def __init__(self, visualization=True):
		self.visualization = visualization 
		self.colors = {1:'r', -1:'b'}
		if self.visualization:
			self.fig = plt.figure()
			self.ax = self.fig.add_subplot(1,1,1)
	#training
	def fit(self, data):
		self.data = data
		# { ||w||: [w, b]}
		opt_dict = {}

		transforms = [[1,1], [-1,1], [-1,-1], [1,-1]]
		
		# merge all data into one list
		all_data = []
		for yi in self.data:
			for featureset in self.data[yi]:
				for feature in featureset:			
					all_data.append(feature)

		self.max_feature_value = max(all_data)
		self.min_feature_value = min(all_data)
		all_data = None

		# support vectors yi(xi.dot(w) + b) = 1

		step_sizes = [self.max_feature_value * 0.1,
			      self.max_feature_value * 0.01,
			      # starts to get very expensive with very small steps
			      self.max_feature_value * 0.001]
		
		# also very expensive
		b_range_multiple = 5
		#
		b_multiple = 5
		# save a lot of time by cutting corners here
		latest_optimum = self.max_feature_value*10
			
		for step in step_sizes:
			w = np.array([latest_optimum, latest_optimum])
			# we can do this since it is a convex opt
			optimized = False
 
			while not optimized: 
				# note that we should be reducing step size for b in the same manner as w
				# instead, we cut another corner and set the b values range
				for b in np.arange(-1*(self.max_feature_value*b_range_multiple), #start 
							self.max_feature_value*b_range_multiple, #stop
							step*b_multiple): #step size
				
					for transformation in transforms:
						w_t = w*transformation
						found_option = True
						# weakesr link in the SVM fundamentally
						# SMO attempts to fix this a bit
						# yi(xi.dot(w) + b) >=1
						for yi in self.data:
							for xi in self.data[yi]:
								if not yi*(np.dot(w_t, xi)+b) >= 1:
									found_option = False

						if found_option:
							opt_dict[np.linalg.norm(w_t)] = [w_t, b]
				
					if w[0] < 0:
						optimized = True
						print('Optimized a step')
					else: 
						w = w - step

				norms = sorted([n for n in opt_dict])
				# ||w||: [w, b]
				opt_choice = opt_dict[norms[0]]
				self.w = opt_choice[0]
				self.b = opt_choice[1]
				latest_optimum = opt_choice[0][0] + step*2
			
			for i in self.data:
				for xi in self.data[i]:
					print(xi, ":", i*(np.dot(self.w, xi) + self.b))

	def predict(self, features):
		# sign(x.dot(w) + b) 
		classification = np.sign(np.dot(np.array(features), self.w) + self.b)
		if classification !=0 and self.visualization:
			self.ax.scatter(features[0], features[1], s=200, marker='*', c=self.colors[classification])
		else: 
			print("Featureset {} is on the decision boundary".format(features))

		return classification 
        
	def hyperplane_(self, x, w, b, v):
               	 return (-w[0]*x - b + v) / w[1]

	def visualize(self):
		#plotting known features self.data from fit method (data_dict)
		[[self.ax.scatter(x[0], x[1], s=100, color=self.colors[i]) for x in self.data[i]] for i in self.data]
		# hyperplane = x.dot(w) + b
		# v = x.w + b 
		# pos support vector = 1
		# neg support vector = -1
		# decision bound = 0
#		def hyperplane(x, w, b, v):
#			return (-w[0]*x - b + v) / w[1]

		data_range = (self.min_feature_value*0.9, self.max_feature_value*1.1)
		hyp_x_min = data_range[0]
		hyp_x_max = data_range[1]

		# (w.dot(x) + b) = 1
		# pos support vector hyperplane
		psv1 = self.hyperplane_(hyp_x_min, self.w, self.b, 1)
		psv2 = self.hyperplane_(hyp_x_max, self.w, self.b, 1)
		self.ax.plot([hyp_x_min, hyp_x_max], [psv1, psv2], 'k')

                # (w.dot(x) + b) = -1
                # neg support vector hyperplane
		nsv1 = self.hyperplane_(hyp_x_min, self.w, self.b, -1)
		nsv2 = self.hyperplane_(hyp_x_max, self.w, self.b, -1)
		self.ax.plot([hyp_x_min, hyp_x_max], [nsv1, nsv2], 'k')

             	# (w.dot(x) + b) = 0
                # decision boundary
		db1 = self.hyperplane_(hyp_x_min, self.w, self.b, 0)
		db2 = self.hyperplane_(hyp_x_max, self.w, self.b, 0)
		self.ax.plot([hyp_x_min, hyp_x_max], [db1, db2], 'y--')

		plt.show()

data_dict = {-1: np.array([[1,7], [2,8], [3,8]]), 
	      1: np.array([[5,1], [6,-1], [7,3]])}

svm = Support_Vector_Machine()
svm.fit(data=data_dict)

samples = [[0,10], [1,3], [3,4], [3,5], [5,5], [5,6], [6,-5], [5,8]]

for s in samples:
	svm.predict(s)

svm.visualize()
