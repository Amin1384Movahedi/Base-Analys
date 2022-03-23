'''
Created on 2022-01-24
Updated on 2022-03-23 (add some methods for improve analysis results)

Author: Mohammad Amin Movahedi Moghadam
Email: antonio1384minkowski@zohomail.eu
'''

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sb 
import random
from tabulate import tabulate
from modules.correlation import spearman_rank_func, pearson_correlation, plot_corr
from modules.ECDF import ECDF
from modules.LinearRegression import linear_model
from modules.null_checker import null_checker
from modules.unique_values import unique_values

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

	print(f'\n{data.info()}')

def DataFrame_Summarize(data):
	# Summarize our dataset
	print('\nRows           : ', data.shape[0])
	print('Columns        : ', data.shape[1])
	print('\nFeatures       : ', data.columns.tolist())
	print('\nMissing values : ', data.isnull().sum().values.sum())
	print('\nUnique Values  : ', data.nunique(), '\n')

def list_of_binary_columns(data):
	# Binary columns with 2 values
	bin_cols = data.nunique()[data.nunique() == 2].keys().tolist()
	if len(bin_cols) != 0:
		print(f'\nList of columns with Binary values:\n')
		for col in bin_cols:
			print(col)

		print('')

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
	DataFrame_Summarize(data)
	unique_values(data)
	null_checker(data)
	pearson_correlation(data)
	plot_corr(data)
	spearman_rank(data)
	list_of_binary_columns(data)
	plot_linear_regression(data)