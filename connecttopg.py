import psycopg2

conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")

print("Opened database successfully")

# cur = conn.cursor()
# cur.execute('''CREATE TABLE ANIMENAME
#        (GROUPID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        URL            TEXT     NOT NULL);''')
# print("Table created successfully")

# conn.commit()
# conn.close()

# cur = conn.cursor()

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

# conn.commit()
# print("Records created successfully")
# conn.close()