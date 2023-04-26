# Install MySQL on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

# MySQL root variables
# Do not touch them
my_host = 'localhost'
root_user = 'root'
root_password = 'mX74Jy6q2P!_eAtY'

# new db and ne user variables
database_name = 'elderco'
user_name = 'u_elderco'
user_password = 'Prur_preBH.U13_d69'

from mysql import connector
dataBase = connector.connect(
    host = my_host,
    user = root_user,
    passwd = root_password,
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS " + database_name)

# create an user
cursorObject.execute("CREATE USER IF NOT EXISTS " + user_name +"@" + my_host + " IDENTIFIED BY '" + user_password +"'")
cursorObject.execute("GRANT ALL PRIVILEGES ON " + database_name + ".* TO " + user_name + "@" + my_host)

print("All Done!")
