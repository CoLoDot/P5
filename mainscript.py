#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import mysql.connector
from mysql.connector import errorcode
import logging as lg
import colorama
from colorama import Fore, Back, Style

from create_db import *
from cnx_db import *
from sql import *
from queries import *
from constantes import *
from feed_in import *

# lg.basicConfig(level=lg.DEBUG)
colorama.init()


def main():  # Main function

    print(Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nChargement en cours...")

    program = True
    new_product = Product()
    new_product.get_products_from_off()
    new_product.send_products_to_db()

    while program:  # Main loop
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "\n- Menu -" +
              "\n1 - Quel aliment souhaitez-vous remplacer ?" +
              "\n2 - Retrouver mes aliments substitués" +
              "\n3 - Quitter le programme")
        menu_input = input(
            Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nEntrez le chiffre correspondant à votre souhait : ")

        if menu_input == '1':  # Show main menu
            menu()
            cat_id = input(Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nEntrez le chiffre correspondant à la " +
                           "catégorie que vous désirez afficher : ")
            if cat_id <= '3':  # Show the chosen category among cat id
                show_category(cat_id)
                user_idproduct_choosen = input(
                    Fore.WHITE + Back.BLACK + Style.BRIGHT + "\nTapez l\'ID attribué au " +
                    "produit pour afficher une proposition de substitut : ")
                if user_idproduct_choosen:  # Save a substitute
                    substitutes(cat_id, user_idproduct_choosen)

        if menu_input == '2':  # Show saved products
            saving_products = True
            while saving_products:
                show_saved_products()
                saved_menu = input("\nVoulez-vous afficher d'autres substituts ? (tapez 'entrer' sinon tapez 1) : ")
                if saved_menu == '1':
                    saving_products = False

        if menu_input == '3':  # Quit program and delete all data
            stop_program()
            program = False


if __name__ == '__main__':  # Encapsulation of main function
    main()
