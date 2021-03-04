#import dependencies
import numpy as np 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

#Setup Database
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
	




#final if statement
if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    # YOUR CODE GOES HERE
     app.run(debug=True)