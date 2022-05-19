"""All the functions we need to make a map:

    - my_documentation()
    - my_coastlines()
    - my_water_features()
    - my_basemaps()

"""


def my_documentation():

    markdown_documentation = """   
# Mapping Service with On-Demand Data

Your patience is appreciated with the loading of the final map: load times can vary.
    
## Overview

This mapping function provides a regional comparison of algae bloom reports and a biodiversity index using
the Cartopy package as a baseline build. The user can enter a specific region for examination or adjust the given
inputs by changing the inputs under ```# Specify a region of interest``` <br>
Note: algae data is only available for California, and the biodiversity ranges over the contiguous USA.

## Features 
All features are built-in to import from the Cartopy packages, including: Coastlines, Oceans, Rivers, Lakes.
Each feature requires a resolution input of string values "10m", "50m", or "110m" <br>
There is also a built-in Base Map that consists of Open Street Maps and QuadtreeTile.


## On-demand data 

Two data types have been preloaded and formatted: a point data analysis of harmful algae blooms and
raster data of biodiversity functional types. <br>
Note: To accomodate the overlapping display of both point and raster data, the alpha value has been changed: <br>
```cf = ax.contourf( ... cmap="RdYlBu",zorder=2, alpha=0.25) ``` <br>
This can be increased or decreased depending on user preference.


## `Python` documentation

Customised docstrings can be called with the help() function for the data and functions in this program, including: <br>
    my_coastlines <br>
    my_water_features <br>
    my_basemaps <br>
    download_point_data <br>
    download_raster_data<br>
    
Source code found in the src folder. Testing functions found in the tests folder.


"""
    
    return markdown_documentation


def my_coastlines(resolution):
    """ returns the relevant coastlines at the requested resolution, 
    where the resolution must be a string of either '10m', '50m', or '100m' """

    import cartopy.feature as cfeature
    
    #import coastlines from cartopy
    return cfeature.NaturalEarthFeature('physical', 'coastline', resolution,
                                        edgecolor=(0.0,0.0,0.0),
                                        facecolor="none")


def my_water_features(resolution, lakes=True, rivers=True, ocean=True):
    """Returns a [list] of cartopy features including 'rivers', 'lakes', and 'ocean'
    which must be called as (resolution, feature=True)
    where resolution is a string of values '10m', '50m' or '110m
    
    Features are as follows:
     	Ocean – Ocean polygon split into contiguous pieces.
        Lakes – Automatically scaled natural and artificial lakes.
        Rivers - Automatically scaled single-line drainages, including lake centerlines.
    As desinged by Natural Earth Data at https://www.naturalearthdata.com/features/ and integrated
    using the Cartopy package: https://scitools.org.uk/cartopy/docs/latest/index.html'"""
    
    import cartopy.feature as cfeature
    
    #construct the list
    features = []
    
    #define each feature when called
    if rivers == True:
        features.append(cfeature.NaturalEarthFeature(scale=resolution, category='physical',
    name='rivers_lake_centerlines', facecolor='none'))
        
    if lakes == True:
        features.append(cfeature.NaturalEarthFeature('physical', 'lakes', resolution))

    if ocean == True:
        features.append(cfeature.NaturalEarthFeature('physical', 'ocean', resolution))
    
    return features

def my_basemaps():
    """Returns a dictionary of map tile generators that cartopy can use
        The full list of available interfaces is found in the source code for this one:
        https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py
    Currently selected maps are:
        Open Street Map from https://www.openstreetmap.org/#map=4/-28.15/133.28
        QuadtreeTiles which is defined by Cartopy as:
            Implement web tile retrieval using the Microsoft WTS quadkey coordinate system.
            A “tile” in this class refers to a quadkey such as “1”, “14” or “141” 
            where the length of the quatree is the zoom level in Google Tile terms."""
    
    import cartopy.io.img_tiles as cimgt 
    
    #construct the list
    mapper = {}
    
    #import Open Street Map and QuadtreeTiles
    mapper["open_street_map"] = cimgt.OSM()
    mapper["mapbox_outdoors"] = cimgt.QuadtreeTiles()

    return mapper


# # specify some point data (Freshwater Harmful Algae Blooms)

def download_point_data(region):
    """Returns specified point data formatted into an array of longitude, latitude, and ID code. 
            In this instance, harmful algae bloom points in California:
                https://data.ca.gov/dataset/ab672540-aecd-42f1-9b05-9aad326f97ec/resource/c6f760be-b94f-495e-aa91-2d8e6f426e11/download/fhab_bloomreport_portal.csv."""
    
    import pandas as pd
    import numpy as np
    
    #import data and create dataframe
    algae  = pd.read_csv('src/fhab_bloomreport_portal.csv')
    df = pd.DataFrame(algae)
    
    #align data into lat, lon, category
    lon = np.array(df["Longitude"])
    lat = np.array(df["Latitude"])
    cat = np.array(df["CountyID"])
    con = np.ones(len(df["Longitude"]))


    point_data = np.column_stack((lon, lat, cat, con))


    return point_data


def my_point_data(region):
    
    data = download_point_data(region)
    
    return data


# # - Some global raster data (lon, lat, data) Biodiversity in the USA

def download_raster_data():
    """Raster data that has been matched and fit to a global lat/lon grid.
    
    This dataset provides maps of the distribution of ecosystem functional types (EFTs) and the interannual variability of EFTs at 
        0.05 degree resolution across the conterminous United States (CONUS) for 2001 to 2014. EFTs are groupings of ecosystems based on 
        their similar ecosystem functioning that are used to represent the spatial patterns and temporal variability of key ecosystem 
        functional traits without prior knowledge of vegetation type or canopy architecture. Sixty-four EFTs were derived from the metrics 
        of a 2001-2014 time-series of satellite images of the Enhanced Vegetation Index (EVI) from the Moderate Resolution Imaging Spectroradiometer (MODIS) 
        product MOD13C2. EFT diversity was calculated as the modal (most repeated) EFT and interannual variability was calculated as the number of unique EFTs for each pixel.

                https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=1659
    
    """
    
    import cartopy.io.shapereader as shpreader
    import json
    import numpy as np
    from osgeo import gdal
    
    #import data and enter into array
    ds = gdal.Open('src/ecosystem_functional_types_diversity.tif')
    band = ds.GetRasterBand(1)
    arr = band.ReadAsArray()
    
    #size to match the latitude and longitude of the data
    datasize = (494, 1153, 3)
    raster = np.empty(datasize)
    
    #fit the data into a lat/lon array
    #using the data's range to set the space alignment
    lats = np.linspace(49.36, 24.55, datasize[0])
    lons = np.linspace(-124.77, -67.0, datasize[1])
    
    arrlons,arrlats = np.meshgrid(lons, lats)

    raster[...,0] = arrlons[...]
    raster[...,1] = arrlats[...]
    raster[...,2] = arr[...]



    return raster


def my_global_raster_data():

    raster = download_raster_data()
    
    return raster


