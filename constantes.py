#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" SCRIPT "constantes" for OC PIZZA """
import requests

# IF YOU WANT TO ADD A CATEGORY PLEASE FILL THE DICT
CAT_DICT = {1: 'https://fr.openfoodfacts.org/categorie/jus-d-orange/',
            2: 'https://fr.openfoodfacts.org/categorie/pates-a-tartiner-au-chocolat/',
            3: 'https://fr.openfoodfacts.org/categorie/biscottes/'}

NUTRI_DICT = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

for key, value in CAT_DICT.items():
    if key:
        R = requests.get(value + '1.json')
        TABLE_JSON_PAGE = R.json()
        PAGE_SIZE = TABLE_JSON_PAGE[u'page_size']  # return number of products by page
        COUNT = TABLE_JSON_PAGE[u'count']  # return number of product by category
        TOTAL_PAGE_NUMBER = int(COUNT / PAGE_SIZE) + 1  # return number of pages by category
