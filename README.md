# PUR BEURRE

The projet "Pur Beurre" is a software built in order to help french people who are looking for heathier products to use in their everyday life. 

# How does it work ?
This project is based on OPENFOODFACT's API and a MySQL database.

The random user just needs to open the terminal app on his computer and runs the software.
From this point, the software will return to him two options :
      # 1 - Which product do you want to replace ?
      # 2 - Find my substitutes
      
# Installation

-> Download the project (zip format) or use git clone if you are already frendly with the command line.

1 - Install MySQL
https://dev.mysql.com/downloads/windows/installer/8.0.html
Select the right file to download and make sure you saved your root user password ! 

2 - In your favorite code editor, open the file user_param.py and fill the blanks with your personal informations for MySQL (username, password, host, etc.)

3 - Open the command line and go to the directory containing the software's scripts

4 - Run requirements.txt to install dependencies : "pip install -r files/requirements.txt"

5 - Run your virtual env : "virtualenv -p python3 env" and "source env/bin/activate"

6 - Run mainscript.py : "python3 mainscript.py"

7 - Enjoy !

# Details
The software is built for french people.
The language is french.
