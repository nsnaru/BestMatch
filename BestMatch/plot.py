###
# BestMatch: Plot
###

import matplotlib.pyplot as plt

# Can only accept two keys, being a 2D plot.
def plot_best(dict_list, dict_list_ref, keys, n):
    x = [float(row[keys[0]]) for row in dict_list]
    y = [float(row[keys[1]]) for row in dict_list]

    fig, ax = plt.subplots()

    # All points.
    ax.scatter(x,
               y,
               color='lightgray',
               label=f'Top {len(dict_list) - n} by proximity'
    )
    # Top n points.
    ax.scatter(
        x[0:n],
        y[0:n],
        color='tab:red',
        label=f'Top {n} by proximity'
    )
    # Reference point.
    ax.scatter(
        dict_list_ref[keys[0]],
        dict_list_ref[keys[1]],
        color='yellow',
        label=f'Reference Point'
    )

    ax.set_xlabel(keys[0].capitalize())
    ax.set_ylabel(keys[1].capitalize())
    ax.set_title('Closest to the Reference')
    ax.legend()

    return fig, ax

def show():
    plt.show()
