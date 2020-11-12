import os
from flask import Flask
import api
import pprint

pp = pprint.PrettyPrinter()



app= Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
	return ("<h1> You have reached the Treez API Page </h1>")


@app.route('/getCountrySpecificPlant')
def getCountrySpecificPlant():
	return api.get_specific_species("pinus-monticola")
	# return get_specific_species("pinus-monticola")
	# return {"Country_Specific_Plant_1": 1, "Country_Specific_Plant_2": 2}

@app.route('/getRandomPlantFromAnywhere')
def getRandomPlantFromAnywhere():

	return {"Random_Plant": 1}



# Default port:
# if __name__ == '__main__':
#     app.run()

# Or specify port manually:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
