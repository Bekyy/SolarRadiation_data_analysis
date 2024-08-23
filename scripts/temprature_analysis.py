import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_rh_vs_variables(data, rh_col, variables, figsize=(10, 6)):
    for var in variables:
        plt.figure(figsize=figsize)
        sns.scatterplot(x=rh_col, y=var, data=data)
        plt.title(f'Relative Humidity vs {var}')
        plt.xlabel('Relative Humidity (%)')
        plt.ylabel(f'{var}')
        plt.show()


def linear_regression_rh_vs_variable(data, rh_col, target_col):
    # Prepare the data
    X = data[[rh_col]].values.reshape(-1, 1)
    y = data[target_col].values

    # Create and fit the model
    model = LinearRegression()
    model.fit(X, y)

    # Print the coefficient
    coefficient = model.coef_[0]
    print(f"Coefficient for {rh_col} vs {target_col}: {coefficient}")

    return model, coefficient

