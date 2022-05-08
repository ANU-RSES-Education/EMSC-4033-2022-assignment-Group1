import pytest
from src.my_functions import *


def test_is_my_documentation():
    docs = my_documentation()
    docs_t= []
    if "Introduction" in docs:
        docs_t.append(1)
    
    assert docs_t == [1], "this is not the correct documentation for map_maker"


def test_my_documentation_is_txt():
    docs = my_documentation()
    assert type(docs) == str, "this function is not calling text documentation"


# +
#test_is_my_documentation()
# -

def test_my_coastline_is_cfeature():
    coast_t = my_coastlines("50m")
    assert type(coast_t) == cfeature.NaturalEarthFeature, "This is not a cartopy feature"


def test_my_coastline_is_coast(name_t = 'coastline'):
    coast_t = my_coastlines("50m")
    name_m = coast_t.name
    assert name_m == name_t, "This is not a cartopy coastline feature"


coast_t = my_coastlines("50m")
coast_t.scale


def test_my_coastline_input_is_string():
    coast_t = my_coastlines("50m") 
    assert type(coast_t.scale) == str, "a string must be used, use quotations around resolution variable"


test_my_coastline_input_is_string()
#my_coastline_input_is_string()

def test_my_coastline_input_resolution(resolution = ['10m','50m','110m']):
    coast_t = my_coastlines("10m")
    res_s = coast_t.scale 
    res=[]
    if "50m" in res_s:
        res.append(1)
    if "10m" in res_s:
        res.append(1)
    if "110m" in res_s:
        res.append
    assert 1 in res, "must use 10m, 50m, or 110m"


test_my_coastline_input_resolution()


def test_my_coastline_input_m(resolution = "50m"):
    coast_t = my_coastlines("10m")
    res_s = coast_t.scale 
    
    mcheck =[]
    if 'm' in res_s:
        mcheck.append(1)
    assert mcheck == [1], "must use variable (m) in input"


test_my_coastline_input_m()


def test_my_water_feature_islist():
    listw = my_water_features("50m")
    assert isinstance(listw, (list)), "this is not a list"


# +
#my_water_feature_test_islist()
# -

def test_my_water_feature_iscfeature():
    listw = my_water_features("50m")
    assert type(listw[1] == cartopy.feature.NaturalEarthFeature), "this does not contain cartopy features"
    assert type(listw[0] == cartopy.feature.NaturalEarthFeature), "this does not contain cartopy features"


# +
#my_water_feature_test_iscfeature()
# -

def test_my_basemaps_isdict():
    dictt = my_basemaps()
    assert isinstance(dictt, (dict)), "this is not a dictionary"


# +
#my_basemaps_isdict()
# -

def test_my_basemaps_testlen():
    dictt = my_basemaps()
    assert len(dictt) == 5, "this dictionary does not contain all basemap types"


def test_my_basemaps_contains():
    dictt = my_basemaps()
    x = []
    if "open_street_map" in dictt:
        x.append(1)
    if "mapbox_outdoors" in dictt:
        x.append(2)
    if "mapbox_satellite" in dictt:
        x.append(3)
    if "mapbox_satellite_streets" in dictt:
        x.append(4)
    if "mapbox_satellite_streets" in dictt:
        x.append(5)
    assert [1,2,3,4,5] == x, "this dictionary contains the wrong basemaps"


# +
#my_basemaps_testcontains()
# -

def test_my_basemaps_tile():
    dictt = my_basemaps()
    assert type(dictt["open_street_map"]) == cartopy.io.img_tiles.OSM, "This is not calling cartopy image tiles"


# +
#my_basemaps_test_tile()

# +
lat0 =  30  ; lat1 = 40
lon0 =  -123; lon1 = -113

map_extent = [lon0, lon1, lat0, lat1]


# -

def test_Download_point_imports():
    download_point_data(map_extent,"1975-01-01","2022-01-01", 7)
    import sys
    mods = []
    if 'pandas' in sys.modules:
        mods.append(1)
    if 'obspy.core' in sys.modules:
        mods.append(1)
    if 'obspy.clients.fdsn' in sys.modules:
        mods.append(1)
    
    assert mods == [1,1,1], "the required modules have not imported"


# +
#Download_point_test_imports()
# -

def test_Download_point_type():
    data = download_point_data(map_extent,"1975-01-01","2022-01-01", 7)
    assert type(data) == np.ndarray, "this is not in the required data structure"


# +
#Download_point_test_type()
# -

def test_Download_point_dim():
    data = download_point_data(map_extent,"1975-01-01","2022-01-01", 7)
    assert data.ndim == 2, "this does not have the expected dimesions"


# +
#Download_point_test_dim()
# -

def test_Download_point_shape():
    data = download_point_data(map_extent,"1975-01-01","2022-01-01", 7)
    assert data.shape == (4,4), "this does not have the expected shape"


# +
#Download_point_test_shape()
# -

def test_download_raster_data_size():
    data = download_raster_data()
    assert data.shape == (1801, 3601, 3), "this does not have the expected shape"

# +
#download_raster_data_test_size()
# -


