import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(data, columns, figsize=(10, 8), cmap='coolwarm', linewidths=0.5, center=0, title='Correlation Heatmap'):
    # Calculate the correlation matrix
    corr_matrix = data[columns].corr()

    # Plotting the heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, annot=True, cmap=cmap, linewidths=linewidths, center=center)
    plt.title(title)
    plt.show()


def plot_pairplot(data, columns, title='Pair Plot', title_y=1.02):
    # Generate the pair plot
    sns.pairplot(data[columns])
    
    # Add the title
    plt.suptitle(title, y=title_y)
    
    # Show the plot
    plt.show()


def plot_scatter_matrix(data, columns, diag_kind='kde', title='Scatter Matrix', title_y=1.02):

    # Generate the scatter matrix
    sns.pairplot(data[columns], diag_kind=diag_kind)
    
    # Add the title
    plt.suptitle(title, y=title_y)
    
    # Show the plot
    plt.show()
