"""All the functions we need to make a map:

    - my_documentation()
    - my_coastlines()
    - my_water_features()
    - my_basemaps()

"""

from .dependencies import *

def my_documentation():
    """ This function displays handy hints on what this notebook does and how to use it
    """

    markdown_documentation = """   
# Map Maker Program
    
## Introduction

The map maker program is a friendly seismic event map generator that can be run by anyone using python.
This map maker utilsies the IRIS seismic moniotring station data, various basemaps and Earthbyters 
ocean seafloor age data to visualize sesimic events on the globe. Users can define when and where they
want to analyse and what basemaps are most useful to their study.

## Using the program

Using this program is very simple, all it requires is the user to download the map_maker notebad from 
our Git repository. The notebook will open up, and comments will prompt users where they need to input
their parameters. There are five areas where the user will need to input data. These are:

### latitude and longitude
Input the lats and lons of the bounding box you want to study. These are the North(lat1), East(lon1),
South(lat0), West (lon0).

```python
# Simply change the values next to the equals sign!
lat0 =  30  ; lat1 = 40
lon0 =  -123; lon1 = -113
```

### basemap_name
Input what basemap you would like to display in the final product. To find the list of basemaps you can choose from run the code line:

```python
map_tiles_dictionary = my_basemaps()
map_tiles_dictionary.keys()
```
``` 
```
You must copy the basemap name in quotation marks for this code to excute



### my_coastline and my_water_features
Input the resolution you want these features to be presented as. Call ```help(my_coastline)``` to see the resolution options. 

### point_data
Input the range (start and end) and minimum magnitude of seismic events want to work with, leave map_extent.

### Run the code
Once the required information has been inputted the user needs to simply run the code, and a .png image will be saved with the seismic event map.

## Getting help
If you require additional help, all the functions in this notebook have handy hints to look at. Simple call ```help("the function you need help with")``` 
to print function documentation.

"""
    
    return markdown_documentation


def my_coastlines(resolution):
    """ 
    This function generates coastline edges at a specified resolution
    Parameters
    ----------
    resolution : string
        the resolutions that can be chosen are "10m", "50m", or "110m"
    
    Returns
    -------
    cartopy.feature : cartopyfeature.COASTLINE object at specifed resolution

    """
    p = resolution
    import cartopy.feature as cfeature
    print("Chosen coastline resolution is:", p)
    return cfeature.NaturalEarthFeature('physical', 'coastline', p, facecolor = 'none')


def my_water_features(resolution, lakes=True, rivers=True, ocean=False):
    """
    This function returns a [list] of cartopy water features at a specified resolution
    Parameters
    ----------
    resolution : string
                the resolutions that can be chosen are "10m", "50m", or "110m"
    
    Returns
    -------
    features : list
                cartopyfeature.river or lakes object at specifed resolution
    
    """
    p = resolution
    features = []
    print("Chosen water features resolution is:", p)
    if rivers:
        features.append(cfeature.NaturalEarthFeature(scale=p, category='physical',
        name='rivers_lake_centerlines', facecolor='none'))
        
    if lakes:
        features.append(cfeature.NaturalEarthFeature('physical', 'lakes', p))

    if ocean:
        features.append(cfeature.NaturalEarthFeature('physical', 'ocean', p))
    return features


# +

def my_basemaps():
    """
    Returns a dictionary of map tile generators that cartopy can use. To use this function simply type "my_basemaps()".
    Parameters
    ----------
    tile generators: matplotlib tiles
                      Cartoply basemap fetchers
                    
     
    Returns
    -------
    basemaps : list
                list of basemaps that user can choose from.
    
    
    """
    
    
    ## The full list of available interfaces is found in the source code for this one:
    ## https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py

    # dictionary of possible basemap tile objects
    
    mapper = {}
    
    ## Open Street map
    mapper["open_street_map"] = cimgt.OSM()
    mapper["mapbox_outdoors"] = cimgt.MapboxTiles(access_token='pk.eyJ1Ijoic2FtbDk5IiwiYSI6ImNsMm1tdzhyejBnN20za2xwazN3aWRwdncifQ.mfIqdP9UUjSGm5gx8LkKZQ',map_id='outdoors-v11')
    mapper["mapbox_satellite"] = cimgt.MapboxTiles(access_token='pk.eyJ1Ijoic2FtbDk5IiwiYSI6ImNsMm1tdzhyejBnN20za2xwazN3aWRwdncifQ.mfIqdP9UUjSGm5gx8LkKZQ',map_id='satellite-v9')
    mapper["mapbox_satellite_streets"] = cimgt.MapboxTiles(access_token='pk.eyJ1Ijoic2FtbDk5IiwiYSI6ImNsMm1tdzhyejBnN20za2xwazN3aWRwdncifQ.mfIqdP9UUjSGm5gx8LkKZQ',map_id='satellite-streets-v11')
    mapper["stamen_terrain"] = cimgt.StamenTerrain()

    return mapper
# -





# # specify some point data (e.g. global seismicity in this case)

def download_point_data(region, start, end, minmag):
    """
    This function generates point data for seismic events picked up on the IRIS seismic monitor for th given location, start and end times and the minimum magnitude.
    
    Parameters
    ----------
    Region: string
            Input "map_extent" string. This string references a list of lat and lons. map_extent must be defined to be valid.
    start: string
           Input date in format "yyyy-mm-dd". This is the time you want to start gathering seismic data from
    end: string
           Input date in format "yyyy-mm-dd". This is the time you want to stop gathering seismic data from
    minmag: int
            Input the minimum magnitude number you want to collect data for. Ie input 7 if you only want to gather information on events larger than magnitude 7.               
     
    Returns
    -------
    df1 : numpy array
          The retrun is a numpy array with (lat, lon, magnitude and marker size) of seismic event.
    
    """
    
    import pandas as pd
    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    client = Client("IRIS")
    extent = region

    
    t1 = UTCDateTime(start)
    t2   = UTCDateTime(end)
    
    
    cat = client.get_events(starttime=t1, endtime=t2, minmagnitude=minmag, minlatitude=extent[2],
                        maxlatitude=extent[3],minlongitude=extent[0],maxlongitude=extent[1])
    print ("Point data: {} events in catalogue".format(cat.count()))
    
    # Unpack the obspy data into a plottable array

    feature_list = ['Lon [°]','Lat [°]', 'mag', 'event_type']
    df = pd.DataFrame(0, index=np.arange(len(cat)), columns=feature_list)

    for ii in range (0, len(cat)):
        
        df['Lon [°]'].loc[ii] = cat[ii].origins[0].longitude
        df['Lat [°]'].loc[ii] = cat[ii].origins[0].latitude
        df['mag'].loc[ii] = cat[ii].magnitudes[0].mag
        df['event_type'].loc[ii] = 3
    df1 = df.to_numpy()

    return df1


def my_point_data(region,start, end, minmag):
    """
    This function generates point data for seismic events picked up on the IRIS seismic monitor for th given location, start and end times and the minimum magnitude.
    
    Parameters
    ----------
    Region: string
            Input "map_extent" string. This string references a list of lat and lons. map_extent must be defined to be valid.
    start: string
           Input date in format "yyyy-mm-dd". This is the time you want to start gathering seismic data from
    end: string
           Input date in format "yyyy-mm-dd". This is the time you want to stop gathering seismic data from
    minmag: int
            Input the minimum magnitude number you want to collect data for. Ie input 7 if you only want to gather information on events larger than magnitude 7.               
     
    Returns
    -------
    df1 : numpy array
          The retrun is a numpy array with (lat, lon, magnitude and marker size) of seismic event.
    
    """
    
    data = download_point_data(region,start, end, minmag)
    
    return data


# # - Some global raster data (lon, lat, data) global plate age, in this example

def download_raster_data():
    
    # Seafloor age data and global image - data from Earthbyters

    # The data come as ascii lon / lat / age tuples with NaN for no data. 
    # This can be loaded with ...

    # age = numpy.loadtxt("Resources/global_age_data.3.6.xyz")
    # age_data = age.reshape(1801,3601,3)  # I looked at the data and figured out what numbers to use
    # age_img  = age_data[:,:,2]

    # But this is super slow, so I have just stored the Age data on the grid (1801 x 3601) which we can reconstruct easily
    datasize = (1801, 3601, 3)
    raster = np.empty(datasize)

    ages = np.load("global_age_data.3.6.z.npz")["ageData"]

    lats = np.linspace(90, -90, datasize[0])
    lons = np.linspace(-180.0,180.0, datasize[1])

    arrlons,arrlats = np.meshgrid(lons, lats)

    raster[...,0] = arrlons[...]
    raster[...,1] = arrlats[...]
    raster[...,2] = ages[...]


    return raster


def my_global_raster_data():
    """
    This function downloads seafloor age data from earthbyters.
    
    Parameters
    ----------
    global_age_data: npz file from Earthbyters
    
    Returns
    -------
    
    Raster: numpy array
            Returns a numpy array with latitude, longitudes and ages.
    """

    raster = download_raster_data()
    
    return raster


