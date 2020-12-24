import cdflib
import os
from collections.abc import Mapping

class ReadOnlyCDF(Mapping):
    """Mapping abstract base class defines a read-only dictionary"""
    def __init__(self,cdf_filename):
        self.cdf = cdflib.cdfread.CDF(cdf_filename)
        self.cdf_filename = os.path.realpath(cdf_filename)
        self._keys = self._get_var_names()

    def _get_var_names(self):
        """Find out what variables are in the CDF"""
        cdfinfo = self.cdf.cdf_info()
        names = []
        for cdfvarname in cdfinfo['rVariables']:
            names.append(cdfvarname)
        for cdfvarname in cdfinfo['zVariables']:
            names.append(cdfvarname)
        return names

    def _extract_epoch(self):
        """Extract the timestamps (Epoch) variable from a CDF file as
        a numpy array of datetime objects"""
        cdftime = self.cdf.varget('Epoch')
        
        #The Epoch variable data can either be a numpy
        #float array (if the CDF epoch type is CDF_EPOCH)
        #or a numpy complex array (if the CDF epoch type is CDF_EPOCH_16)
        epoch_info = self.cdf.varinq('Epoch')
        epoch_type = epoch_info['Data_Type_Description']
        if epoch_type!='CDF_EPOCH':
            print('Epoch type is {}'.format(epoch_type))
            
        #cdflib.cdfepoch is another name for cdflib.epochs.CDFEpoch
        #which is a container class
        
        #The to_datetime method converts an epoch's numerical representation
        #to a Python datetime
        
        #the to_np switch toggles whether a list (False) or numpy array (True)
        #of datetimes is returned. I return an array since that
        #is what pycdf does.
        dtimes = cdflib.cdfepoch().to_datetime(cdftime,to_np=True)
        return dtimes

    def __str__(self):
        keystr = '\n'.join([key for key in self])
        return 'CDF File {} with variables:\n{}'.format(self.cdf_filename,keystr)

    def __len__(self):
        return self._keys.__len__()

    def __contains__(self,key):
        return self._keys.__contains__(key)

    def __iter__(self):
        return self._keys.__iter__()

    def __getitem__(self,key):
        if key == 'Epoch':
            return self._extract_epoch()
        else:
            return self.cdf.varget(key)
