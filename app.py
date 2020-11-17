import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import api
import pprint
import pickle
import random

pp = pprint.PrettyPrinter()


app= Flask(__name__)
CORS(app)
app.config.from_object('config', )
app.config["CORS_HEADERS"] = "Content-Type"

def load_slugs():
	with open("./slugList.txt", "rb") as fp:
		k = pickle.load(fp)
		return k

SLUG_LIST = load_slugs()

@app.route('/')
def index():
	return ("<h1> You have reached the Treez API Page </h1>")


@app.route('/getTreeSlug')
@cross_origin()
def getTreeSlug():
	return {"slug": random.sample(SLUG_LIST, 1)[0]}

@app.route('/getSpecificSpecies')
@cross_origin()
def getCountrySpecificPlant():
	try:
		recSlug = str(request.args.get("slug"))
		print (recSlug)
	except:
		#change with a better looking species
		return api.get_specific_species("juniperus-communis-var-communis")

	return api.get_specific_species(recSlug)


@app.route('/testAnotherButton')
def testAnotherButton():
	return api.get_specific_species("holcus-lanatus")

@app.route('/getRandomPlantFromAnywhere')
def getRandomPlantFromAnywhere():

	return {"Random_Plant": 1}



# Default port:
# if __name__ == '__main__':
#     app.run()

# Or specify port manually:

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3035))
    app.run(host='0.0.0.0', port=port)
