"""All the functions we need to make a map:

    - my_documentation()
    - my_coastlines()
    - my_water_features()
    - my_basemaps()

"""

from .dependencies import *

def my_documentation():

    markdown_documentation = """   

This my_functions.py module contains all the functions that will make MapMaker.ipynb work properly. 

The user needs to specify the region, resolution and basemap of interest as inputs. 

In general, the functions in this module is organised based on different types of features to be put on the map. 

## The features are: 

1) geographical features: my_coastlines and my_water_features that take requested resolution as a parameter to generate map features. 

2) graphical features: my_basemaps, download_raster_data, and my_global_raster_data output corresponding map graphics. 

3) point features: download_point_data and my_point_data output the regional seismicity as point-like representation on the map. 

## Data: 

1) Point data (seismicity): downloaded from IRIS FDSN network (http://www.fdsn.org/services/)

2) Raster data (seafloor age data): downloaded from cloudstor "global_age_data.3.6.z.npz".

"""
    
    return markdown_documentation



def my_coastlines(resolution):
    """ Map the relevant coastlines at the requested resolution.
        
        Parameters: 
        resolution (string): The dataset scale,
        one of ‘10m’, ‘50m’, or ‘110m’. 
        Corresponding to 1:10,000,000, 1:50,000,000, and 1:110,000,000 respectively.
        
        Returns: 
        coastline (Cartopy features)
        
    """

    import cartopy.feature as cfeature
    coastline_feature = cfeature.NaturalEarthFeature('physical', 'coastline',
                                           resolution,  
                                           edgecolor=(0.0,0.0,0.0),
                                           facecolor='none')
    #coastline = ax.add_feature(coastline_feature)

    return coastline_feature

def my_water_features(resolution, lakes=True, rivers=True, ocean=False):
    """ Create the relevant river, lake, and ocean features at the requested resolution.
        
        Parameters: 
        resolution (string): The dataset scale,
        one of ‘10m’, ‘50m’, or ‘110m’. 
        Corresponding to 1:10,000,000, 1:50,000,000, and 1:110,000,000 respectively.
        
        Returns: 
        features (list): a list of cartopy features 
        
    """
    features = []   #create an empty list to store water features
    
    if rivers:
        river_feature = cfeature.NaturalEarthFeature('physical','rivers_lake_centerlines', resolution,
                                        edgecolor='none',
                                        facecolor='#0000FF')
        features.append(river_feature)
        
    if lakes:
        lake_feature = cfeature.NaturalEarthFeature('physical', 'lakes', resolution,
                                        edgecolor=(0.0,0.0,0.0),
                                        facecolor='none')
        features.append(lake_feature)

    if ocean:
        ocean_feature = cfeature.NaturalEarthFeature('physical', 'ocean', resolution,
                                        edgecolor=(0.0,0.0,0.0),
                                        facecolor='none')
        features.append(ocean_feature)
    
    return features

def my_basemaps():
    """Create a dictionary of map tile generators for later use.
       The user can check the cartopy documentation of image tiles (https://scitools.org.uk/cartopy/docs/v0.16/cartopy/io/img_tiles.html). 
    
       Parameters: 
       None
        
       Returns: 
       mapper (dict): contains map tiles of open street map, Mapbox tiles and aerial photos for user to choose from
    
    """
    
    ## The full list of available interfaces is found in the source code for this one:
    ## https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py

    # dictionary of possible basemap tile objects
    
    mapper = {}
    
    ## Open Street map
    mapper["open_street_map"] = cimgt.OSM()
    ##open mapbox tiles 
    mapper["mapbox_outdoors"] = cimgt.MapboxTiles (map_id='outdoors-v11',
                                           access_token=   
                    'pk.eyJ1IjoibG91aXNtb3Jlc2kiLCJhIjoiY2pzeG1mZzFqMG5sZDQ0czF5YzY1NmZ4cSJ9.lpsUzmLasydBlS0IOqe5JA')
    
    mapper["Aerial"] = cimgt.MapQuestOpenAerial()
    
    return mapper


## specify some point data (e.g. global seismicity in this case)

def download_point_data(region):
    """Create a numpy array that contains the geographical and depth information of seismicity in the selected region.
       The user can check the documentation of obspy (https://docs.obspy.org/) for the usage of the functions. 
    
       Parameters: 
       
       region (list): a list containing the the min&max longitude and min&max latitude of the selected region 
       [min_lon, max_lon, min_lat, max_lat]
        
       Returns: 
       eq_origins (numpy array): 
       1st column: longitude
       2nd column: latitude
       3rd column: depth
       4th column: size of the circles representing seismic events
       
    """
    
    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    client = Client("IRIS")

    map_extent = region

    starttime = UTCDateTime("1975-01-01")
    endtime   = UTCDateTime("2022-01-01")
    
    #extract latitude and longitude information from map_extent
    lat0 = map_extent[2]
    lat1 = map_extent[3]
    lon0 = map_extent[0]
    lon1 = map_extent[1]
    
    #ertrieve seismic events above magnitude 5.0 and their metadata
    catalogue = client.get_events(starttime=starttime,endtime=endtime,\
                              minlatitude=lat0,maxlatitude=lat1,\
                              minlongitude=lon0,maxlongitude=lon1,\
                              minmagnitude=5.0, maxmagnitude=None,\
                              mindepth=None, maxdepth=None)
    
    print ("Point data: {} events in catalogue".format(catalogue.count()))
    
    # Unpack the obspy data into a plottable array
    
    event_count = catalogue.count()
    
    #set up an empty array with four columns to store seismic information for plotting 
    eq_origins = np.zeros((event_count, 4))
    
    #to store each seismic event
    eventlist = []
    for i in range(len(catalogue)):
        event = catalogue[i]
        eventlist.append(event)
    
    #to store the origin of each event 
    originlist = []
    for eq in eventlist:
        origin = eq.origins[0]
        originlist.append(origin)
    
    #to store the longitude of each event from its origin
    lonlist = []
    for item in originlist:
        lon = item.longitude
        lonlist.append(lon)
    
    #to store the latitude of each event from its origin
    latlist = []
    for item in originlist:
        lat = item.latitude
        latlist.append(lat)
    
    #to store the depth of each event from its origin
    depthlist = []
    for item in originlist:
        depth = item.get('depth')
        depthlist.append(depth)

    eq_origins[:,0] = lonlist
    eq_origins[:,1] = latlist
    eq_origins[:,2] = depthlist
    eq_origins[:,3] = np.ones(event_count)*2
    
    return eq_origins


def my_point_data(region):
    """Re-name returned values from function 'download_point_data(region)'.
    
       Parameters: 
       region (list): a list containing the the min&max longitude and min&max latitude of the selected region 
       [min_lon, max_lon, min_lat, max_lat]
       
       Returns: 
       data (numpy array):
       1st column: longitude
       2nd column: latitude
       3rd column: depth
       4th column: size of the circles representing seismic events
    
    """
    data = download_point_data(region)
    
    return data


## - Some global raster data (lon, lat, data) global plate age, in this example

def download_raster_data():
    """Create a numpy array that contains the global seafloor age data.
    
       Parameters: 
       None
        
       Returns: 
       raster_data (numpy array): 
       1st column: longitude
       2nd column: latitude
       3rd column: age of seafloor
       
    """
    
    # Seafloor age data and global image - data from Earthbyters

    # The data come as ascii lon / lat / age tuples with NaN for no data. 
    # This can be loaded with ...

    # age = numpy.loadtxt("Resources/global_age_data.3.6.xyz")
    # age_data = age.reshape(1801,3601,3)  # I looked at the data and figured out what numbers to use
    # age_img  = age_data[:,:,2]

    # But this is super slow, so I have just stored the Age data on the grid (1801 x 3601) which we can reconstruct easily

    from cloudstor import cloudstor
    teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
    teaching_data.download_file_if_distinct("global_age_data.3.6.z.npz", "global_age_data.3.6.z.npz")

    datasize = (1801, 3601, 3)
    raster_data = np.empty(datasize)
    
    age = np.load ("global_age_data.3.6.z.npz")["ageData"]
    lats_extent = np.linspace(90,-90,1801)
    lons_extent = np.linspace(-180,180, 3601)
    llX, llY = np.meshgrid(lons_extent, lats_extent)
    raster_data[...,0] = llX [...]
    raster_data[...,1] = llY [...]
    raster_data[...,2] = age [...]
    
    return raster_data



def my_global_raster_data():
    """Re-name returned values from function 'download_raster_data()'.
    
       Parameters: 
       None
       
       Returns: 
       raster (numpy array):
       1st column: longitude
       2nd column: latitude
       3rd column: age of seafloor
    
    """
    raster = download_raster_data()
    
    return raster
