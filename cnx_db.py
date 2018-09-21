""" script to connect to db ocpizza"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from user_param import *

CNX = mysql.connector.connect(user=USER_NAME,
                              password=USER_PASSWORD,
                              host=USER_HOST,
                              database=DB_NAME,
                              auth_plugin=PASSWORD_TYPE)
