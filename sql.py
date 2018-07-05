#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from create_db import *
from cnx_db import *

try:
	cursor = cnx.cursor()
	create_table = "CREATE TABLE `Category` ("\
					"`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					" `Produit` varchar(40) NOT NULL,"\
					" PRIMARY KEY (`id`)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table)
	cnx.commit()

	create_table_1 = "CREATE TABLE `Product` ("\
					" `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					" `produit_id` smallint(5) unsigned NOT NULL,"\
					"`nom` text NOT NULL,"\
					"`marque` text NOT NULL,"\
					"`nutriscore` text NOT NULL,"\
					"`url` text NOT NULL,"\
					 "PRIMARY KEY (`id`),"\
					 "KEY `fk_produit_id` (`produit_id`),"\
					 "CONSTRAINT `fk_produit_id` FOREIGN KEY (`produit_id`) REFERENCES Category(id)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table_1)
	cnx.commit()

	create_table_2 = "CREATE TABLE `Saved` ("\
					 "`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					 "`produit_id` smallint(5) unsigned NOT NULL,"\
					 "`nom` text NOT NULL,"\
					 "`marque` text NOT NULL,"\
					 "`nutriscore` text NOT NULL,"\
					 "`url` text NOT NULL,"\
					 "PRIMARY KEY (`id`)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table_2)
	cnx.commit()

except:
	print("Les tables existent déjà dans la base de données OPENFOODFACTS.")
else:
	print("Bienvenue !")
finally:
	cnx.close()