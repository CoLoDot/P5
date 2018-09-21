"""SCRIPT OF SQL QUERIES FOR OCPIZZA"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from const_msg import *
from user_param import *

CNX = mysql.connector.connect(user=USER_NAME,
                              password=USER_PASSWORD,
                              host=USER_HOST,
                              database=DB_NAME,
                              auth_plugin=PASSWORD_TYPE)


def menu():  # display main menu
    """ THE MAIN MENU"""
    try:
        print(SELECT_CAT)
        cursor = CNX.cursor()
        cursor.execute("SELECT * FROM Category")
        for (id, Produit) in cursor:
            print("{} - {}".format(id, Produit))
    except:
        print(PROBLEM_CAT_MENU)


def show_category(cat_id):  # show a chosen category
    """ SHOW THE CATEGORY CHOSEN BY THE USER"""
    try:
        cursor = CNX.cursor()
        cursor.execute("SELECT id, nom, marque, shop, nutriscore, url "
                       " FROM Product WHERE produit_id = " + str(cat_id) +
                       " AND NOT nutriscore='unknown'")
        for (id, nom, marque, shop, nutriscore, url) in cursor:
            print("ID : {} NOM : {} MARQUE : {} MAGASIN : {} NUTRISCORE : {} LIEN : {}".format(
                id, nom, marque, shop, nutriscore, url))
    except:
        menu()


def substitutes(cat_id, user_idproduct_choosen):  # find and save a healthier substitute
    """ SUBSTITUTES FUNCTION"""
    try:
        cursor = CNX.cursor()
        cursor.execute("SELECT id, sub, nom, marque, shop, nutriscore, url"
                       " FROM Product WHERE produit_id = " + str(cat_id) +
                       " AND NOT id = " + str(user_idproduct_choosen) + " AND NOT sub > 1"
                                                                        " ORDER BY nutriscore, RAND() LIMIT 1")
        print(SUB_RESULT)

        result_sub_product = cursor.fetchall()[0]  # gives the substitute
        id_sub = result_sub_product[0]  # gives the id of the substitute in order to save it later
        print(result_sub_product)  # print the substitute

        user_menu = input(SAVE_SUB)

        if user_menu == '1':
            cursor = CNX.cursor()
            # update the table , saving the id of the substitute
            cursor.execute("UPDATE Product SET sub=" + str(id_sub) + " WHERE id=" + str(user_idproduct_choosen))
            CNX.commit()
            print(SUB_SAVED_CONFIRMATION)
    except:
        show_category(cat_id)


def show_saved_products():  # shows saved products
    """ SHOW SAVED PRODUCTS"""

    try:
        print(SUB_SAVED_MENU)

        cursor = CNX.cursor()
        # display on screen all products with a substitute
        cursor.execute(" SELECT id, sub, nom, marque, shop, nutriscore, url FROM Product WHERE sub > 0")
        for (id, sub, nom, marque, shop, nutriscore, url) in cursor:
            print("Votre produit d'origine -> ID : {} SUBSTITUT : {} NOM : {} MARQUE : {} "
                  "MAGASIN : {} NUTRISCORE : {} LIEN : {}\n".format(id, sub, nom, marque, shop, nutriscore, url))

        user_menu = input(ENTER_IDSUB_NUMBER_WANTED)
        if user_menu: # display on screen the substitute choosen for the initial product
            cursor.execute(" SELECT id, nom, marque, shop, nutriscore, url FROM Product WHERE id= "+ str(user_menu))
            for (id, nom, marque, shop, nutriscore, url) in cursor:
                print("Votre substitut -> ID : {} NOM : {} MARQUE : {} MAGASIN : {} NUTRISCORE : {} LIEN : {}\n".format(
                    id, nom, marque, shop, nutriscore, url))
    except:
        print(PROBLEM_SUB_MENU)

def stop_program():  # Delete all data and quit
    """ STOP PROGRAM FUNCTION"""
    try:
        cursor = CNX.cursor()
        cursor.execute("DROP TABLE IF EXISTS Product, Category")
        cursor.execute("DROP DATABASE IF EXISTS OPENFOODFACTS")
    except:
        print(PROBLEM_DB_SUPPR)
    finally:
        CNX.close()
        print(GOODBYE_MSG)
