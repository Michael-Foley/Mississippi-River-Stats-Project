import matplotlib
import matplotlib.pyplot as plt
import numpy as np

mississippi_data = np.array([
    23.9,
    24.5,
    24.7,
    24.4,
    24.6,
    26.1,
    24.8,
    25.1,
    25.1,
    24.7,
    24.5,
    24.8,
    24.9,
    24.9,
    24.8,
    24.6,
    24.5,
    24.6,
    25.0,
    24.6
])

graph_bins = np.arange(min(mississippi_data), max(mississippi_data), 0.1)
graph_range = (23.8, 26.2)
style = {'facecolor': 'gray', 'edgecolor' : 'black', 'linewidth' : 3}

def main() -> None:
    #plt.rcParams.update({'font.size' : 32})
    plt.rc('axes', titlesize=22)
    plt.rc('axes', labelsize=19)
    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)
    fig, ax = plt.subplots()
    ax.hist(mississippi_data, bins=graph_bins, range=graph_range, histtype='bar', align='mid', **style)
    ax.set_yticks(np.arange(0, 5))
    ax.set_xticks(np.arange(graph_range[0], graph_range[1], 0.2))
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Number of Data Points")
    ax.set_title("Mississippi River Temperature Data")
    plt.show()

if __name__ == "__main__":
    main()