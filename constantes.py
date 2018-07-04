#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


R = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/1.json')
TABLE_JSON_PAGE = R.json()
PAGE_SIZE = TABLE_JSON_PAGE[u'page_size'] # return number of products by page
COUNT = TABLE_JSON_PAGE[u'count'] # return number of product by category
TOTAL_PAGE_NUMBER = int(COUNT/PAGE_SIZE)+1 # return number of pages by category

R2 = requests.get('https://fr.openfoodfacts.org/categorie/pates-a-tartiner-au-chocolat/1.json')
TABLE_JSON_PAGE_2 = R2.json()
PAGE_SIZE_2 = TABLE_JSON_PAGE_2[u'page_size'] # return number of products by page
COUNT_2 = TABLE_JSON_PAGE_2[u'count'] # return number of product by category
TOTAL_PAGE_NUMBER_2 = int(COUNT_2/PAGE_SIZE_2)+1 # return number of pages by category

R3 = requests.get('https://fr.openfoodfacts.org/categorie/biscottes/1.json')
TABLE_JSON_PAGE_3 = R3.json()
PAGE_SIZE_3 = TABLE_JSON_PAGE_3[u'page_size'] # return number of products by page
COUNT_3 = TABLE_JSON_PAGE_3[u'count'] # return number of product by category
TOTAL_PAGE_NUMBER_3 = int(COUNT_3/PAGE_SIZE_3)+1 # return number of pages by category