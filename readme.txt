---------------------------------------------------------------------
Neuronal and behavioural data analysis with machine learning methods
---------------------------------------------------------------------

This repository was created as part of the Pattern Recognition in Neuroimaging (PRNI) Virtual Summer School 2020 for teaching purposes. The tutorial shows how to analyze neuronal and behavioural data using machine learning techniques. You will see how a combination of agglomerative clustering and PCA can yield powerful visualisations of the data that help us draw insights on the relationship between behaviour and neuronal activity.

--------------------------------------
Calcium Imaging Datset from C. elegans
--------------------------------------

The following dataset is part of the published work, Kato et al. 2015, Global Brain Dynamics Embed the Motor Command Sequence of Caenorhabditis elegans, https://doi.org/10.1016/j.cell.2015.09.034.

------------------------------
Attributes of class 'Database' 
------------------------------
fps: volume acquisition rate

neuron_names: It contains an array of names for neurons in the given dataset. Unidentified neurons are represented by a number.

neuron_traces: It contains the original neurons traces (fluorescent change in GCaMP) of the recordings stored as a numpy array with shape (number of neurons) * (number of time frames).

derivative_traces: It contains the time derivatives of the same neurons traces stored as a numpy array with shape (number of neurons) * (number of time frames). The derivatives are calculated derivatives of detrTraces using total-variation regularization (Chartrand, R. (2011). Numerical Differentiation of Noisy, Nonsmooth Data. ISRN Applied Mathematics, 2011,  (1-4), 1-11. http://doi.org/10.1152/ajpregu.00055.2010)

states: It contains the designated behavioural brain state of the worm for each time slice and is of length (number of time frames). It has have been inferred using 4 neurons: AVA, SMDV, SMDD and RIB which are seen to be perfectly correlated with the behaviours in a free-moving worm. The brain state can take one of eight values of which,

0 is Dorsal turn
1 is Forward
2 is No state  
3 is Reverse-1
4 is Reverse-2
5 is Sustained reverse
6 is Slowing
7 is Ventral turn

where 2 represents 'No state' and is used to mark very few frames where the brain state cannot be deduced.

state_names: It contains the names corresponding to the eight possible states as above.

