import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#inspect the tables metadata
inspector = inspect(engine)

# Create our session (link) from Python to the DB
session = Session(engine)

max_date = session.query(func.max(Measurement.date)).scalar()

strt_date = dt.datetime.strptime(max_date,'%Y-%m-%d') - dt.timedelta(days=365)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precepitation():
    """Return a dicionary of dates and precipitation"""
    # Start the session
    session = Session(engine)
    
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= strt_date).all()

    #Create a dictionary from the query data with 'Date' as the key and 'prcp' as the value
    days_prceipitation = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Prcp"] = prcp
        
        days_prceipitation.append(prcp_dict)
        
    return jsonify(days_prceipitation)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
    session = Session(engine)
    
    results = session.query(Station.station).all()

    stations_lst = list(map(''.join,results))
    return jsonify(stations_lst)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of tobs in the previous year from last registered tobs day"""
    session = Session(engine)
    
    results = session.query(Measurement.date,Measurement.tobs).\
                filter(Measurement.date >= strt_date).all()

    prev_year_temps = []
    # prev_year_temps = list(np.ravel(results))
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["tobs"] = tobs
        
        prev_year_temps.append(tobs_dict)

    return jsonify(prev_year_temps)


@app.route("/api/v1.0/<start>")
def agg_by_start_date(start):
    """Return a tmin,tavg,tmax for all days after start date"""
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()

    agg_vals = []
    for tmin, tavg, tmax in results:
        agg_dict = {}
        agg_dict["MinTemp"] = tmin
        agg_dict["AvgTemp"] = tavg
        agg_dict["MaxTemp"] = tmax

        agg_vals.append(agg_dict)

    return jsonify(agg_vals)

@app.route("/api/v1.0/<start>/<end>")
def agg_by_start_end_date(start,end):
    """Return a tmin,tavg,tmax for all days between start date and end date"""
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    agg_vals = []
    for tmin, tavg, tmax in results:
        agg_dict = {}
        agg_dict["MinTemp"] = tmin
        agg_dict["AvgTemp"] = tavg
        agg_dict["MaxTemp"] = tmax

        agg_vals.append(agg_dict)

    return jsonify(agg_vals)


if __name__ == '__main__':
    app.run(debug=True)
