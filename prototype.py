#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import mysql.connector
from mysql.connector import errorcode
import logging as lg

#lg.basicConfig(level=lg.DEBUG)



cnx = mysql.connector.connect(user='root', 
		                      password='XXXXXXXXX', 
		                      host='localhost', 
		                      database= 'OPENFOODFACTS', 
		                      auth_plugin='mysql_native_password')

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
		for self.page in range(0, TOTAL_PAGE_NUMBER_2):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/pates-a-tartiner-au-chocolat/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE_2 = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE_2[u'products']

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
		for self.page in range(0, TOTAL_PAGE_NUMBER_3):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/biscottes/' 
										+ str(self.page+1) + '.json')
			self.TABLE_JSON_PAGE_3 = self.rpage.json()
			self.products_by_page = self.TABLE_JSON_PAGE_3[u'products']

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
		orange_juice = self.products_data_orangejuice[:] # all data from orange juice OFF
		pate_a_tartiner = self.products_data_pateatartinerchoco[:] # all data from pateatartinerchoco from OFF
		biscottes = self.products_data_biscottes[:] # all data from biscottes from OFF
		cursor = cnx.cursor()
		cursor.executemany("INSERT INTO Jus_orange(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, '1', %s, %s, %s, %s)", orange_juice)
		cursor.executemany("INSERT INTO Pate_a_tartiner(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, '2', %s, %s, %s, %s)", pate_a_tartiner)
		cursor.executemany("INSERT INTO Biscottes(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, '3', %s, %s, %s, %s)", biscottes)
		cnx.commit()


	

def main(): # Main function

	print("Nous accèdons à la base de données, merci de patienter.")
	print("Chargement en cours...")

	#program = True
	new_product = Product()
	new_product.get_products_from_OFF_orangejuice()
	new_product.get_products_from_OFF_pateatartinerchoco()
	new_product.get_products_from_OFF_biscottes()
	new_product.send_products_to_db()
	
	print('1 - Quel aliment souhaitez-vous remplacer ?')
	print('2 - Retrouver mes aliments substitués')
	user_input = input('Indiquez le chiffre correspondant à votre souhait : ')

	#while program:

	if user_input == '1': # Show table "Produit"
		print('Sélectionnez la catégorie')
		c = cnx.cursor()
		c.execute("SELECT * FROM Produit")
		for data in c:
			print(data)

		
		user_input_1 = input('Tapez le numéro correspondant à la catégorie que vous désirez afficher : ')
		if user_input_1 == '1': # Show table "Jus d'orange"
			cursor = cnx.cursor()
			cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Jus_orange WHERE NOT nutriscore='unknown'")
			for data_2 in c:
				print(data_2)
			user_input_4 = input('Sélectionnez l\'aliment (tapez le numéro qui lui est attribué et appuyez sur entrée) : ')
			if user_input_4 == '2': #input doit être égal au numéro de produit entré par le client
				cursor = cnx.cursor()
				cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Jus_orange WHERE NOT nutriscore='c' AND NOT nutriscore='d' AND NOT nutriscore='e' AND NOT nutriscore='unknown' ORDER BY id LIMIT 1")
				print("Nous vous proposons le subsitut suivant:")
				for data_5 in c:
					print(data_5)

				# en test ####
				user_input_6 = input('Souhaitez-vous effacer les données ? (tapez Q) :')
				if user_input_6 == 'q':
					cursor = cnx.cursor()
					cursor.execute("DELETE FROM `Jus_orange` WHERE 0")

		if user_input_1 == '2': # Show table "Pâte à tartiner"
			cursor = cnx.cursor()
			cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Pate_a_tartiner WHERE NOT nutriscore='unknown'")
			for data_3 in c:
				print(data_3)
			user_input_4 = input('Voulez-vous afficher les produits avec un nustricore supérieur à C ? (tapez 2 si oui): ')
			if user_input_4 == '2':
				cursor = cnx.cursor()
				cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Pate_a_tartiner WHERE NOT nutriscore='c' AND NOT nutriscore='d' AND NOT nutriscore='e' AND NOT nutriscore='unknown' ORDER BY id LIMIT 1")
				for data_5 in c:
					print(data_5)

		if user_input_1 == '3': # Show table "Biscottes"
			cursor = cnx.cursor()
			cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Biscottes WHERE NOT nutriscore='unknown'")
			for data_4 in c:
				print(data_4)
			user_input_4 = input('Voulez-vous afficher les produits avec un nustricore supérieur à C ? (tapez 2 si oui): ')
			if user_input_4 == '2':
				cursor = cnx.cursor()
				cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Biscottes WHERE NOT nutriscore='c' AND NOT nutriscore='d' AND NOT nutriscore='e' AND NOT nutriscore='unknown' ORDER BY id LIMIT 1")
				for data_5 in c:
					print(data_5)
		

	if user_input == '2': # Show saved products
		print('Accès à vos produits sauvegardés...')

	if user_input > '2': # return questions until right's answers
		print('Votre choix ne correspond à aucune option !')

	#print("Souhaitez-vous quitter le programme ? Tapez Q")
	#if user_input_5 == "q":
	#	program = False

if __name__ == '__main__': # Encapsulation of main function
    main()