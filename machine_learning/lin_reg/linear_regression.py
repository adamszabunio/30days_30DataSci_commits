#! usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

#xs = np.arange(1,7, dtype=np.float64)
#ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

def create_dataset(n, var, step=2, corr=False):
	'''corr: 'pos' or 'neg'''
	val = 1
	ys = []
	for i in range(n):
		y = val + np.random.randint(-var, var+1)
		ys.append(y)
		if corr	== 'pos':
			val += step
		elif corr == 'neg':
			val -= step
	xs = [i for i in range(n)]  
	return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_slope_intercept(xs, ys):
	numer = np.mean(xs)*np.mean(ys) - np.mean(xs*ys)
	denom = np.mean(xs)**2 - np.mean(xs**2)
	m = numer/denom
	b = np.mean(ys) - m * np.mean(xs)
	return m, b

def squared_error(ys_orig, ys_line):
	return sum((ys_line - ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_line):
	y_mean_line = [np.mean(ys_orig) for _ in ys_orig]
	squared_error_reg = squared_error(ys_orig, ys_line)
	squared_error_y_mean  = squared_error(ys_orig, y_mean_line)
	return 1 - (squared_error_reg / squared_error_y_mean)


xs, ys = create_dataset(40, 20, 2, corr='pos')

m, b = best_fit_slope_intercept(xs, ys)

regression_line = [m*x + b for x in xs]

r_squared = coefficient_of_determination(ys, regression_line)

print("m: ", m, "\nb: ", b, "\nr2: ", r_squared) #, regression_line)

# predictions from first pass (manually created xs and ys)
predict_x1 = 4.5
predict_x2 = 8

predict_y1 = m*predict_x1 + b 
predict_y2 = m*predict_x2 + b

plt.plot(xs, regression_line)
plt.scatter(xs, ys)
plt.scatter([predict_x1, predict_x2], [predict_y1, predict_y2], s=100, c='r')
plt.show()
