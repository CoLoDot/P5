#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from const_msg import *

cnx = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              auth_plugin='mysql_native_password')

try:
    cursor = cnx.cursor()
    create_db = "CREATE DATABASE IF NOT EXISTS `OPENFOODFACTS` CHARACTER SET 'utf8'"
    cursor.execute(create_db)

    param_user = "GRANT ALL PRIVILEGES ON OPENFOODFACTS.* TO 'root'@'localhost' "
    cursor.execute(param_user)
    cnx.commit()

except:
    print(PROBLEM_DB)
finally:
    cnx.close()
