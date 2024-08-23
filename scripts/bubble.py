import matplotlib.pyplot as plt

def plot_bubble_chart(data, x_col, y_col, size_col, color_col, cmap, edgecolors, x_label=None, y_label=None, scale_factor=20, figsize=(10, 8)):
    plt.figure(figsize=figsize)
    
    # Create the bubble chart
    scatter = plt.scatter(
        data[x_col],                    # X-axis
        data[y_col],                    # Y-axis
        s=data[size_col] * scale_factor,  # Bubble size
        c=data[color_col],              # Color of bubbles
        cmap=cmap,                 # Color map
        alpha=0.6,                      # Transparency
        edgecolors=edgecolors,                 # Edge color
        linewidth=0.5
    )

    # Add color bar for the color dimension
    plt.colorbar(scatter, label=color_col)

    # Set chart title and labels
    plt.title(f'Bubble Chart: {x_col} vs. {y_col} vs. {color_col} with Bubble Size Representing {size_col}')
    plt.xlabel(x_label if x_label else x_col)
    plt.ylabel(y_label if y_label else y_col)

    # Show plot
    plt.show()
