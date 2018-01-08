#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

class UnivariateLinearRegression(object):
    '''TODO: Implement Normalization and generalize to Multivariate'''
    def __init__(self, xs, ys):
        self.xs = np.array(xs)
        self.ys = np.array(ys)

    def fit(self):
        numer = np.mean(self.xs)*np.mean(self.ys) - np.mean(self.xs*self.ys)
        denom = np.mean(self.xs)**2 - np.mean(xs**2)
        m = numer/denom
        b = np.mean(ys) - m*np.mean(xs)
        return m, b

    def predict(self, m, b, x_pred):
        y_pred = m * np.array(x_pred) + b
        return y_pred

    def sum_squared_error(self, y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        return sum((y_pred - y_true)**2)

    def rmse(self, y_true, y_pred):
        assert len(y_true) == len(y_pred)
        sse = self.sum_squared_error(y_true, y_pred)
        return np.sqrt(sse/len(y_true))

    def coefficient_of_determination(self, y_true, y_pred):
        y_mean_line = [np.mean(y_true) for _ in y_true]
        squared_error_reg = self.sum_squared_error(y_true, y_pred)
        squared_error_y_mean  = self.sum_squared_error(y_true, y_mean_line)
        return 1 - (squared_error_reg / squared_error_y_mean)


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


xs, ys = create_dataset(40, 20, 2, corr='pos')

model = UnivariateLinearRegression(xs, ys)

m, b = model.fit()
y_pred = model.predict(m, b, xs)

# metrics
rmse = model.rmse(ys, y_pred)
r_squared = model.coefficient_of_determination(ys, y_pred)

print("m: ", m, "\nb: ", b, "\nrmse: ", rmse, "\nr2: ", r_squared) #, regression_line)

# predictions from first pass (manually created xs and ys)
predict_x1 = 4.5
predict_x2 = 8

predictions = model.predict(m, b, [predict_x1, predict_x2])

plt.plot(xs, y_pred)
plt.scatter(xs, ys)
plt.scatter([predict_x1, predict_x2], predictions, s=100, c='r')
plt.show()
