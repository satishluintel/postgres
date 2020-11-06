## Installing postgres

```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### Switch to postgres account

```
sudo -i -u postgres
```

to access the prompt, simply type

```
psql
```

### If you want to directly log in to postgres

```
sudo -u postgres psql
```

to login into a database without needing a password,

```
sudo -u user_name psql db_name
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

to delete the column,

```
ALTER TABLE test DROP some_date;
```

to update data in the table,

```
UPDATE test SET id = 12341 WHERE name='Satish Luintel';
```

### To export your database 

```
sudo pg_dump -d your_database -h 127.0.0.1 -p 5432 -U postgres > target_db_name.sql
```

### Just in case you needed to purge the postgres servers and user accounts , follow these

https://stackoverflow.com/questions/2748607/how-to-thoroughly-purge-and-reinstall-postgresql-on-ubuntu#2748644

https://linoxide.com/linux-command/how-delete-remove-user-ubuntu/



