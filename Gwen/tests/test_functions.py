import pytest
from src.my_functions import *
from src.dependencies import *


def test_my_documentation ():
    #test my_documentation loads
    if my_documentation: 
        pass
    else:
        raise Exception ("my_documentation not found")


def test_is_my_documentation():
    #test correct document loads
    docs = my_documentation()
    docst = []
    if "Overview" in docs:
        docst.append(1)
    
    assert docst == [1], "Please check file path for my_documentation"


def test_my_documentation_string():
    #test document is of string type
    docs = my_documentation()
    assert type(docs) == str, "my_documentation must be a string type"





def test_my_coastline():
    #test my_coastlines loads
    if my_coastlines: 
        pass
    else:
        raise Exception ("my_coastlines function not found")


def test_my_coastline_is_cfeature():
    #test cartopy feature is called
    coast1 = my_coastlines("10m")
    assert type(coast1) == cfeature.NaturalEarthFeature, "This is not a cartopy feature"
    coast2 = my_coastlines("50m")
    assert type(coast2) == cfeature.NaturalEarthFeature, "This is not a cartopy feature"
    coast3 = my_coastlines("110m")
    assert type(coast3) == cfeature.NaturalEarthFeature, "This is not a cartopy feature"


def test_my_coastline_string():
    #test input is string type
    coast1 = my_coastlines("10m") 
    assert type(coast1.scale) == str, "Input must be a string of values '10m', '50m', or '110m'"
    coast2 = my_coastlines("50m") 
    assert type(coast2.scale) == str, "Input must be a string of values '10m', '50m', or '110m'"
    coast3 = my_coastlines("110m") 
    assert type(coast3.scale) == str, "Input must be a string of values '10m', '50m', or '110m'"



def test_my_water_features():
    #test my_water_features loads
    if my_water_features: 
        pass
    else:
        raise Exception ("my_water_features function not found")


def test_my_water_features_is_cfeature():
    #test cartopy feature is called
    wf1 = my_water_features("50m", lakes=True)
    assert type(wf1[0]) == cfeature.NaturalEarthFeature, "This is not a cartopy feature"
    wf2 = my_water_features("50m", rivers=True)
    assert type(wf2[1]) == cfeature.NaturalEarthFeature, "This is not a cartopy feature"
    wf3 = my_water_features("50m", ocean=True)
    assert type(wf3[2]) == cfeature.NaturalEarthFeature, "This is not a cartopy feature"


def test_my_water_feature_resolution(resolution = "50m"):
    #test input is string of correct values
    if resolution == "50m" or "10m" or "110m": 
        pass
    else: 
        raise Exception ("Input must be a string of values '10m', '50m', or '110m'")



def test_my_basemap():
    #test my_basemaps loads
    if my_basemaps: 
        pass
    else:
        raise Exception ("my_basemaps function not found")


def test_my_basemaps_dict():
    #test my_basemaps is a dictionary type
    tdict = my_basemaps()
    assert type(tdict) == dict, "my_basemaps is wrong type; must be dictionary"


def test_my_basemaps_tile():
    #test my_basemaps calls cartopy tiles
    tile = my_basemaps()
    assert type(tile["open_street_map"]) == cartopy.io.img_tiles.OSM, "calling error. must call cartopy tile"
    tile2 =  my_basemaps()
    assert type(tile2["mapbox_outdoors"]) == cartopy.io.img_tiles.QuadtreeTiles, "calling error. must call cartopy tile"



def test_point_data ():
   #test download_point_data loads
    if download_point_data: 
        pass
    else:
        raise Exception ("download_point_data function not found")


def test_point_data_dimension():
    #test point data dimensions
    pdata = download_point_data(map_extent)
    assert pdata.ndim == 2, "Point data is not of the expected dimensions"


def test_point_data_type():
    #test that point data is in numpy array
    pdata = download_point_data(map_extent)
    assert type(pdata) == np.ndarray, "TypeError: Point data must be called as numpy array"



# +
lat0 =  30  ; lat1 = 40
lon0 =  -123; lon1 = -113

map_extent = [lon0, lon1, lat0, lat1]
# -



def test_download_raster_data ():
   #test download_raster_data loads
    if download_raster_data: 
        pass
    else:
        raise Exception ("download_raster_data function not found")


def test_raster_data_dimension():
    #test raster data dimensions
    rdata = download_raster_data()
    assert rdata.ndim == 3, "Raster data is not of the expected dimensions"


def test_raste_data_type():
    #test that raster data is in numpy array
    rdata = download_raster_data()
    assert type(rdata) == np.ndarray, "TypeError: Raster data must be called as numpy array"



















# +
lat0 =  30.23  ; lat1 = 42.135
lon0 =  -114.139 ; lon1 = -177.269

algae_extent = [lon0, lon1, lat0, lat1]

# +
lat0 =  49.36  ; lat1 = 24.55
lon0 =  -67.00 ; lon1 = -124.77

bio_extent = [lon0, lon1, lat0, lat1]
# -












