import h5py
import numpy as np



class EEGLAB():

    def __init__(self,eeglab_set_file):
        self.eeglab_set_file = eeglab_set_file
        self.EEG = h5py.File(self.eeglab_set_file,'r')['EEG']

        self.set_all()
    
    def set_setname(self):
        encoded_setname = self.EEG['setname']
        self.setname = ''.join([chr(encoding[0]) for encoding in encoded_setname])

    '''
        Issue with reading file name properly from EEGLAB set file
    '''
    def set_filename(self):
        encoded_filename = self.EEG['filename']
        self.filename = ''.join([chr(encoding[0]) for encoding in encoded_filename])

    def set_nbchan(self):
        self.nbchan = self.EEG['nbchan'][0][0]

    def set_trials(self):
        self.trials = self.EEG['trials'][0][0]

    def set_pnts(self):
        self.pnts = self.EEG['pnts'][0][0]

    def set_srate(self):
        self.srate = self.EEG['srate'][0][0]

    def set_xmin(self):
        self.xmin = self.EEG['xmin'][0][0]

    def set_xmax(self):
        self.xmax = self.EEG['xmax'][0][0]

    def set_times(self):
        self.times = [self.EEG['times'][t][0] for t in range(len(self.EEG['times']))]

    '''
        Does not work
    '''
    def set_data(self):
        pass


    def set_epochs(self):

        self.set_trials()
        
        epoch_structure = self.EEG['epoch']

        events_structure = epoch_structure['event']
        events_duration_structure = epoch_structure['eventduration']
        event_latency_structure = epoch_structure['eventlatency']
        event_type_structure = epoch_structure['eventtype']
        ur_event_structure = epoch_structure['eventurevent']

        python_epochs_structure = []

        for i in range(int(self.trials)):
            
            cur_epoch_events_indices = epoch_structure[events_structure[i][0]][()][:,0]
            cur_epoch_events_duration = epoch_structure[events_duration_structure[i][0]]
            cur_epoch_events_latency = epoch_structure[event_latency_structure[i][0]]
            cur_epoch_urevents = epoch_structure[ur_event_structure[i][0]]
            
            ur_events = [epoch_structure[cur_epoch_urevents[i][0]][0][0] for i in range(len(cur_epoch_urevents))]

            durations = [epoch_structure[dur[0]][0][0] for dur in cur_epoch_events_duration]
            latencies = [epoch_structure[latency[0]][0][0] for latency in cur_epoch_events_latency]
            
              
            cur_event_types = epoch_structure[event_type_structure[i][0]]

            decoded_event_types = [''.join([chr(char[0]) for char in epoch_structure[event_type[0]]]) for event_type in cur_event_types]

            cur_epoch = {
                'event': list(cur_epoch_events_indices),
                'eventlatency': latencies,
                'eventtype': decoded_event_types,
                'eventurevent': ur_events,
                'eventduration':durations
            }

            python_epochs_structure.append(cur_epoch)

            self.epoch = python_epochs_structure

    def set_event(self):

        events_structure = self.EEG['event']
        python_events_structure = []

        n_events = len(events_structure['type'])

        event_latencies = [events_structure[events_structure['latency'][i][0]][0][0] for i in range(n_events)]
        urevents = [events_structure[events_structure['urevent'][i][0]][0][0] for i in range(n_events)] 
        durations = [events_structure[events_structure['duration'][i][0]][0][0] for i in range(n_events)] 
        epoch = [events_structure[events_structure['epoch'][i][0]][0][0] for i in range(n_events)] 

        event_types = []
        
        for i in range(n_events):
            cur_encoded_event = events_structure[events_structure['type'][i][0]]
            cur_decoded_event = ''.join([chr(cur_encoded_event[j][0]) for j in range(len(cur_encoded_event))])

            event_types.append(cur_decoded_event)       

        python_events_structure = []

        for j in range(n_events):

            cur_event = {
                'latency': event_latencies[j],
                'type': event_types[j],
                'urevent': urevents[j],
                'duration': durations[j],
                'epoch': epoch[j]
            }

            python_events_structure.append(cur_event)

        self.event = python_events_structure

    def set_all(self):

        self.set_setname()
        self.set_filename()
        self.set_nbchan()
        self.set_trials()
        self.set_pnts()
        self.set_srate()
        self.set_xmin()
        self.set_xmax()
        self.set_times()
        self.set_data()
        self.set_epochs()
        self.set_event()

    



    