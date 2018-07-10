# PUR BEURRE

The projet "Pur Beurre" is a software built in order to help french people who are looking for heathier products to use in their everyday life. 

# How does it work ?
This project is based on OPENFOODFACT's API and a MySQL database.

The random user just needs to open the terminal app on his computer and runs the software.
From this point, the software will return to him two options :
      # 1 - Which product do you want to replace ?
      # 2 - Find my substitutes
      
# Installation

1 - Install MySQL
https://dev.mysql.com/downloads/windows/installer/8.0.html
Select the right file to download and make sure you saved your root user password ! 

2 - Open the command line

3 - Please read requirements.txt to get right versions of plugins and install a virtual environnement
The project is built in Python 3.4 and require Requests, Logging, mysql.connector, json, and MySQL

4 - Open cnx_db.py / create_db.py / feed_in.py / queries.py
Change de password XXXXXX to your own (you should get access now)

5 - Run your virtual env

6 - Run mainscript.py ( python3 mainscript.py )

7 - Enjoy !

# Details
The software is built for french people.
The language is french.
