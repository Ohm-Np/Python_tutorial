# Exercises

<style> p { text-align: justify; } </style>

At the end of this tutorial, you should have a solid understanding of key geospatial operations in Python, from handling vector and raster data to performing advanced spatial analyses. To ensure that you’ve mastered the concepts and are able to apply the techniques covered, let’s test your skills with the following practical exercises. These tasks will help you reinforce your understanding of spatial data manipulation, analysis, and visualization:

**1. Subset the Kanchanpur district polygon** and extract the region named “Mahendranagar”. Plot the subsetted region to visualize it.

- Use Python libraries like `GeoPandas` to load the shapefile of the Kanchanpur district and extract the region "Mahendranagar" based on its name. Then, visualize this subset using `Matplotlib`.

**2. Compute the area of the Mahendranagar region** in square kilometers and explore its geographic size.

- After subsetting the "Mahendranagar" region, use `GeoPandas` to compute its area. Make sure the data is in a projected coordinate reference system (CRS) to get accurate area calculations, and express the area in square kilometers.

**3. Calculate the perimeter of the Mahendranagar region**, another key geometric property that provides insights into the shape of the region.

- Calculate the perimeter of the Mahendranagar region using `GeoPandas` by accessing the length attribute of the geometry. This helps you understand the shape’s boundaries.

**4. Analyze the change in population** in the Mahendranagar region from the year 2000 to 2020 using zonal statistics and raster data.

- Use `Rasterio` and `Rasterstats` to load population raster data for the years 2000 and 2020. Perform zonal statistics to calculate population changes within the Mahendranagar region by comparing these two rasters.

**5. Create a custom function** that takes polygon and raster data, masks the raster to the polygon’s boundary, converts the masked raster to a data frame, and returns a preview of the data frame.

- Define a Python function that takes both polygon and raster data as inputs. The function will mask the raster to the polygon boundary, convert the masked raster data into a DataFrame, and provide a preview of the first few rows of the DataFrame.

**6. Create a geospatial data frame** consisting of five points (A, B, C, D, and E), and add a new column representing temperature values in Celsius.

- Use `Shapely` to create a geospatial data frame consisting of five points representing locations A, B, C, D, and E. Then, add a new column for the temperature at each point.

**7. Load ESA Land Cover data** for 2015 and 2019, compute and visualize the change raster for the Mahendranagar region, and check the summary statistics to assess the changes in land cover over time.

- Load the `ESA Land Cover` data for 2015 and 2019 using `Rasterio`. Compute the difference between the two rasters to analyze changes in land cover for the Mahendranagar region and visualize the results. Use summary statistics to assess the magnitude of these changes.

**8. Create a function named `get_popCount()`** that takes the ISO3 country code and year as arguments, and downloads the Population Count Raster from the WorldPop Hub. Click here for the [<span style="color:red">source URL</span>](https://hub.worldpop.org/geodata/listing?id=69).

- Write a function that downloads population count raster data based on the ISO3 country code and the specified year from the WorldPop Hub, using the source URL. The function will allow you to access population data for different countries and years programmatically.

These exercises will provide you with hands-on practice in performing common geospatial operations in Python, ensuring you’re well-prepared to handle spatial datasets and solve real-world geographic problems using Python and its geospatial libraries.

If you have any questions or encounter any difficulties while solving these exercises, feel free to visit my [GitHub page](https://github.com/Ohm-Np/Python_tutorial) and open an issue.
