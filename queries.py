#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='root', 
		                      password='XXXXXXX', 
		                      host='localhost', 
		                      database= 'OPENFOODFACTS', 
		                      auth_plugin='mysql_native_password')
		                      
# This file includes all functions using MySQL queries

def menu(): # display main menu
	try:
		print('\n- Sélectionnez la catégorie -')
		cursor = cnx.cursor()
		cursor.execute("SELECT * FROM Category")
		for data in cursor:
			print(data)
	except:
		print("Impossible d'afficher le menu.")

def show_category(cat_id): # show a chosen category
	try:
		cursor = cnx.cursor()
		cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` "
							" FROM Product WHERE produit_id = " + str(cat_id)+
							" AND NOT nutriscore='unknown'")
		for data in cursor:
			print(data)
	except:
		menu()
		

def substitutes(cat_id, user_input_4): # find and save a healthier substitute
	try:
		cursor = cnx.cursor()
		cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` "
							"FROM Product WHERE produit_id = "+str(cat_id)+
							" AND NOT id = "+str(user_input_4)+
							" AND NOT nutriscore='c' AND NOT nutriscore='d' "
							"AND NOT nutriscore='e' AND NOT nutriscore='unknown' "
							"ORDER BY RAND() LIMIT 1")
		print("\nNous vous proposons le substitut suivant:")
		for data in cursor:
			print(data)
			user_input = input('\nVoulez-vous sauvegarder ce substitut ? '+
								'(tapez 1, sinon tapez sur "entrer"): ')
			if user_input == '1':
				cursor = cnx.cursor()
				cursor.execute("INSERT INTO Saved(id, produit_id, nom, marque, nutriscore, url) "
									"VALUES (NULL, %s, %s, %s, %s, %s)", data)
				cnx.commit()
				print("Produit sauvegardé !")
	except:
		show_category(cat_id)

def show_saved_products(): # shows saved products	
	cursor = cnx.cursor()
	cursor.execute("SELECT `id`, `nom`, `marque`, `nutriscore`, `url` FROM Saved")
	print('\n- Mes produits sauvegardés -')
	for row in cursor:
		print(row)

def stop_program(): # Delete all data and quit
	try:
		cursor = cnx.cursor()
		cursor.execute("DROP TABLE IF EXISTS Product, Saved, Category")
		cursor.execute("DROP DATABASE IF EXISTS `OPENFOODFACTS`")
	except:
		print("Un problème est survenu lors de la suppression des données.")
	finally:
		cnx.close()
		print("\nMerci d'avoir utilisé notre programme. À bientôt")