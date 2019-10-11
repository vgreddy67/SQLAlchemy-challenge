# SQLAlchemy-challenge
Climate analysis for a vacation to Honolulu.
Used SQLAlchemy ORM queries, Pandas, and Matplotlib for this analysis. Vacation range is 3-15 days. Depending on this range we can choose a start date and end date. SQLite database is used.
Used SQLAlchemy automap_base() to reflect your tables into classes and saved a reference to those classes called Station and Measurement.

Precipitation Analysis:
Designed a query to retrieve the last 12 months of precipitation data. The date and prcp values are only selected.

Loaded the query results into a Pandas DataFrame and set the index to the date column.
The DataFrame values are sorted by date.

Ploted the results using the DataFrame plot method.

![Precipitation](Instructions/Images/precipitation.png)

Station Analysis:

Designed a query to calculate the total number of stations.

Designed a query to find the most active stations.

Listed the stations and observation counts in descending order.

Used functions such as func.min, func.max, func.avg, and func.count in the queries to find which station has the highest number of observations.

Designed a query to retrieve the last 12 months of temperature observation data (tobs).

Filtered by the station with the highest number of observations.

Ploted the results as a histogram with bins=12.

![Histogram](Instructions/Images/Station%20Histogram.png)

