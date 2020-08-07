# COVID-19-Growth-Trend-Clustering

There is a lot of analysis happening with the various datasets for COVID-19 right now. One of the goals of these analyses is to help figure out which countries are "beating" the pandemic.



Using the publicly available Johns Hopkins COVID-19 data, you'll be performing clustering on time series data for different regions in the world.  Each region is defined by a row in the data set, which can be a country, a province, etc.  The time series data represents the number of (cumulative) confirmed cases on each day.  Because different regions have different onset of the outbreak and differ in magnitude, it is often desirable to convert a raw time series into a  shorter feature vector.  For this assignment, you will represent a time series by two numbers: the "x" and "y" values in the above ten-hundred plot video.   After each region becomes that two-dimensional feature vector, you will cluster all regions with HAC.

Functions:

load_data(filepath) — takes in a string with a path to a CSV file formatted as in the link above, and returns the data (without the lat/long columns but retaining all other columns) in a single structure.
calculate_x_y(time_series) — takes in one row from the data loaded from the previous function, calculates the corresponding x, y values for that region as specified in the video, and returns them in a single structure.
Some x or y can be NaN if the time series doesn't contain enough growth.  
There is a link to Matlab code in the video description on YouTube, please consult that for the precise definition of x and y.
hac(dataset) — performs single linkage hierarchical agglomerative clustering on the regions with the (x,y) feature representation,  and returns a data structure representing the clustering.
