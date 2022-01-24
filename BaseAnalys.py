import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sb 
import scipy
import random
from tabulate import tabulate
from modules.correlation import spearman_rank_func, pearson_correlation
from modules.ECDF import ECDF
from modules.LinearRegression import linear_model

def plot_ECDF(data):
	for i in data:
		type_of_data = str(type(data[str(i)][random.randint(0, len(data) - 1)]))
		if 'int' in type_of_data or 'float' in type_of_data:
			ECDF(data[str(i)], str(i))

def Describe_Dataset(data):
	dataset_describe = data.describe()
	print(dataset_describe)

	sb.pairplot(data)
	plt.show()

def spearman_rank(data):
	head = ['Variables', 'Spearman Correlation']
	values = []
	numeric_cols = []

	for col in data:
	    type_of_data = str(type(data[str(col)][random.randint(0, len(data) - 1)]))
	    if 'int' in type_of_data or 'float' in type_of_data:
	        numeric_cols.append(str(col))

	for i in range(len(numeric_cols)):
	    for j in range(1, len(numeric_cols)):
	        if i != j:
	            tmp = []
	            tmp.append(str(numeric_cols[i]) + str(numeric_cols[j]))
	            tmp.append(str(spearman_rank_func(np.array(data[str(numeric_cols[i])]), np.array(data[str(numeric_cols[j])]), str(numeric_cols[i]), str(numeric_cols[j]))))
	            values.append(tmp)

	print(tabulate(values, headers=head, tablefmt='grid'))

def plot_linear_regression(data):
	numeric_cols = []

	for col in data:
		type_of_data = str(type(data[str(col)][random.randint(0, len(data) - 1)]))
		if 'int' in type_of_data or 'float' in type_of_data:
			numeric_cols.append(str(col))

	for i in range(len(numeric_cols)):
		for j in range(1, len(numeric_cols)):
			if i != j:
				linear_model(np.array(data[str(numeric_cols[i])]), np.array(data[str(numeric_cols[j])]), str(numeric_cols[i]), str(numeric_cols[j]))

def get_report(data):
	plot_ECDF(data)
	Describe_Dataset(data)
	pearson_correlation(data)
	spearman_rank(data)
	plot_linear_regression(data)