#!/usr/bin/env python
# -*- coding: utf-8 -*-

import colorama
from colorama import Fore, Back, Style

colorama.init()

# loading message
LOADING_MSG = Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nChargement en cours..."

# main loop messages
THE_MAIN_MENU = Fore.WHITE + Back.BLACK + Style.BRIGHT + "\n- Menu - " \
                                                         "\n1 - Quel aliment souhaitez-vous remplacer ? " \
                                                         "\n2 - Retrouver mes aliments substitués " \
                                                         "\n3 - Quitter le programme "

ENTER_NUMBER = Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nEntrez le chiffre correspondant à votre souhait : "
ENTER_CAT_NUMBER = Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nEntrez le chiffre correspondant à la " \
                                                           "catégorie que vous désirez afficher : "

ENTER_IDSUB_NUMBER = Fore.WHITE + Back.BLACK + Style.BRIGHT + "\nTapez l\'ID attribué au " \
                                                              "produit pour afficher une proposition" \
                                                              " de substitut \nou appuyez sur entrer " \
                                                              "pour quitter : "
SHOW_MORE_SUB = "\nVoulez-vous afficher d'autres substituts ? (tapez 'entrer' sinon tapez 1) : "

# messages for queries.py
SELECT_CAT = Fore.BLACK + Back.WHITE + Style.BRIGHT + '\n- Sélectionnez la catégorie -'
SUB_RESULT = Fore.BLACK + Back.CYAN + Style.BRIGHT + "\nNous vous proposons le substitut suivant:"
SAVE_SUB = Fore.BLACK + Back.CYAN + Style.BRIGHT +'\nVoulez-vous sauvegarder ce substitut ? ' \
                                                  '(tapez 1, sinon tapez "entrer") : '
SUB_SAVED_CONFIRMATION = Fore.BLACK + Back.CYAN + Style.BRIGHT + "Produit sauvegardé !"

SUB_SAVED_MENU = Fore.BLACK + Back.WHITE + Style.BRIGHT + '\n- Mes produits sauvegardés -'

ENTER_IDSUB_NUMBER_WANTED = "\nTapez le numéro du SUBSTITUT que vous désirez " \
                            "afficher ou tapez 'entrer' pour quitter : "

# goodbye message
GOODBYE_MSG = Fore.BLACK + Back.WHITE + Style.BRIGHT + "\nMerci d'avoir utilisé notre programme. À bientôt."

# messages in case of trouble
PROBLEM_DB = "Un problème est survenu lors de la création de la base de données."
PROBLEM_DB_TABLES = Fore.RED + Back.WHITE + Style.BRIGHT + "Les tables existent déjà dans " \
                                                           "la base de données OPENFOODFACTS."
PROBLEM_INSERTION = Fore.RED + Back.WHITE + Style.BRIGHT + "Un problème est survenu lors de la " \
                                                           "récupération/insertion des produits."
PROBLEM_CAT_MENU = Fore.RED + Back.WHITE + Style.BRIGHT + "Impossible d'afficher le menu."
PROBLEM_SUB_MENU = "Impossible d'afficher les produits sauvegardés."
PROBLEM_DB_SUPPR = "Un problème est survenu lors de la suppression des données."