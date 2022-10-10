import mysql.connector
  
# connecting to the database 
dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "mp2",
                     passwd = "eecs116",
                     database = "blurts" ) 

cursorObject1 = dataBase.cursor() 
cursorObject1.execute('''SELECT id , description AS d, COUNT(id)
                     FROM topic,  blurt_analysis 
                     WHERE id = topicid  GROUP BY id , d
                    ORDER BY id''')

myresult1 = cursorObject1.fetchall()
print("Question 1: ")
for x in myresult1:
  print(x)
print()

cursorObject2 = dataBase.cursor() 
cursorObject2.execute('''SELECT DISTINCT(u.name) name, COUNT(follower) followers 
FROM celebrity c, follow, user u
WHERE c.email = followee AND followee = u.email GROUP BY name''')

myresult2 = cursorObject2.fetchall()
print("Question 2: ")
for x in myresult2:
  print(x)
print()

cursorObject3 = dataBase.cursor() 
cursorObject3.execute('''SELECT u.name name, COUNT(text) blurts
FROM celebrity c, blurt b, user u 
WHERE c.email = b.email AND b.email = u.email GROUP BY  name
ORDER BY blurts DESC''')

myresult3 = cursorObject3.fetchall()
print("Question 3: ")
for x in myresult3:
  print(x)
print()

dataBase.close()


#SELECT id , description AS d, COUNT(id) FROM topic,  blurt_analysis WHERE id = topicid  GROUP BY id ORDER BY id;