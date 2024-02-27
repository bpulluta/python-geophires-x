import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit
from scipy.optimize import minimize


def fit_lower_bound(x, y, percentile):
    # Sort the data by x and get the lower percentile of y for each x
    indices = x.argsort()
    x_sorted = x[indices]
    y_sorted = y[indices]

    # Define the objective function for the linear model: y = ax + b
    def objective(x, a, b):
        return a * x + b

    # Define an error function that will be minimized
    def error_function(params):
        a, b = params
        fitted_line = objective(x_sorted, a, b)
        # Error is a combination of distance to the lower percentile points and the y-intercept
        return np.sum((fitted_line - y_sorted) ** 2) + b**2

    # Initial guess for parameters a and b
    initial_guess = [0, 0]

    # Perform the minimization
    result = minimize(error_function, initial_guess)

    # Extract the optimized parameters
    a_opt, b_opt = result.x

    # Calculate the residuals and find the lower bound threshold
    residuals = y_sorted - objective(x_sorted, a_opt, b_opt)
    threshold = np.percentile(residuals, percentile)

    # Adjust the y-intercept to the lower bound threshold
    b_lower_bound = b_opt + threshold

    # Generate x values for the line of best fit
    x_line = np.asarray([np.min(x), np.max(x)])

    # Calculate the y values for the lower bound line
    lower_line = objective(x_line, a_opt, b_lower_bound)

    # Create a label for the plot
    label = f'y={a_opt:.4f}x+{b_lower_bound:.4f}'

    return a_opt, b_lower_bound, x_line, lower_line, label


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
    unique_temp,
    df,
):
    fig, ax = plt.subplots()  # Create a figure and an axes.

    # Normalize the color map based on the range of temperatures
    norm = mcolors.Normalize(vmin=min(unique_temp), vmax=max(unique_temp))

    for val in unique_temp:
        mask = df['Average Production Temperature (degC)'] == val
        ax.scatter(x[mask], y[mask], color=color_map(norm(val)), s=4)

    # Plot the trend line
    ax.plot(x_line, lower_line, '--', color='red', label=label)

    # Add labels and title
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Set the limits for the x and y axes
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)

    # Add faint grid lines with 50% transparency
    ax.grid(True, which='both', color='gray', linewidth=0.5, linestyle='-', alpha=0.5)

    # Create the colorbar
    sm = plt.cm.ScalarMappable(cmap=color_map, norm=norm)
    sm.set_array([])  # This line is necessary for ScalarMappable.
    cbar = fig.colorbar(sm, ax=ax, pad=0.01)  # Create a colorbar by specifying the axes
    cbar.set_label('Average Production Temperature (degC)', rotation=270, labelpad=15)

    # Add the trend line equation as text on the plot with a box around it
    ax.text(
        0.05,
        0.95,
        label,
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        color='red',
        bbox={'facecolor': 'white', 'alpha': 1, 'edgecolor': 'black', 'boxstyle': 'round,pad=0.5', 'linewidth': 1},
    )


# Function to save plots to a PDF
def save_image(filename):
    p = PdfPages(filename)
    # Save all plots to a PDF
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(p, format='pdf')
    p.close()
