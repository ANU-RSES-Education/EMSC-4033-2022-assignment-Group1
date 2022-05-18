import pytest
from src import my_functions

import matplotlib.pyplot as plt
import numpy as np

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt

from IPython.display import display_markdown
from matplotlib import cm

from cloudstor import cloudstor

from obspy.core import event
from obspy.clients.fdsn import Client
from obspy import UTCDateTime

"""   

This test_functions.py module contains all the tests to verify functions my_functions.py. 
The user needs to import pytest to use this module.  
In general, the test functions in this module tests each function in my_functions.py based in the following three ways, 
including: 

1) the existence of each function: exception will be raised if the function does not exist.  

2) the type of returned value: are they what we expect? e.g. cartopy NaturalEarth features, numpy arrays, lists etc.
TypeError or ValueError will be raised to better inform the user the type of the error.

3) the input parameters: is the type of an input parameter the one we expect? Where appropriate, is the value of the input parameter meaningful? e.g. is the input geographical coordinate within bounds?

"""

def test_my_coastline1 ():
    '''Verify the existence of my_coastlines.
       If True: function exists, pass. 
       If False: function does not exist, raise exception.  
    '''
    if my_functions.my_coastlines: 
        pass
    else:
        raise Exception ('my_coastlines function does not exist.')
        
def test_my_coastline2 ():
    '''Verify the returned value of my_coastlines.
       Assertion: 
       True: the output value is cartopy NaturalEarth feature.
       False: TypeError.  
    '''
    output1 = my_functions.my_coastlines('50m')
    assert type(output1) == cartopy.feature.NaturalEarthFeature, " TypeError "

def test_my_coastline3 (resolution = '110m'):
    '''Verify the input parameter of my_coastlines.
       Assertion: 
       True: the input parameter is a string AND one of '50m', '10m' or '110m'. 
       False: ValueError.  
    '''
    if resolution == "50m" or "10m" or "110m": 
        pass
    else: 
        raise Exception ("ValueError or TypeError, resolution must be a STRING value from '50m', '10m' or '110m'")


def test_my_water_features1 ():
    '''Verify the existence of my_water_features.
       If True: function exists, pass. 
       If False: function does not exist, raise exception.  
    '''
    if my_functions.my_water_features: 
        pass
    else:
        raise Exception ('my_water_features function does not exist.')
        
def test_my_water_features2 ():
    '''Verify the returned value of my_water_features.
       Assertion: 
       True: the output value is a list.
       False: TypeError.  
    '''
    output1 = my_functions.my_water_features('10m')
    assert type(output1) == list, " TypeError "

def test_my_water_features3 (resolution = '10m'):
    '''Verify the input parameter of my_water_features.
       Assertion: 
       True: the input parameter is a string AND one of '50m', '10m' or '110m'. 
       False: ValueError.  
    '''
    if resolution == "50m" or "10m" or "110m": 
        pass
    else: 
        raise Exception ("ValueError or TypeError, resolution must be a STRING value from '50m', '10m' or '110m'")

def test_my_water_features4 ():
    '''Verify the items inside the returned list of my_water_features.
       Assertion: 
       True: the item is a cartopy NaturalEarth features. 
       False: TypeError.  
    '''    
    water = my_functions.my_water_features ('10m')
    
    for water_features in water: 
        if type(water_features) == cartopy.feature.NaturalEarthFeature:
            pass
        else: 
            raise TypeError ("The item inside the list of my_water_features should be a cartopy NaturalEarth feature.")

def test_my_basemaps1 ():
    '''Verify the existence of my_basemaps.
       If True: function exists, pass. 
       If False: function does not exist, raise exception.  
    '''
    if my_functions.my_basemaps: 
        pass
    else:
        raise Exception ('my_basemaps function does not exist.')
        
def test_my_basemaps2 ():
    '''Verify the returned value of my_basemaps.
       Assertion: 
       True: the output value is a dictionary.
       False: TypeError.  
    '''
    output1 = my_functions.my_basemaps()
    assert type(output1) == dict, " TypeError "


       
def test_download_point_data1 ():
    '''Verify the existence of download_point_data.
       If True: function exists, pass. 
       If False: function does not exist, raise exception.  
    '''
    if my_functions.download_point_data: 
        pass
    else:
        raise Exception ('download_point_data function does not exist.')
        
#def test_download_point_data2 ():
    #'''Verify the returned value of download_point_data.
       #Assertion: 
       #True: the output value is a numpy array of seismicity information'.
       #False: TypeError.  
    #'''
    #output1 = my_functions.download_point_data([30, -123, 40, -113])
    #assert type(output1) == np.array, " TypeError "

    
def test_download_point_data3 (region = [30, 190, 40, -113]):
    '''Verify the type of the input parameter of download_point_data, the type of each item inside the input parameter, 
       and if the item value is feasible.
       Assertion: 
       True: 1) the input parameter is a list. 
             2) the item inside the input parameter is a float number.
             3) the item value is a meaningful geographical coordinate. 

       False: 1) TypeError. 2) TypeError. 3) ValueError.   
    '''
    if type (region) == list: #check the type of 'region'
        
        #check the type of coordinates in region list
        for coordinate in region: 
            if type (coordinate) == float or int:
                pass
            else: 
                raise TypeError ("region coordinate must be a float number")
                
        #check if the latitudes are valid
        if -90 <= region[0] <= 90 and -90 <= region[2] <= 90: 
            pass
        else: raise ValueError ("region latitude should be a float number in the range of [-90,90].")
        
        #check if the longitudes are valid
        if -180 <= region[1] <= 180 and -180 <= region[3] <= 180:
            pass
        else: raise ValueError ("region longitude should be a float number in the range of [-180,180].")
        
    else: 
        raise TypeError ("region must be a list.")


def test_my_point_data1 ():
    '''Verify the existence of my_point_data.
       If True: function exists, pass. 
       If False: function does not exist, raise exception.  
    '''
    if my_functions.my_point_data: 
        pass
    else:
        raise Exception ('my_point_data function does not exist.')

#def test_my_point_data2 ():
    #'''Verify the returned value of my_point_data.
       #Assertion: 
       #True: the output value is a numpy array .
       #False: TypeError.  
    #'''
    #output1 = my_functions.my_point_data(region = [30, -123, 40, -113])
    #assert type(output1) == np.array, " TypeError "
    


def test_download_raster_data1 ():
    '''Verify the existence of download_raster_data.
       If True: function exists, pass. 
       If False: function does not exist, raise exception.  
    '''
    if my_functions.download_raster_data: 
        pass
    else:
        raise Exception ('download_raster_data function does not exist.')
        
def test_download_raster_data2 ():
    '''Verify the returned value of download_raster_data.
       Assertion: 
       True: the output value is a numpy n-dimensional array.
       False: TypeError.  
    '''
    output1 = my_functions.download_raster_data()
    assert type(output1) == np.ndarray, " TypeError "


def test_my_global_raster_data1 ():
    '''Verify the existence of my_global_raster_data.
       If True: function exists, pass. 
       If False: function does not exist, raise exception.  
    '''
    if my_functions.my_global_raster_data: 
        pass
    else:
        raise Exception ('download_raster_data function does not exist.')
        
def test_my_global_raster_data2 ():
    '''Verify the returned value of my_global_raster_data.
       Assertion: 
       True: the output value is a numpy n-dimensional array.
       False: TypeError.  
    '''
    output1 = my_functions.my_global_raster_data()
    assert type(output1) == np.ndarray, " TypeError "           



