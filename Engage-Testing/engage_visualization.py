import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit


def fit_linear_model(x, y, res, m_offset, b_offset):
    # Define the objective function for the linear model: y = ax + b
    def objective(x, a, b):
        return a * x + b

    # Use curve fitting to find the optimal values of a and b that minimize
    # the difference between the predicted y values and the actual y values
    popt, _ = curve_fit(objective, x, y)
    a, b = popt  # a is the slope, b is the y-intercept

    a = a * (m_offset + 1)

    # Generate x values for the line of best fit: use the minimum and maximum x values
    x_line = np.asarray([np.min(x), np.max(x)])

    # Calculate the residuals (difference between actual y values and predicted y values)
    # This is used to adjust the y-intercept for the lower bound line

    b_values = y - np.multiply(a, x)

    # Calculate the 5th percentile of the residuals to determine the lower bound
    lower_b = np.percentile(b_values, res) + b_offset

    # Calculate the y values for the lower bound line using the adjusted y-intercept
    lower_line = objective(x_line, a, lower_b)

    # Create a label for the plot with the equation of the lower bound line
    label = f'y={a:.4f}x+{lower_b:.4f}'

    return a, lower_b, x_line, lower_line, label


def create_scatter_plot(
    x,
    y,
    x_line,
    lower_line,
    label,
    title,
    xlabel,
    ylabel,
    color_map,
    unique_prod_wells,
    unique_inj_wells,
    unique_depth,
    df,
):
    plt.figure()
    for i, val in enumerate(unique_depth):
        mask = df['Depth (m)'] == val
        plt.scatter(x[mask], y[mask], color=color_map(i / len(unique_depth)), label=val, s=4)
    plt.plot(x_line, lower_line, '--', color='red', label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Set the limits for the x and y axes
    plt.xlim(left=0)  # This ensures the x-axis starts at 0
    plt.ylim(bottom=0)  # This ensures the y-axis starts at 0

    plt.legend(handles=[plt.plot([], [], color='red', ls='--', label=label)[0]])


# Function to save plots to a PDF
def save_image(filename, fig_nums):
    p = PdfPages(filename)
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(p, format='pdf')
    p.close()
