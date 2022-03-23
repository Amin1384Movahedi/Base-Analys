import matplotlib.pyplot as plt 
import seaborn as sb 
import scipy

def spearman_rank_func(x_data, y_data, x_label, y_label):
	spearmanr, _ = scipy.stats.spearmanr(x_data, y_data)

	return spearmanr
def pearson_correlation(data):
	corr = data.corr()
	print(corr)

# Correlation plot doesn't end up being too informative

def plot_corr(df, size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.
    
    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of plot'''
    
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    cax = ax.matshow(corr)
    fig.colorbar(cax)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
    plt.yticks(range(len(corr.columns)), corr.columns)
    
    plt.show()