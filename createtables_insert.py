#!/usr/bin/python
# VERSION 3.6.9 
# before running this run the code on your shell -> pip3 install psycopg2
# psycopg2-2.8.6

import psycopg2

#establish a database connection to postgres
conn = psycopg2.connect(database="satishluintel", user = "postgres", password = "your_password", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
cur.execute('CREATE TABLE testdb (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PHONE TEXT NOT NULL, ADDRESS TEXT NOT NULL, SALARY real NOT NULL)')
cur.execute("INSERT INTO testdb (ID,NAME,PHONE,ADDRESS,SALARY) VALUES (1, 'Satish Luintel', '+9771000000', 'Kathmandu', 100000.00 )")
conn.commit()
print("Records created successfully")
conn.close()
