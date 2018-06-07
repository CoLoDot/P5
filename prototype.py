#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
#import mysql.connector
#from mysql.connector import errorcode
import logging as lg

#lg.basicConfig(level=lg.DEBUG)

r = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/1.json')

# AFFICHAGE DES CLEFS DU DICTIONNAIRE OPENFOODFACT
if (r.status_code == requests.codes.ok):
        print(r.headers['content-type'])
commit_data = json.loads(r.text)
print(commit_data.keys())
# FIN DE L'AFFICHAGE

# Table JSON
table_JSON_page = r.json()

page_size = table_JSON_page[u'page_size']
# 20 produits par page

count = table_JSON_page[u'count']
# 531 produits

total_page_number = int(count/page_size)+1
# 27

products_data = [] #list for datas from OFF
for page in range(0, total_page_number):
	rpage = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/' + str(page+1) + '.json')
	table_JSON_page = rpage.json()
	products_by_page = table_JSON_page[u'products']

	for products in products_by_page:
		name = products['product_name']
		nutriscore = products['nutrition_grades_tags']
		brand = products['brands']
		url = products['url']

		products_data.append(name)
		products_data.append(nutriscore)
		products_data.append(brand)
		products_data.append(url)

print(products_data)

#for test in enumerate(products_data):
	#print(test)