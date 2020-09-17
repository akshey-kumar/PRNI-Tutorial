import mat73
import numpy as np

class Database:

    def __init__(self):
        data_set_no = 2
        data_dict = mat73.loadmat('NoStim_Data.mat')
        data  = data_dict['NoStim_Data']

        deltaFOverF_bc = data['deltaFOverF_bc'][data_set_no]
        derivatives = data['derivs'][data_set_no]
        NeuronNames = data['NeuronNames'][data_set_no]
        fps = data['fps'][data_set_no]
        States = data['States'][data_set_no]
        
        
        self.states = np.sum([n*States[s] for n, s in enumerate(States)], axis = 0).astype(int) # making a single states array in which each number corresponds to a behaviour
        self.state_names = [*States.keys()]
        self.neuron_traces = np.array(deltaFOverF_bc).T
        self.derivative_traces = derivatives['traces'].T
        self.neuron_names = np.array(NeuronNames, dtype=object)
        self.fps = fps

        f = open('readme.txt', 'r')
        self.DESCR = f.read()
        f.close()    
        '''
        #Sort the data according to the clustering dendogram (only for dataset 3, as of now)
        self.neuron_traces = self.neuron_traces[sort_indices]
        self.derivative_traces = self.derivative_traces[sort_indices]
        self.NeuronNames = self.NeuronNames[sort_indices]
        '''
        ## Creating dictionary of identified neurons and their indices
        #self.neuron_id = {}
        #for n, i in enumerate(self.NeuronNames):
        #    if type(i) == list:
        #        self.neuron_id[i[0]]=n
