import requests
import pprint

pp = pprint.PrettyPrinter()


ACCESS_TOKEN = "ra7wth1dF-PZdBvp5fkhF32CQO5j9BUnSw7JMQKmZ9M"

HEADERS = {"Authorization": "Bearer {0}".format(ACCESS_TOKEN)}

base_url_plant = "https://trefle.io/api/v1/plants/"
base_url_species = "https://trefle.io/api/v1/species/"
base_url_dist = "https://trefle.io/api/v1/distributions/"


# print (HEADERS)


params = {"filter_not[images]": "null"}



japan = "antarctica/"
test = "achillea-millefolium"


COUNTRY_CODES = {}


def get_all_distributions():
	r = requests.get('https://trefle.io/api/v1/distributions/', headers=headers).json()
	res = {}
	for i in r:
		return

def g_format(res_obj, keys):
	res = {}
	keys = keys
	for i in keys:
		res[i] = res_obj[i]
	return res

def get_specifc_plant(plant_slug):
	r = requests.get(base_url_plant+plant_slug, headers=HEADERS).json()
	print(r["data"].keys())
	g = g_format(r["data"])

	return

def get_specific_species(species_slug):
	r = requests.get(base_url_species+species_slug, headers=HEADERS).json()
	
	fields = ["common_name", "slug", "scientific_name", "year", "author", "family_common_name", "vegetable",
				"image_url", "duration", "edible_part", "edible", "images", "common_names", "distributions", 
				"distribution", "flower", "fruit_or_seed", "specifications", "growth"]
	
	return g_format(r["data"], fields)


def top_tallest_trees():
	r = requests.get("https://trefle.io/api/v1/plants?filter_not%5Bmaximum_height_cm%5D=null&filter%5Bligneous_type%5D=tree&order%5Bmaximum_height_cm%5D=desc", headers=headers).json()
	pp.pprint (r["data"])



def get_plants_from_specifc_country(country_code):
	#japan
	r = requests.get('https://trefle.io/api/v1/distributions/jap/plants', headers=HEADERS).json()
	#denmark
	r = requests.get('https://trefle.io/api/v1/distributions/den/plants', headers=HEADERS).json()
	#finland
	r = requests.get('https://trefle.io/api/v1/distributions/fin/plants', headers=HEADERS).json()
	#sweden
	r = requests.get('https://trefle.io/api/v1/distributions/swe/plants', headers=HEADERS).json()
	#austria
	r = requests.get('https://trefle.io/api/v1/distributions/aut/plants', headers=HEADERS).json()
	#ukraine
	r = requests.get('https://trefle.io/api/v1/distributions/ukr/plants', headers=HEADERS).json()
	#madagascar
	r = requests.get('https://trefle.io/api/v1/distributions/mdg/plants', headers=HEADERS).json()
	#bangladesh
	r = requests.get('https://trefle.io/api/v1/distributions/ban/plants', headers=HEADERS).json()
	res = {}
	pp.pprint(r["data"][2].keys())


# get_specifc_plant("pinus-monticola")
# get_specific_species("pinus-monticola")


# height()
