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
from const_msg import *

# lg.basicConfig(level=lg.DEBUG)
colorama.init()


def main():  # Main function

    print(LOADING_MSG)

    program = True
    new_product = Product()
    new_product.get_products_from_off()
    new_product.send_products_to_db()

    while program:  # Main loop
        print(THE_MAIN_MENU)
        menu_input = input(ENTER_NUMBER)

        if menu_input == '1':  # Show main menu
            menu()

            cat_id = input(ENTER_CAT_NUMBER)
            if cat_id <= '3':  # Show the chosen category among cat id
                show_category(cat_id)
                user_idproduct_choosen = input(ENTER_IDSUB_NUMBER)
                if user_idproduct_choosen:  # Save a substitute
                    substitutes(cat_id, user_idproduct_choosen)

        if menu_input == '2':  # Show saved products
            saving_products = True
            while saving_products:
                show_saved_products()
                saved_menu = input(SHOW_MORE_SUB)
                if saved_menu == '1':
                    saving_products = False

        if menu_input == '3':  # Quit program and delete all data
            stop_program()
            program = False


if __name__ == '__main__':  # Encapsulation of main function
    main()
