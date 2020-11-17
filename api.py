import requests
import pprint
import pickle
import random

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
		try:
			res[i] = res_obj[i]
		except:
			print ("Error occured at getting key in g_format")
			pass

	return res

def get_list_of_plants_from_main():
	r = requests.get(base_url_plant, headers=HEADERS).json()
	print(r.keys())
	# pp.pprint(r["data"][8])
	pp.pprint(r["data"])
	print(r["links"])
	print (len(r["data"]))

	return

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




def top_tallest_trees():
	r = requests.get("https://trefle.io/api/v1/plants?filter_not%5Bmaximum_height_cm%5D=null&filter%5Bligneous_type%5D=tree&order%5Bmaximum_height_cm%5D=desc", headers=headers).json()
	pp.pprint (r["data"])


def get_specifc_plant(plant_slug):
	r = requests.get(base_url_plant+plant_slug, headers=HEADERS).json()
	print(r.keys())
	pp.pprint(r["data"])

	return


def get_tree_slug_list(count):
	
	fields = ["common_name", "slug", "scientific_name", "year", "author", "family_common_name",
				"image_url", "duration", "edible_part", "edible", "images", "common_names", 
				"distribution", "flower", "specifications", "growth"]
	final_list = []
	if (count == 1):
		
		INITIAL_PARAMS = {"filter_not[images]": "null"}
		r = requests.get(base_url_species, params=INITIAL_PARAMS,headers=HEADERS).json()

	else:
		INITIAL_PARAMS = {"filter_not[images]": "null", "page": 2 }
		r = requests.get(base_url_species, params=INITIAL_PARAMS,headers=HEADERS).json()

	for i in r["data"]:
		final_list.append(i["slug"])


	return {"random20plants": final_list}



def get_slugs_in_list():
	final_list = []

	INITIAL_PARAMS = {"filter_not[images]": "null"}
	r = requests.get(base_url_species, params=INITIAL_PARAMS,headers=HEADERS).json()

	for i in r["data"]:
		final_list.append(i["slug"])

	for j in range(2, 50, 1):
		INITIAL_PARAMS = {"filter_not[images]": "null", "page": j }
		r = requests.get(base_url_species, params=INITIAL_PARAMS,headers=HEADERS).json()
		#adding all the slugs to final list from each page request
		for k in r["data"]:
			final_list.append(k["slug"])

	with open("./slugList.txt", "wb") as fp:
		pickle.dump(final_list, fp)

	return final_list



def get_specific_species(species_slug):
	print ("Slug delivered: " + species_slug)
	r = requests.get(base_url_species+species_slug, headers=HEADERS)
	print (r)
	r = r.json()
	
	fields = ["common_name", "slug", "scientific_name", "year", "author", "family_common_name", "vegetable",
				"image_url", "duration", "edible_part", "edible", "images", "common_names", 
				"distribution", "flower", "fruit_or_seed", "specifications", "growth"]
	
	res = g_format(r["data"], fields)

	if res["image_url"] is None:
		r = requests.get(base_url_species+"juniperus-communis-var-communis", headers=HEADERS)
		r = r.json()

	res = g_format(r["data"], fields)
	

	if isinstance(res["common_names"], list):
		print ("GOT a LIST in COMMON NAMES")
		print (res["common_names"])
	
	if isinstance(res["common_names"], dict):
		
		t = res["common_names"].keys()
		if ("eng" in t):
			res["common_names"] = res["common_names"]["eng"]

		elif ("en" in t):
			res["common_names"] = res["common_names"]["en"]

	# if common_name field is empty get the first one from common_names and remove it
	# or if common_name is there and the first of common_names is the same as common_name
	# remove it
	if res["common_name"] is None:
		print ("got in none")
		res["common_name"] = res["common_names"].pop(0)
	elif res["common_name"].lower() == res["common_names"][0].lower():
		print ("got in both first equal")
		res["common_names"].pop(0)
	
	if isinstance(res["distribution"], list):
		print (res["distribution"])
		res["distribution"].sort()
		print ("GOTCHA in DIST")

	if isinstance(res["distribution"], dict):
		if "native" in res["distribution"].keys():
			res["distribution"] = res["distribution"]["native"]
			res["distribution"].sort()

	if "cm" in res["specifications"]["maximum_height"].keys():
		res["max_height"] = res["specifications"]["maximum_height"]["cm"]


	return res






def load_slugs():
	with open("./slugList.txt", "rb") as fp:
		k = pickle.load(fp)
		print (type(k))
	print (random.sample(k, 1))


