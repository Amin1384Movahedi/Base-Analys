import matplotlib.pyplot as plt 
import seaborn as sb 
import scipy

def spearman_rank_func(x_data, y_data, x_label, y_label):
	spearmanr, _ = scipy.stats.spearmanr(x_data, y_data)

	return spearmanr
def pearson_correlation(data):
	corr = data.corr()
	print(corr)

	# seaborn for visualize pearson correlation coefficient
	plt.figure(figsize=(11, 8))
	sb.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, vmin=-1, vmax=+1)
	plt.show()