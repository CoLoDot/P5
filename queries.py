#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

# This file includes all functions using MySQL queries

cnx = mysql.connector.connect(user='root', 
		                      password='XXXXXXX', 
		                      host='localhost', 
		                      database= 'OPENFOODFACTS', 
		                      auth_plugin='mysql_native_password')

def menu(): # display main menu
	print('\nSélectionnez la catégorie')
	cursor = cnx.cursor()
	cursor.execute("SELECT * FROM Category")
	for data in cursor:
		print(data)

def show_category(cat_id): # show a chosen category
	cursor = cnx.cursor()
	sql_query = """SELECT `id`, `nom`, `marque`, `nutriscore`, `url` "
						" FROM Product WHERE produit_id = """ + str(cat_id)
	cursor.execute(sql_query)
	for data in cursor:
		print(data)

def substitutes(cat_id, user_input_4): # find and save a healthier substitutes
	cursor = cnx.cursor()
	cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Product WHERE produit_id = "+str(cat_id)+" AND NOT id = "+str(user_input_4)+" AND NOT nutriscore='c' AND NOT nutriscore='d' AND NOT nutriscore='e' AND NOT nutriscore='unknown' ORDER BY RAND() LIMIT 1")
	print("\nNous vous proposons le substitut suivant:")
	for data in cursor:
		print(data)
		user_input = input('\nVoulez-vous sauvegarder ce substitut ? (tapez 1): ')
		if user_input == '1':
			cursor = cnx.cursor()
			sql_query_1 = "INSERT INTO Saved(id, produit_id, nom, marque, nutriscore, url) VALUES (NULL, %s, %s, %s, %s, %s)"
			cursor.execute(sql_query_1, data)
			cnx.commit()
			print("Produit sauvegardé !")

def show_saved_products(): # shows saved products
	print('\nMes produits sauvegardés')
	cursor = cnx.cursor()
	cursor.execute("SELECT * FROM Saved")
	for data in cursor:
		print(data)

def stop_program(): # Delete all data and quit
	cursor = cnx.cursor()
	cursor.execute("DROP TABLE Product")
	cursor.execute("DROP TABLE Saved")
	cursor.execute("DROP TABLE Category")
	cnx.close()
	print("\nMerci d'avoir utilisé notre programme. À bientôt")