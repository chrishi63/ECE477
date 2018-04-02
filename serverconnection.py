import mysql.connector

cnx = mysql.connector.connect(user='ece477', password='SET56?ra', \
                              host='mysql.stackcp.com',\
                              database='cl57-users-xyq', port='50728')
if cnx.is_connected():
    print('Connected to MySQL database')
cur = cnx.cursor()

query = ("SELECT * FROM users;")

cur.execute(query)

for (num, name, email, password, dummy, client, server) in cur:
  print("{}, {}, {}, {}, {}, {}".format(num, name, email, password, client, server))

#insertquery = ("INSERT INTO users "
#               "(email, password, nameTag, client, server)"
#"VALUES ('abc@purdue.edu', 'abcdef234','abc2491','test16','test29');")

newquery = ("SELECT CURDATE();")
#cur.execute(insertquery)
cur.execute(newquery)
for value in cur:
    print(value[0])

#cnx.commit()
cur.close()
cnx.close()
