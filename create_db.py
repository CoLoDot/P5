#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from const_msg import *
from user_param import *

CNX = mysql.connector.connect(user=USER_NAME,
                              password=USER_PASSWORD,
                              host=USER_HOST,
                              auth_plugin=PASSWORD_TYPE)

try:
    CURSOR = CNX.cursor()
    create_db = "CREATE DATABASE IF NOT EXISTS `OPENFOODFACTS` CHARACTER SET 'utf8'"
    CURSOR.execute(create_db)

    param_user = "GRANT ALL PRIVILEGES ON OPENFOODFACTS.* TO '"+USER_NAME+"'@'"+USER_HOST+"' "
    CURSOR.execute(param_user)
    CNX.commit()

except:
    print(PROBLEM_DB)
finally:
    CNX.close()