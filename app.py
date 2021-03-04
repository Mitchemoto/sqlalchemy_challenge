#import dependencies
import numpy as np 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base=automap_base()
# reflect the tables
Base.prepare(engine,reflect=True)

# Save references to each table
Measurement=Base.classes.measurement
Station=Base.classes.station

#################################################
# Flask Setup
#################################################
# @TODO: Initialize your Flask app here
app=Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
	return(
		#List all routes that are available.
		f"You have arrived to the SQL Alchemy API!<br/>"
		f"Here are the avilable routes:<br/>"
		f"/api/v1.0/precipitation<br/>"
		f"/api/v1.0/stations<br/>"
		f"/api/v1.0/tobs<br/>"
		f"/api/v1.0/<start><br/>"
		f"/api/v1.0/<start>/<end><br/>")
	
@app.route("/api/v1.0/precipitation")
def percipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #query all data from start date forward
    results=session.query(Measurement.date,Measurment.prcp)\
    	.filter(Measurement.date>="2016-08-23").all()

    session.close()

    #Convert the query results to a dictionary using 
    #date as the key and prcp as the value.
    all_prcp=[]
    for date,prcp in results:
    	prcp_dict={}
    	prcp_dict['date']=date
    	prcp_dict['prcp']=prcp
    	all_prcp.append(prcp_dict)

    #Return the JSON representation of your dictionary.
    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #query all stations
    results=session.query(Station.station).order_by(Station.station).all()

    session.close()

    #convert to normal list
    all_stations=list(np.ravel(results))

    #Return the JSON representation
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #query all tobs
    results=session.query(Measurement.date,Measurement.prcp,Measurement.tobs)\
    	.filter(Measurement.date>="2016-08-23")\
    	.filter(Measurement.station=='USC00519281')\
    	.order_by(Measurement.date).all()

    session.close()

    # Return a JSON list of temperature observations (TOBS) for the previous year.
    all_tobs=[]
    for date, prcp, tobs in results:
    	tobs_dict={}
    	tobs_dict['date']=date
    	tobs_dict['prcp']=prcp
    	tobs_dict['tobs']=tobs
    	all_tobs.append(tobs_dict)

    return jsonify(all_tobs)


#final if statement
if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    # YOUR CODE GOES HERE
     app.run(debug=True)