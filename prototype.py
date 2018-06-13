#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import mysql.connector
from mysql.connector import errorcode
import logging as lg

lg.basicConfig(level=lg.DEBUG)

# connect to database
cnx = mysql.connector.connect(user='root', 
		                      password='XXXXX', 
		                      host='localhost', 
		                      database= 'OPENFOODFACTS', 
		                      auth_plugin='mysql_native_password')
# create a cursor 
cur = cnx.cursor()

# request to import data from OFF
r = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/1.json')

# return keys of OFF 
if (r.status_code == requests.codes.ok):
        print(r.headers['content-type'])
commit_data = json.loads(r.text)

# Table JSON
table_JSON_page = r.json()
page_size = table_JSON_page[u'page_size'] # return number of products by page
count = table_JSON_page[u'count'] # return number of product by category
total_page_number = int(count/page_size)+1 # return number of pages by category

class Product:
	"""Class Product : get products from OFF, send products to database """
	def __init__(self): # constructor
		self.products_data = [] # create empty list for data from OFF
		print("hello init")

	def get_products_from_OFF(self, products_data): # function to get data with requests' module
		for self.page in range(0, 1):
			self.rpage = requests.get('https://fr.openfoodfacts.org/categorie/jus-d-orange/' + str(page+1) + '.json')
			self.table_JSON_page = self.rpage.json()
			self.products_by_page = self.table_JSON_page[u'products']

			for products in self.products_by_page:
				self.name = products['product_name']
				self.brand = products['brands']
				self.nutriscore = products['nutrition_grades_tags']
				self.url = products['url']
				self.id_produit = '1'

			self.products_data.append([self.name, self.brand, self.nutriscore, self.url, self.id_produit])
			print("Hello get_products_from_OFF")

	def send_products_to_db(self, products_data): # function to send products to databse
		self.query = ("INSERT INTO Orangejuice (nom, marque, nutriscore, url, id_produit) VALUES (%(nom)s, %(marque)s, %(nutriscore)s, %(url)s, %(id_produit)s)")
		self.data_for_db = {
		'nom': self.products_data[12][0],
		'marque': self.products_data[12][1],
		'nutriscore': 'A', # test substitut nutriscore
		'url': self.products_data[12][3],
		'id_produit': '1',
		}
		print("hello send_products_to_db")


print('Quel aliment souhaitez-vous remplacer ? (1) ou retrouver mes aliments substitués (2)')
user_input = input('Indiquez le chiffre correspondant à votre souhait : ')

if user_input == '1': 
	print('Affichage de la table de catégories de produit')
	c = cnx.cursor()
	c.execute("SELECT * FROM Orangejuice")
	for data in c:
		print(data)
	user_input_1 = input('Si vous souhaitez afficher les produits avec un nutriscore supérieur à C tapez appuyez sur 1 :')
	if user_input_1 == '1':
		for data in c:
			c.execute("SELECT `ID_AUTO`, `nom`, `marque`, `nutriscore`, `url`, `id_produit` FROM `Orangejuice` WHERE 'nutriscore'='A'")
		print(data)
	c.close()

if user_input == '2':
	print('Accès à vos produits sauvegardés')

if user_input > '2':
	print('Votre choix de correspond à aucune option')

# Execution of database
#cur.execute(query, data_for_db)
cnx.commit()
cur.close()
