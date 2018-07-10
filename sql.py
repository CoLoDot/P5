#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from create_db import *
from cnx_db import *

try:
	cursor = cnx.cursor()
	create_table = "CREATE TABLE IF NOT EXISTS `Category` ("\
					"`id` SMALLINT unsigned NOT NULL AUTO_INCREMENT,"\
					" `Produit` VARCHAR(40) NOT NULL,"\
					" PRIMARY KEY (`id`)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table)
	cnx.commit()

	create_table_1 = "CREATE TABLE IF NOT EXISTS `Product` ("\
					" `id` SMALLINT unsigned NOT NULL AUTO_INCREMENT,"\
					" `produit_id` SMALLINT unsigned NOT NULL,"\
					"`nom` TEXT NOT NULL,"\
					"`marque` TEXT NOT NULL,"\
					"`nutriscore` TINYTEXT  NOT NULL,"\
					"`url` TEXT NOT NULL,"\
					 "PRIMARY KEY (`id`),"\
					 "KEY `fk_produit_id` (`produit_id`),"\
					 "CONSTRAINT `fk_produit_id` FOREIGN KEY (`produit_id`) REFERENCES Category(id)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table_1)
	cnx.commit()

	create_table_2 = "CREATE TABLE IF NOT EXISTS `Saved` ("\
					 "`id` SMALLINT unsigned NOT NULL AUTO_INCREMENT,"\
					 "`produit_id` SMALLINT unsigned NOT NULL,"\
					 "`nom` TEXT NOT NULL,"\
					 "`marque` TEXT NOT NULL,"\
					 "`nutriscore` TINYTEXT NOT NULL,"\
					 "`url` TEXT NOT NULL,"\
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