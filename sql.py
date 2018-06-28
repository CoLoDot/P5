#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', 
		                      password='XXXXXX', 
		                      host='localhost', 
		                      database= 'OPENFOODFACTS', 
		                      auth_plugin='mysql_native_password')

cursor = cnx.cursor()

try:
	create_table = "CREATE TABLE `Produit` ("\
					"`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					" `Produit` varchar(40) NOT NULL,"\
					" PRIMARY KEY (`id`)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table)
	cnx.commit()

	create_table_1 = "CREATE TABLE `Mes_produits` ("\
					 "`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					 "`produit_id` smallint(5) unsigned NOT NULL,"\
					 "`nom` text NOT NULL,"\
					 "`marque` text NOT NULL,"\
					 "`nutriscore` text NOT NULL,"\
					 "`url` text NOT NULL,"\
					 "PRIMARY KEY (`id`)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table_1)
	cnx.commit()

	create_table_2 = "CREATE TABLE `Jus_orange` ("\
					" `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					" `produit_id` smallint(5) unsigned NOT NULL,"\
					"`nom` text NOT NULL,"\
					"`marque` text NOT NULL,"\
					"`nutriscore` text NOT NULL,"\
					"`url` text NOT NULL,"\
					 "PRIMARY KEY (`id`),"\
					 "KEY `fk_produit_id` (`produit_id`),"\
					 "CONSTRAINT `fk_produit_id` FOREIGN KEY (`produit_id`) REFERENCES Produit(id)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table_2)
	cnx.commit()

	create_table_3 = "CREATE TABLE `Pate_a_tartiner` ("\
					 "`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					 "`produit_id` smallint(5) unsigned NOT NULL,"\
					 "`nom` text NOT NULL,"\
					 "`marque` text NOT NULL,"\
					 "`nutriscore` text NOT NULL,"\
					 "`url` text NOT NULL,"\
					 "PRIMARY KEY (`id`),"\
					 "KEY `fk_produit_id_2` (`produit_id`),"\
					 "CONSTRAINT `fk_produit_id_2` FOREIGN KEY (`produit_id`) REFERENCES `Produit` (`id`)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table_3)
	cnx.commit()

	create_table_4 = "CREATE TABLE `Biscottes` ("\
					 "`id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,"\
					 "`produit_id` smallint(5) unsigned NOT NULL,"\
					 "`nom` text NOT NULL,"\
					 "`marque` text NOT NULL,"\
					 "`nutriscore` text NOT NULL,"\
					 "`url` text NOT NULL,"\
					 "PRIMARY KEY (`id`),"\
					 "KEY `fk_produit_id_3` (`produit_id`),"\
					 "CONSTRAINT `fk_produit_id_3` FOREIGN KEY (`produit_id`) REFERENCES `Produit` (`id`)"\
					") ENGINE=InnoDB"
	cursor.execute(create_table_4)
	cnx.commit()
	
except:
	print("Les tables existent déjà dans la base de données OPENFOODFACTS.")
else:
	print("Création de base de données...")
finally:
	cnx.close()