## Installing postgres

```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### Switch to postgres account

```
sudo -i -u postgres
```

The console will appear like

```
postgres@linux_username:~$
```

to access the Postgres prompt then , simply type

```
psql
```

and you will see

```
postgres#
```

### If you want to directly log in to postgres

```
sudo -u postgres psql
```

to login into a database without needing a password,

```
sudo -u user_name psql db_name
```


### To expose your Postgres Server Port for Remote Login

First check by telnet if you succeed, 

```
telnet your_server_IP 5432
```

The error should be 'Connection Refused' , if postgres is not configured for a remote login.

Now, to fix this, find the Postgres configuration file,

```
find / -name "postgresql.conf"
```

Sample output:
/usr/lib/tmpfiles.d/postgresql.conf
/etc/postgresql/10/main/postgresql.conf

Open the /etc/... file and replace the line 

```
listen_addresses = 'localhost'
```

with 

```
listen_addresses = '*'
```

i.e your server will now listen connections from all IP Addresses

After this restart the server,

```
sudo systemctl restart postgresql.service

```

If you check now with nmap or any other port scanning tool, you should find your 5432 port open.
However, to connect to this server using psql, configure pg_hba.conf file in the same directory as the conf file above,
add the following entries to the end of the file.

```
host    all             all              0.0.0.0/0                       md5
host    all             all              ::/0                            md5
```

Finally, restart the server,

```
sudo systemctl restart postgresql.service

```

and connect to the server as,

```
$ psql -h your_server_IP_ADDRESS -U postgres
```


### To create a user from shell directly,

```
sudo -u postgres createuser --interactive
```

### To reset the password if you have forgotten:

```
ALTER USER user_name WITH PASSWORD 'new_password';
```

### To log in with ident based authentication, a Linux user with the same name as the Postgres role and database is required.

```
sudo adduser satishluintel
```

to switch over psql with this account,

```
sudo -i -u satishluintel
psql
```
or directly inline 
```
sudo -u satishluintel psql
```

### To create a new database,

```
create database satishluintel
```
Note that from bash you can create a db as createdb database_name

### To rename a database,

```
alter database "old_db" rename to "new_db"
``` 

### To list all the databases,

```
\list 
```
or 
```
\l
```
### To connect to a database

```
psql -d satishluintel
```

### To see the tables, if any

```
\dt
```

### To create a table

Creating Table in postgres 
```
CREATE TABLE table_name (
    column_name1 col_type (field_length) column_constraints,
    column_name2 col_type (field_length),
    column_name3 col_type (field_length)
);
```
so, as an example,

```
 CREATE TABLE TEST( ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);
```

to display the table,
```
\d test
```

to insert data into the table,

```
INSERT INTO test (id, name) VALUES (1, 'Satish Luintel');

```

to retrieve data from the table,

```
select * from test;
```

to delete a row from the table,

```
delete from test where id=1;
```

to add some column in the table,

```
ALTER TABLE test  ADD some_date date;
```

remember that some_date is the name of the column to add to the table, and date is the data type. Data types can be int, text, date etc. 

to delete the column,

```
ALTER TABLE test DROP some_date;
```

to update data in the table,

```
UPDATE test SET id = 12341 WHERE name='Satish Luintel';
```

### To check your database size

```
SELECT pg_size_pretty (pg_database_size ('your_database_name'));
```

### To check SIZE of all databases
```
SELECT pg_database.datname as "database_name", pg_database_size(pg_database.datname)/1024/1024 AS size_in_mb FROM pg_database ORDER by size_in_mb DESC;
```

### To export your database 

```
sudo pg_dump -d your_database -h 127.0.0.1 -p 5432 -U postgres > target_db_name.sql
```

### Just in case you needed to purge the postgres servers and user accounts , follow these

```
sudo apt-get --purge remove postgresql postgresql-doc postgresql-common
``` 

https://stackoverflow.com/questions/2748607/how-to-thoroughly-purge-and-reinstall-postgresql-on-ubuntu#2748644

https://linoxide.com/linux-command/how-delete-remove-user-ubuntu/



