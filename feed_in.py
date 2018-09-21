#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import mysql.connector

from mysql.connector import errorcode
from constantes import *
from const_msg import *
from user_param import *

CNX = mysql.connector.connect(user=USER_NAME,
                              password=USER_PASSWORD,
                              host=USER_HOST,
                              database=DB_NAME,
                              auth_plugin=PASSWORD_TYPE)


class Product:
    """Class Product : get products from OFF, send products to database """

    def __init__(self):  # constructor
        self.products_data = []

    def get_products_from_off(self):  # method to get data with requests' module
        global nutriscore
        try:
            for page in range(0, TOTAL_PAGE_NUMBER):
                for key, value in CAT_DICT.items():
                    if key:
                        rpage = requests.get(value + str(page + 1) + '.json')
                        TABLE_JSON_PAGE = rpage.json()
                        products_by_page = TABLE_JSON_PAGE[u'products']

                        for products in products_by_page:  # Fill the list of products

                            id_product = key
                            sub = 0

                            try:
                                name = products['product_name']
                            except KeyError:
                                name = '/'

                            try:
                                brand = products['brands']
                            except KeyError:
                                brand = '/'

                            try:
                                shop = products['stores']
                            except KeyError:
                                shop = '/'

                            try:
                                nutri_origin = products['nutrition_grades_tags'][0]
                                for key_nutri, value_nutri in NUTRI_DICT.items():
                                    if nutri_origin == value_nutri:
                                        nutriscore = key_nutri
                            except KeyError:
                                nutriscore = '/'

                            try:
                                url = products['url']
                            except KeyError:
                                url = '/'

                            self.products_data.append([id_product,
                                                       sub, name,
                                                       brand, shop,
                                                       nutriscore, url])
        except:
            print(PROBLEM_INSERTION)

    def send_products_to_db(self):  # method to send products to database
        try:
            data = self.products_data[:]  # all data got from OFF
            CURSOR = CNX.cursor()
            CURSOR.execute("INSERT INTO Category (id, Produit) "
                           "VALUES (NULL, 'Jus d''orange'), "
                           "(NULL, 'Pâte à tartiner au chocolat'),"
                           "(NULL, 'Biscottes')")
            CURSOR.executemany("INSERT INTO Product(id, produit_id, sub, nom, marque, shop, nutriscore, url) "
                               "VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)", data)
            CNX.commit()
        except:
            print(PROBLEM_INSERTION)