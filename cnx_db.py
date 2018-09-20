""" script to connect to db ocpizza"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

CNX = mysql.connector.connect(user='root',
							  password='',
							  host='localhost',
							  database='OPENFOODFACTS',
							  auth_plugin='mysql_native_password')
