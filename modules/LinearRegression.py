from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

# Calculate Linear Regression by sklearn's model and plot the result by matplotlib
def linear_model(x, y, x_label, y_label):
	x = x.reshape((-1, 1))
	model = LinearRegression().fit(x, y)

	# Print the training results
	print(f'linear regression coefficient of determination : {model.score(x, y)}')
	print(f'intercept : {model.intercept_}')
	print(f'slope : {model.coef_}')

	y_pred = model.predict(x)

	plt.figure(figsize=(11, 8))
	plt.grid(True)
	plt.scatter(x, y)
	plt.plot(x, y_pred, c='red')
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.show()