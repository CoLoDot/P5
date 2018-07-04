#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import mysql.connector
from mysql.connector import errorcode
import logging as lg

from cnx_db import *
from sql import *
from constantes import *
from queries import *
#lg.basicConfig(level=lg.DEBUG)


class Product:
	"""Class Product : get products from OFF, send products to database """
	def __init__(self): # constructor
		self.products_data_orangejuice = [] # create empty list for data from OFF
		self.products_data_chocolatespread = []
		self.products_data_toast = []

	def get_products_from_OFF_orangejuice(self): # method to get data with requests' module
		for self.page in range(0, 3):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE[u'products']

			for self.products in self.products_by_page: # Fill the list of products
				self.id_product_orangejuice = 1
				self.name = self.products['product_name']
				self.brand = self.products['brands']
				self.nutriscore = self.products['nutrition_grades_tags']
				self.url = self.products['url']
				self.products_data_orangejuice.append([self.id_product_orangejuice,
											self.name, 
											self.brand, 
											self.nutriscore[0], 
											self.url])


	def get_products_from_OFF_chocolatespread(self): # method to get data with requests' module
		for self.page in range(0, 3):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/pates-a-tartiner-au-chocolat/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE_2 = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE_2[u'products']

			for self.products in self.products_by_page: # Fill the list of products
				self.id_product_chocolatespread = 2
				self.name = self.products['product_name']
				self.brand = self.products['brands']
				self.nutriscore = self.products['nutrition_grades_tags']
				self.url = self.products['url']
				self.products_data_chocolatespread.append([self.id_product_chocolatespread,
											self.name, 
											self.brand, 
											self.nutriscore[0], 
											self.url])

	def get_products_from_OFF_toast(self): # method to get data with requests' module
		for self.page in range(0, 3):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/biscottes/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE_3 = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE_3[u'products']

			for self.products in self.products_by_page: # Fill the list of products
				self.id_product_toast = 3
				self.name = self.products['product_name']
				self.brand = self.products['brands']
				self.nutriscore = self.products['nutrition_grades_tags']
				self.url = self.products['url']
				self.products_data_toast.append([self.id_product_toast,
											self.name, 
											self.brand, 
											self.nutriscore[0], 
											self.url])

	def send_products_to_db(self): # method to send products to database
		orange_juice = self.products_data_orangejuice[:] # all data from orange juice OFF
		chocolate_spread = self.products_data_chocolatespread[:] # all data from pateatartinerchoco from OFF
		toast = self.products_data_toast[:] # all data from biscottes from OFF
		
		cursor = cnx.cursor()
		cursor.execute("INSERT INTO `Category` (`id`, `Produit`) VALUES (NULL, 'Jus d''orange'), (NULL, 'Pâte à tartiner au chocolat'), (NULL, 'Biscottes')")
		cursor.executemany("INSERT INTO Product(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, %s, %s, %s, %s, %s)", orange_juice)
		cursor.executemany("INSERT INTO Product(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, %s, %s, %s, %s, %s)", chocolate_spread)
		cursor.executemany("INSERT INTO Product(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, %s, %s, %s, %s, %s)", toast)
		cnx.commit()
