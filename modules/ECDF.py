import numpy as np 
import matplotlib.pyplot as plt 

def ECDF(data, x_label):
	data = data
	x_label = x_label
	n = len(data)
	x = np.sort(data)
	y = np.arange(1, n+1) / n 

	plt.figure(figsize=(11, 8))
	plt.grid(True)
	plt.scatter(x, y, s=80)
	plt.margins(0.05)
	plt.xlabel(str(x_label), fontsize=15)
	plt.ylabel('ECDF', fontsize=15)

	plt.show()