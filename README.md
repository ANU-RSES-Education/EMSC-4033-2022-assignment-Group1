
> # About this repository
> 
> This repository is written by Sam, Gwendolyn and Xulu for assignment 1 EMSC-4033/8033, semester 1, 2022.  Within this repository are three folders containing a MapMaker program and its supporting files.
> # Project aims
> 
> This project aims to combine three types of geological data into one useful map.
> 
>    * Mapping geographical features including coastlines, lakes, rivers, and ocean. This is achieved using Cartopy NaturalEarthFeature (https://scitools.org.uk/cartopy/docs/v0.14/matplotlib/feature_interface.html) with classic Python Matplotlib, given requested resolution and region coordinates. Cartopy is a popular mapping tool in the geoscience community due to its simplicity and quality visualisation of scientific data.
> 
>    * Mapping point data. This repository provieds point data for  seimic events downloaded from IRIS FDSN server (http://www.fdsn.org/datacenters/detail/IRISDMC/) We use Obspy library in Python (https://docs.obspy.org/) to query, retrieve and process seismic data.
> 
>    * Mapping raster data. This repository provides the option of mapping seafloor age data and visualising it as contour lines for the region of interest. The data is available at https://www.earthbyte.org/category/resources/data-models/seafloor-age/.
> 
> [See Note about Alternate Data below]
> 
> # How to Use
> 
> The plotting program 'MapMaker.ipynb' is a Jupyter Notebook ready-to-run with all the necessary support files arranged in each folder: 'Sam', 'Xulu', and 'Gwen'.
> 
> It imports all necessary libraries and functions from the src folder, which include:
> 
>  * 'dependencies.py'  -- The requisite Python libraries and modules are called within 'dependecies.py'. 
>
> * 'my_functions.py' -- Which contains: Geographical feature mapping functions: my_coastlines, my_water_features, my_basemaps; Seismic event mapping functions: download_point_data, my_point_data; Seafloor Age mapping functions: download raster_data, my_global_raster_data.
>
>
>   ''RunTests.ipynb' is another notebook alongside the MapMaker which provides robust tests that are defined within 'test_functions.py' designed for useful debugging. Note: tests vary in each folder ('Sam', 'Xulu', and 'Gwen')
>
>
> 
> 
># Alternative Data
> The Sam and Xulu folders contain the seismic and seafloor data defined above. The folder 'Gwen' contains alternate data that documents Freshwater Harmful Algae Blooms in California and Functional Biodiversity in the contiguous USA.
