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
from OFFclass import *
#lg.basicConfig(level=lg.DEBUG)


def main(): # Main function

	print("\nNous accèdons à la base de données, merci de patienter.")
	print("Chargement en cours...\n")

	program = True
	new_product = Product()
	new_product.get_products_from_OFF_orangejuice()
	new_product.get_products_from_OFF_chocolatespread()
	new_product.get_products_from_OFF_toast()
	new_product.send_products_to_db()
	
	while program: # Main loop
		print("\n1 - Quel aliment souhaitez-vous remplacer ?"+
			  "\n2 - Retrouver mes aliments substitués"+
			  "\n3 - Quitter le programme")
		user_input = input('\nIndiquez le chiffre correspondant à votre souhait: ')

		if user_input == '1': # Show main menu
			menu()
			cat_id = input('\nEntrez le chiffre correspondant à la '+ 
								  'catégorie que vous désirez afficher : ')
			if cat_id <= '3': # Show the chosen category
				show_category(cat_id)
				user_input_4 = input('\nTapez le numéro attribué au'+ 
									  'produit pour afficher un substitut: ')
				if user_input_4: # Save a substitute
					substitutes(cat_id, user_input_4)

		if user_input == '2': # Show saved products
			show_saved_products()

		if user_input == '3': # Quit program and delete all data
			stop_program()
			program = False

if __name__ == '__main__': # Encapsulation of main function
    main()