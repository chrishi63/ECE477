
# http://web.ics.purdue.edu/software/phpMyAdmin/

import mysql.connector
import pymysql
#
# cnx = mysql.connector.connect(user='ece477', password='SET56?ra', \
#                               host='mysql.stackcp.com',\
#                               database='cl57-users-xyq', port=50728)
cnx = pymysql.connect(user='senior477', password='SET56?ra', host=\
                 'mysql.stackcp.com',database='senior-33352e44', port = 50857)

#cnx = mysql.connector.connect(user='senior477', password='SET56?ra', host=\
#                 'mysql.stackcp.com',database='senior-33352e44', port = 50857)
#cnx = mysql.connector.connect(user = 'achhetri',password='aka619ASH',\
#                              host='mydb.ics.purdue.edu',\
#                              database='achhetri')
#if cnx.is_connected():
#   print('Connected to MySQL database ...')
cur = cnx.cursor()

query = ("SELECT CONCAT(first_name, ' ', last_name) AS 'Patient Name', "
   "CASE "
       "WHEN user_name='chrishi63' THEN 'ccoluson989' "
       "ELSE '' "
   "END AS user_name, "
   "heart AS 'Heart Rate', "
   "temp AS 'Body Temperature', "
   "sweat AS 'Sweat Response' "
   "FROM users "
   "INNER JOIN datasets ON users.user_id = datasets.user_id "
   "WHERE user_name = 'ccoluson99' AND password = '123456';")

cur.execute(query)

for (full_name, user_name, heart, temp, sweat) in cur:
 print("{}, {}, {}, {}, {}".format(full_name, user_name, heart, temp, sweat))

#insertquery = ("INSERT INTO users "
#               "(email, password, nameTag, client, server)"
#"VALUES ('abc@purdue.edu', 'abcdef234','abc2491','test16','test29');")

newquery = ("SELECT DATE_SUB(NOW(), INTERVAL 5 HOUR);")
#newquery = ("SELECT CURDATE();")
#cur.execute(insertquery)
cur.execute(newquery)
for value in cur:
   print(str(value[0]).split()[0])

#cnx.commit()
cur.close()
cnx.close()


