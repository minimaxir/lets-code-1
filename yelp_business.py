import json
import datetime
import csv
import unicodedata

# via http://stackoverflow.com/a/518232
# Necessary to handle Montreal.

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

filename = "yelp_academic_dataset_business.json"


with open('yelp_businesses.csv', 'wb') as file:
	w = csv.writer(file)
	w.writerow(["name","business_id","city","state","categories","stars", "review_count"])
	with open(filename) as f:
		for line in f:
			data = json.loads(line)
			w.writerow([data['name'].encode('utf-8'), data['business_id'], strip_accents(data['city']), data['state'], '|'.join(data['categories']), data['stars'], data['review_count']])
				