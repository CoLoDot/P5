#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import mysql.connector
from mysql.connector import errorcode
import colorama
from colorama import Fore, Back, Style

colorama.init()

from constantes import *

cnx = mysql.connector.connect(user='root',
                              password='cocotte4978',
                              host='localhost',
                              database='OPENFOODFACTS',
                              auth_plugin='mysql_native_password')


class Product:
    """Class Product : get products from OFF, send products to database """

    def __init__(self):  # constructor
        self.products_data = []

    def get_products_from_off(self):  # method to get data with requests' module
        try:
            for page in range(0, 1):
                for key, value in CAT_DICT.items():
                    if key:
                        rpage = requests.get(value + str(page + 1) + '.json')
                        TABLE_JSON_PAGE = rpage.json()
                        products_by_page = TABLE_JSON_PAGE[u'products']

                        for products in products_by_page:  # Fill the list of products

                            id_product = key
                            sub = 0
                            name = products['product_name']
                            brand = products['brands']

                            nutri_origin = products['nutrition_grades_tags'][0]
                            for key_nutri, value_nutri in NUTRI_DICT.items():
                                if nutri_origin == value_nutri:
                                    nutriscore = key_nutri

                            url = products['url']
                            self.products_data.append([id_product,
                                                       sub,
                                                       name,
                                                       brand,
                                                       nutriscore,
                                                       url])
        except:
            print(Fore.RED + Back.WHITE + Style.BRIGHT +
                  "Un problème est survenu lors de la " +
                  "récupération des produits.")

    def send_products_to_db(self):  # method to send products to database
        try:
            data = self.products_data[:]  # all data got from OFF
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO `Category` (`id`, `Produit`) "
                           "VALUES (NULL, 'Jus d''orange'), "
                           "(NULL, 'Pâte à tartiner au chocolat'),"
                           "(NULL, 'Biscottes')")
            cursor.executemany("INSERT INTO Product(id, produit_id, sub, nom, marque, nutriscore, url) "
                               "VALUES (NULL, %s, %s, %s, %s, %s, %s)", data)
            cnx.commit()
        except:
            print(Fore.RED + Back.WHITE + Style.BRIGHT +
                  "Un problème est survenu lors de l'insertion des données dans la BDD.")
