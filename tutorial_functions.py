import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D
from mpl_toolkits import mplot3d
from scipy.cluster.hierarchy import dendrogram


def plot_raster(neuron_traces, derivative_traces):
    fig, ax = plt.subplots(2,1, figsize=(15,10))
    plt0 = ax[0].imshow(neuron_traces, aspect="auto", vmin=0, vmax=1)
    #ax[0].set_yticks(np.arange(neuron_names.shape[0]))
    #ax[0].set_yticklabels(neuron_names)
    fig.colorbar(plt0, ax=ax[0])
    plt1 = ax[1].imshow(derivative_traces, cmap='seismic', aspect="auto", vmin=-0.25, vmax=0.25)
    #ax[1].set_yticks(np.arange(neuron_names.shape[0]))
    #ax[1].set_yticklabels(neuron_names)
    fig.colorbar(plt1, ax=ax[1])
    plt.show()


def dendogram(classifier):
    ## Dendogram
    # Create linkage matrix and then plot the dendrogram
    # create the counts of samples under each node
    counts = np.zeros(classifier.children_.shape[0])
    n_samples = len(classifier.labels_)
    for i, merge in enumerate(classifier.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count
    linkage_matrix = np.column_stack([classifier.children_, classifier.distances_, counts]).astype(float)
    # Plot the corresponding dendrogram
    R = dendrogram(linkage_matrix, truncate_mode='level')
    ## Sorting: The features are ordered according to the order of the leaves in the dendogram
    sort_indices = R['leaves']
    return sort_indices


def plot_phase_space(pca_neurons, states):
    fig = plt.figure(figsize=(8,8))
    ax = plt.axes(projection='3d')
    X = pca_neurons.T[:3]
    points = np.array(X).T.reshape(-1, 1, 3)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    colors = [*mcolors.TABLEAU_COLORS.keys()][:8]
    for segment, state in zip(segments, states[:-1]):
        p = ax.plot3D(segment.T[0], segment.T[1], segment.T[2], color=colors[state] )
    # Create legend
    state_names = ['Dorsal turn', 'Forward', 'No state', 'Reverse-1', 'Reverse-2', 'Sustained reverse', 'Slowing', 'Ventral turn']
    legend_elements = [Line2D([0], [0], color=c, lw=4, label=state) for c, state in zip(colors, state_names)]
    ax.legend(handles=legend_elements)
    plt.show()
