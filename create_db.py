#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', 
		                      password='XXXXXXX', 
		                      host='localhost',
		                      auth_plugin='mysql_native_password')

cursor = cnx.cursor()

try:
	create_db = "CREATE DATABASE IF NOT EXISTS `OPENFOODFACTS` CHARACTER SET 'utf8'"
	cursor.execute(create_db)
	
	param_user = "GRANT ALL PRIVILEGES ON OPENFOODFACTS.* TO 'root'@'localhost' "
	cursor.execute(param_user)
	cnx.commit()

except:
	print("Un problème est survenu lors de la création de la base de données.")
else:
	print("La base de données a été crée.")
finally:
	cnx.close()