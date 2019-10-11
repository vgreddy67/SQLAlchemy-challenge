# SQLAlchemy-challenge
Climate analysis for a vacation to Honolulu.
Used SQLAlchemy ORM queries, Pandas, and Matplotlib for this analysis. Vacation range is 3-15 days. Depending on this range we can choose a start date and end date. SQLite database is used.
Used SQLAlchemy automap_base() to reflect your tables into classes and saved a reference to those classes called Station and Measurement.

Precipitation Analysis:
Designed a query to retrieve the last 12 months of precipitation data. The date and prcp values are only selected.

Loaded the query results into a Pandas DataFrame and set the index to the date column.
The DataFrame values are sorted by date.

Ploted the results using the DataFrame plot method.
![Precipitation]()
