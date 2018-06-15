#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import mysql.connector
from mysql.connector import errorcode
import logging as lg

lg.basicConfig(level=lg.DEBUG)



cnx = mysql.connector.connect(user='root', 
		                      password='XXXXXXXX', 
		                      host='localhost', 
		                      database= 'OPENFOODFACTS', 
		                      auth_plugin='mysql_native_password')
r = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/1.json')
table_JSON_page = r.json()
page_size = table_JSON_page[u'page_size'] # return number of products by page
count = table_JSON_page[u'count'] # return number of product by category
total_page_number = int(count/page_size)+1 # return number of pages by category


class Product:
	"""Class Product : get products from OFF, send products to database """
	def __init__(self): # constructor
		self.products_data = [] # create empty list for data from OFF

	def get_products_from_OFF(self): # function to get data with requests' module
		for self.page in range(0, 10):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/' 
										+ str(self.page+1) + '.json')
			self.table_JSON_page = self.rpage.json()
			self.products_by_page = self.table_JSON_page[u'products']

			for self.products in self.products_by_page:
				self.name = self.products['product_name']
				self.brand = self.products['brands']
				self.nutriscore = self.products['nutrition_grades_tags']
				self.url = self.products['url']
				self.products_data.append([self.name, 
											self.brand, 
											self.nutriscore, 
											self.url])


	def send_products_to_db(self): # function to send products to database
		cursor = cnx.cursor()
		self.data_for_db = {
		'nom': self.products_data[14][0],
		'marque': self.products_data[14][1],
		'nutriscore': self.products_data[14][2][0], 
		'url': self.products_data[14][3],
		}
		
		self.query = ("INSERT INTO Jus_orange "
						"(`id`, `produit_id`, `nom`, `marque`, `nutriscore`, `url`)"
						" VALUES (NULL, '1', %(nom)s, %(marque)s, %(nutriscore)s, %(url)s);")
		
		cursor.execute(self.query, self.data_for_db)

def main():

	X = Product()
	X.get_products_from_OFF()
	X.send_products_to_db()
	
	print('1 - Quel aliment souhaitez-vous remplacer ?')
	print('2 - Retrouver mes aliments substitués')
	user_input = input('Indiquez le chiffre correspondant à votre souhait : ')

	if user_input == '1': 
		print('Affichage de la table de catégories de produit')
		c = cnx.cursor()
		c.execute("SELECT * FROM Produit")
		for data in c:
			print(data)

		
		user_input_1 = input('Si vous souhaitez afficher les produits Jus dorange tapez 1 : ')
		if user_input_1 == '1':
			cursor = cnx.cursor()
			cursor.execute("SELECT * FROM Jus_orange")
			for data_2 in c:
				print(data_2)
				
		c.close()

	if user_input == '2':
		print('Accès à vos produits sauvegardés...')

	if user_input > '2':
		print('Votre choix ne correspond à aucune option !')


if __name__ == '__main__': # Encapsulation of main function
    main()