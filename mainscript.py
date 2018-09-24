#!/usr/bin/env python
# -*- coding: utf-8 -*-



import create_db
import sql

from feed_in import *
from queries import *
from const_msg import *

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
            if cat_id == '1' or '2' or '3':  # Show the chosen category among cat id
                show_category(cat_id)

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
