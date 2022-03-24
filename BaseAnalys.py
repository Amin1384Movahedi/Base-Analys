'''
Created on 2022-01-24
Updated on 2022-03-23 (Added several methods to improve the analysis results) 

Author: Mohammad Amin Movahedi Moghadam from Yazd, Iran
Email: antonio1384minkowski@zohomail.eu
'''

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sb 
from tabulate import tabulate
from modules.correlation import spearman_rank_func, pearson_correlation, plot_corr
from modules.ECDF import ECDF
from modules.LinearRegression import linear_model
from modules.null_checker import null_checker
from modules.unique_values import unique_values

# This is a simple function for fixing the data types
def fix_data_types(data):
	return data.infer_objects()

# This is a function for extracting columns that have numeric values 
def numeric_column_extraction(data):
	return list(data.select_dtypes(include=[np.number]).columns.values)

# Drop null values from DataFrame for Linear Regression
def null_value_remover(data):
	data.dropna(inplace=True)
	for col in data.columns:
		data = data[data[col] != '?']
		data = data[data[col] != ' ?']
		data = data[data[col] != '? ']
		data = data[data[col] != ' ? ']

	return data

def plot_ECDF(data):
	print('================== ECDF plot ==================\n')
	# Apply the ECDF function on numeric columns
	for col in numeric_column_extraction(data):
		ECDF(data[col], col)

def Describe_Dataset(data):
	print('\n================== DataFrame Describe ==================\n')
	# Use pandas and seaborn pairplot to describe the DataFrame
	dataset_describe = data.describe()
	print(dataset_describe)

	sb.pairplot(data)
	plt.show()

	print(f'\n{data.info()}')

def DataFrame_Summarize(data):
	print('\n================== DataFrame Summarize ==================\n')
	# Summarize our dataset
	print('\nRows           : ', data.shape[0])
	print('Columns        : ', data.shape[1])
	print('\nFeatures       : ', data.columns.tolist())
	print('\nMissing values : ', data.isnull().sum().values.sum())
	print('\nUnique Values  : \n', data.nunique(), '\n')

def list_of_binary_columns(data):
	# Etract Binary columns with 2 values
	bin_cols = data.nunique()[data.nunique() == 2].keys().tolist()
	if len(bin_cols) != 0:
		print(f'\nList of columns with Binary values:\n')
		for col in bin_cols:
			print(col)

		print('')

def spearman_rank(data):
	head = ['Variables', 'Spearman Correlation']
	values = []

	# Extract numeric columns from DataFrame
	numeric_cols = numeric_column_extraction(data)

	# Apply the Spearman calculation on extracted values
	for i in range(len(numeric_cols)):
		for j in range(1, len(numeric_cols)):
			if i != j:
				tmp = []
				tmp.append(str(numeric_cols[i]) + str(numeric_cols[j]))
				tmp.append(str(spearman_rank_func(np.array(data[str(numeric_cols[i])]), np.array(data[str(numeric_cols[j])]), str(numeric_cols[i]), str(numeric_cols[j]))))
				if 'nan' not in tmp:
					values.append(tmp)

	# Print correlation values
	print(tabulate(values, headers=head, tablefmt='grid'))

def plot_linear_regression(data):
	# Extract numeric columns from DataFrame
	numeric_cols = numeric_column_extraction(data)

	# Apply the Linear Regression model on extracted values
	for i in range(len(numeric_cols)):
		for j in range(1, len(numeric_cols)):
			if i != j:
				linear_model(np.array(data[str(numeric_cols[i])]), np.array(data[str(numeric_cols[j])]), str(numeric_cols[i]), str(numeric_cols[j]))

def get_report(data):
	data = fix_data_types(data)
	plot_ECDF(data)
	Describe_Dataset(data)
	DataFrame_Summarize(data)
	unique_values(data)
	null_checker(data)
	pearson_correlation(data)
	plot_corr(data)
	spearman_rank(data)
	list_of_binary_columns(data)
	plot_linear_regression(null_value_remover(data))
