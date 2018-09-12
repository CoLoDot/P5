"""SCRIPT OF SQL QUERIES FOR OCPIZZA"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import colorama
from colorama import Fore, Back, Style

colorama.init()

CNX = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              database='OPENFOODFACTS',
                              auth_plugin='mysql_native_password')


def menu():  # display main menu
    """ THE MAIN MENU"""
    try:
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + '\n- Sélectionnez la catégorie -')
        cursor = CNX.cursor()
        cursor.execute("SELECT * FROM Category")
        for (id, Produit) in cursor:
            print("{} - {}".format(id, Produit))
    except:
        print(Fore.RED + Back.WHITE + Style.BRIGHT + "Impossible d'afficher le menu.")


def show_category(cat_id):  # show a chosen category
    """ SHOW THE CATEGORY CHOSEN BY THE USER"""
    try:
        cursor = CNX.cursor()
        cursor.execute("SELECT id, nom, marque, nutriscore, url "
                       " FROM Product WHERE produit_id = " + str(cat_id) +
                       " AND NOT nutriscore='unknown'")
        for (id, nom, marque, nutriscore, url) in cursor:
            print("ID : {} NOM : {} MARQUE : {} NUTRISCORE : {} LIEN : {}".format(
                id, nom, marque, nutriscore, url))
    except:
        menu()


def substitutes(cat_id, user_idproduct_choosen):  # find and save a healthier substitute
    """ SUBSTITUTES FUNCTION"""
    try:
        cursor = CNX.cursor()
        cursor.execute("SELECT id, sub, nom, marque, nutriscore, url"
                       " FROM Product WHERE produit_id = " + str(cat_id) +
                       " AND NOT id = " + str(user_idproduct_choosen) + " AND NOT sub > 1"
                                                                        " ORDER BY nutriscore, RAND() LIMIT 1")
        print(Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nNous vous proposons le substitut suivant:")

        result_sub_product = cursor.fetchall()[0]  # gives the substitute
        id_sub = result_sub_product[0]  # gives the id of the substitute in order to save it later
        print(result_sub_product)  # print the substitute

        user_menu = input(Fore.BLACK + Back.CYAN + Style.BRIGHT +
                          '\nVoulez-vous sauvegarder ce substitut ? ' +
                          '(tapez 1, sinon tapez "entrer") : ')

        if user_menu == '1':
            cursor = CNX.cursor()
            # update the table , saving the id of the substitute
            cursor.execute("UPDATE Product SET sub=" + str(id_sub) + " WHERE id=" + str(user_idproduct_choosen))
            CNX.commit()
            print(Fore.BLACK + Back.CYAN + Style.BRIGHT + "Produit sauvegardé !")
    except:
        show_category(cat_id)


def show_saved_products():  # shows saved products
    """ SHOW SAVED PRODUCTS"""

    try:
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + '\n- Mes produits sauvegardés -')

        cursor = CNX.cursor()
        # display on screen all products with a substitute
        cursor.execute(" SELECT id, sub, nom, marque, nutriscore, url FROM Product WHERE sub > 0")
        for (id, sub, nom, marque, nutriscore, url) in cursor:
            print("Votre produit d'origine -> ID : {} SUBSTITUT : {} NOM : {} MARQUE : {} NUTRISCORE : {} LIEN : {}\n".format(
                id, sub, nom, marque, nutriscore, url))

        user_menu = input("\nTapez le numéro du SUBSTITUT que vous désirez afficher ou tapez 'entrer' pour quitter : ")
        if user_menu: # display on screen the substitute choosen for the initial product
            cursor.execute(" SELECT id, nom, marque, nutriscore, url FROM Product WHERE id= "+ str(user_menu))
            for (id, nom, marque, nutriscore, url) in cursor:
                print("Votre substitut -> ID : {} NOM : {} MARQUE : {} NUTRISCORE : {} LIEN : {}\n".format(
                    id, nom, marque, nutriscore, url))
    except:
        print("Impossible d'afficher les produits sauvegardés.")

def stop_program():  # Delete all data and quit
    """ STOP PROGRAM FUNCTION"""
    try:
        cursor = CNX.cursor()
        cursor.execute("DROP TABLE IF EXISTS Product, Category")
        cursor.execute("DROP DATABASE IF EXISTS OPENFOODFACTS")
    except:
        print("Un problème est survenu lors de la suppression des données.")
    finally:
        CNX.close()
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT +
              "\nMerci d'avoir utilisé notre programme. À bientôt.")
