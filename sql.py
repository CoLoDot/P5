"""script of sql queries"""
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

try:
    CURSOR = CNX.cursor()
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS Category (" \
                   "id SMALLINT unsigned NOT NULL AUTO_INCREMENT," \
                   "Produit VARCHAR(40) NOT NULL," \
                   " PRIMARY KEY (id)" \
                   ") ENGINE=InnoDB"
    CURSOR.execute(CREATE_TABLE)
    CNX.commit()

    CREATE_TABLE_1 = "CREATE TABLE IF NOT EXISTS `Product` (" \
                     "id SMALLINT unsigned NOT NULL AUTO_INCREMENT," \
                     "produit_id SMALLINT unsigned NOT NULL," \
                     "sub TEXT NOT NULL," \
                     "nom TEXT NOT NULL," \
                     "marque TEXT NOT NULL," \
                     "shop TEXT NOT NULL," \
                     "nutriscore TEXT  NOT NULL," \
                     "url TEXT NOT NULL," \
                     "PRIMARY KEY (id)," \
                     "KEY fk_produit_id (produit_id)," \
                     "CONSTRAINT fk_produit_id FOREIGN KEY (produit_id) REFERENCES Category(id)" \
                     ") ENGINE=InnoDB"
    CURSOR.execute(CREATE_TABLE_1)
    CNX.commit()


except:
    print(PROBLEM_DB_TABLES)
finally:
    CNX.close()
