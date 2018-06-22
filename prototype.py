#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import mysql.connector
from mysql.connector import errorcode
import logging as lg

#lg.basicConfig(level=lg.DEBUG)



cnx = mysql.connector.connect(user='root', 
		                      password='XXXXXXXX', 
		                      host='localhost', 
		                      database= 'OPENFOODFACTS', 
		                      auth_plugin='mysql_native_password')

R = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/1.json')
TABLE_JSON_PAGE = R.json()
PAGE_SIZE = TABLE_JSON_PAGE[u'page_size'] # return number of products by page
COUNT = TABLE_JSON_PAGE[u'count'] # return number of product by category
TOTAL_PAGE_NUMBER = int(COUNT/PAGE_SIZE)+1 # return number of pages by category


class Product:
	"""Class Product : get products from OFF, send products to database """
	def __init__(self): # constructor
		self.products_data_orangejuice = [] # create empty list for data from OFF
		self.products_data_pateatartinerchoco = []
		self.products_data_biscottes = []

	def get_products_from_OFF_orangejuice(self): # method to get data with requests' module
		for self.page in range(0, TOTAL_PAGE_NUMBER):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE[u'products']

			for self.products in self.products_by_page: # Fill the list of products
				self.name = self.products['product_name']
				self.brand = self.products['brands']
				self.nutriscore = self.products['nutrition_grades_tags']
				self.url = self.products['url']
				self.products_data_orangejuice.append([self.name, 
											self.brand, 
											self.nutriscore[0], 
											self.url])


	def get_products_from_OFF_pateatartinerchoco(self): # method to get data with requests' module
		for self.page in range(0, 18):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/pates-a-tartiner-au-chocolat/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE[u'products']

			for self.products in self.products_by_page: # Fill the list of products
				self.name = self.products['product_name']
				self.brand = self.products['brands']
				self.nutriscore = self.products['nutrition_grades_tags']
				self.url = self.products['url']
				self.products_data_pateatartinerchoco.append([self.name, 
											self.brand, 
											self.nutriscore[0], 
											self.url])

	def get_products_from_OFF_biscottes(self): # method to get data with requests' module
		for self.page in range(0, 11):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/biscottes/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE[u'products']

			for self.products in self.products_by_page: # Fill the list of products
				self.name = self.products['product_name']
				self.brand = self.products['brands']
				self.nutriscore = self.products['nutrition_grades_tags']
				self.url = self.products['url']
				self.products_data_biscottes.append([self.name, 
											self.brand, 
											self.nutriscore[0], 
											self.url])

	def send_products_to_db(self): # method to send products to database
		orange_juice = self.products_data_orangejuice[:]
		pate_a_tartiner = self.products_data_pateatartinerchoco[:]
		biscottes = self.products_data_biscottes[:]
		cursor = cnx.cursor()
		cursor.executemany("INSERT INTO Jus_orange(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, '1', %s, %s, %s, %s)", orange_juice)
		cursor.executemany("INSERT INTO Pate_a_tartiner(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, '2', %s, %s, %s, %s)", pate_a_tartiner)
		cursor.executemany("INSERT INTO Biscottes(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, '3', %s, %s, %s, %s)", biscottes)
		cnx.commit()


	

def main(): # Main function

	print("Nous accèdons à la base de données, merci de patienter.")
	print("Chargement en cours...")
	X = Product()
	X.get_products_from_OFF_orangejuice()
	X.get_products_from_OFF_pateatartinerchoco()
	X.get_products_from_OFF_biscottes()
	X.send_products_to_db()
	
	print('1 - Quel aliment souhaitez-vous remplacer ?')
	print('2 - Retrouver mes aliments substitués')
	user_input = input('Indiquez le chiffre correspondant à votre souhait : ')

	if user_input == '1': # Show table "Produit"
		print('Affichage de la table de catégories de produit')
		c = cnx.cursor()
		c.execute("SELECT * FROM Produit")
		for data in c:
			print(data)

		
		user_input_1 = input('Tapez le numéro correspondant aux produits que vous désirez afficher : ')
		if user_input_1 == '1': # Show table "Jus d'orange"
			cursor = cnx.cursor()
			cursor.execute("SELECT * FROM Jus_orange")
			for data_2 in c:
				print(data_2)
				
			#récupérer d'abord un produit 
			#puis faire une requête 

			user_input_4 = input('Voulez-vous afficher les produits avec un nustricore supérieur à C ? (tapez 2 si oui): ')
			if user_input_4 == '2':
				cursor = cnx.cursor()
				cursor.execute("SELECT * FROM Jus_orange WHERE nutriscore = 'a' OR 'b'")
				for data_5 in c:
					print(data_5)

		if user_input_1 == '2': # Show table "Pâte à tartiner"
			cursor = cnx.cursor()
			cursor.execute("SELECT * FROM Pate_a_tartiner")
			for data_3 in c:
				print(data_3)

		if user_input_1 == '3': # Show table "Biscottes"
			cursor = cnx.cursor()
			cursor.execute("SELECT * FROM Biscottes")
			for data_4 in c:
				print(data_4)
		

	if user_input == '2':
		print('Accès à vos produits sauvegardés...')

	if user_input > '2':
		print('Votre choix ne correspond à aucune option !')


if __name__ == '__main__': # Encapsulation of main function
    main()