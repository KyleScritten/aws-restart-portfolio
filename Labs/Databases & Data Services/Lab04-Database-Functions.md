# Working with Functions

## Scenario
The database operations team has created a relational database named `world` containing three tables: `city`, `country`, and `countrylanguage`. Based on specific use cases in the lab exercise, I write a few queries using database functions with the `SELECT` statement and `WHERE` clause.

At the end, my architecture looks like the following example:
<p align="center">
  <img src="images/db-functions-lab.png" alt="Database Functions Lab Outcome Overview" width="1000">
</p>

## Task 1: Connect to the Command Host

In this task, I connect to an instance containing a database client, which is used to connect to a database. This instance is referred to as the Command Host.

1. In the AWS Management Console, I choose the **Services** menu, choose **Compute**, and then choose **EC2**.
2. In the left navigation menu, I choose **Instances**, select the check box next to the instance labelled **Command Host**, and choose **Connect**.
>[!Note]
> If I do not see the Command Host, the lab is probably still being provisioned, or I may be using another Region.
3. For **Connect to instance**, I choose the **Session Manager** tab and choose **Connect** to open a terminal window.
4. To configure the terminal to access all required tools and resources, I run the following commands:
```bash
sudo su
cd /home/ec2-user/
```
5. To connect to the relational database instance, I run the following command in the terminal (a password was configured when the database was installed):
```bash
mysql -u root --password='re:St@rt!9'
```
Output:
```bash
sh-4.2$ sudo su
[root@ip-10-1-11-93 bin]# cd /home/ec2-user/
[root@ip-10-1-11-93 ec2-user]# mysql -u root --password='re:St@rt!9'
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 5
Server version: 10.5.29-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

## Task 2: Query the world database

In this task, I query the `world` database using various `SELECT` statements and database functions. A function is used to process and manipulate data in a query, and while there are a wide range of SQL functions, this lab reviews a subset of commonly used ones.

1. To show the existing databases, I enter the following command in the terminal and verify that a database named `world` is available:
```bash
MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| world              |
+--------------------+
4 rows in set (0.001 sec)
```
2. To review the table schema, data, and number of rows in the `country` table, I run the following query:
```bash
MariaDB [(none)]> SELECT * FROM world.country;
```
3. I then run the following query to demonstrate how to use aggregate functions `SUM()`, `MIN()`, `MAX()`, and `AVG()` to summarize data. Because the query does not include a `WHERE` condition, the functions aggregate data from all records in the `country` table:
```bash
MariaDB [(none)]> SELECT sum(Population), avg(Population), max(Population), min(Population), count(Population) FROM world.country;
+-----------------+-----------------+-----------------+-----------------+-------------------+
| sum(Population) | avg(Population) | max(Population) | min(Population) | count(Population) |
+-----------------+-----------------+-----------------+-----------------+-------------------+
|      6078749450 |   25434098.1172 |      1277558000 |               0 |          239 |
+-----------------+-----------------+-----------------+-----------------+-------------------+
1 row in set (0.002 sec)
```
>[!Note]
>  * `SUM()` adds all the population values together.
>  * `AVG()` generates an average across all the population values.
>  * `MAX()` finds the row with the highest population value.
>  * `MIN()` finds the row with the lowest population value.
>  * `COUNT()` finds the number of rows with a population value.

4. In some cases, I might need to split a string. The following query uses `SUBSTRING_INDEX()` to split a string where a space occurs, and I notice that the second column includes the beginning of each region name:
```bash
MariaDB [(none)]> SELECT Region, substring_index(Region, " ", 1) FROM world.country;
+---------------------------+---------------------------------+
| Region                    | substring_index(Region, " ", 1) |
+---------------------------+---------------------------------+
| Caribbean                 | Caribbean                       |
| Southern and Central Asia | Southern                        |
| Central Africa            | Central                         |
...
239 rows in set (0.001 sec)
```
5. Sometimes I may need to search rows using a string fragment. The following query includes `SUBSTRING_INDEX()` as part of a condition in the `WHERE` clause to filter records that include "Southern" in the first part of the region name:
```bash
MariaDB [(none)]> SELECT Name, Region from world.country WHERE substring_index(Region, " ", 1) = "Southern";
+-------------------------------+---------------------------+
| Name                          | Region                    |
+-------------------------------+---------------------------+
| Afghanistan                   | Southern and Central Asia |
| Albania                       | Southern Europe           |
| Andorra                       | Southern Europe           |
| Bangladesh                    | Southern and Central Asia |
| Bosnia and Herzegovina        | Southern Europe           |
| Bhutan                        | Southern and Central Asia |
| Botswana                      | Southern Africa           |
| Spain                         | Southern Europe           |
| Gibraltar                     | Southern Europe           |
| Greece                        | Southern Europe           |
| Croatia                       | Southern Europe           |
| India                         | Southern and Central Asia |
| Iran                          | Southern and Central Asia |
| Italy                         | Southern Europe           |
| Kazakstan                     | Southern and Central Asia |
| Kyrgyzstan                    | Southern and Central Asia |
| Sri Lanka                     | Southern and Central Asia |
| Lesotho                       | Southern Africa           |
| Maldives                      | Southern and Central Asia |
| Macedonia                     | Southern Europe           |
| Malta                         | Southern Europe           |
| Namibia                       | Southern Africa           |
| Nepal                         | Southern and Central Asia |
| Pakistan                      | Southern and Central Asia |
| Portugal                      | Southern Europe           |
| San Marino                    | Southern Europe           |
| Slovenia                      | Southern Europe           |
| Swaziland                     | Southern Africa           |
| Tajikistan                    | Southern and Central Asia |
| Turkmenistan                  | Southern and Central Asia |
| Uzbekistan                    | Southern and Central Asia |
| Holy See (Vatican City State) | Southern Europe           |
| Yugoslavia                    | Southern Europe           |
| South Africa                  | Southern Africa           |
+-------------------------------+---------------------------+
34 rows in set (0.000 sec)
```
6. I can use the `LENGTH()` and `TRIM()` functions to determine how many characters are in a string — `TRIM()` clears leading and trailing blank spaces, and `LENGTH()` returns a count of the remaining characters. The next example returns only regions that have fewer than 10 characters in their names:
```bash
MariaDB [(none)]> SELECT Region FROM world.country WHERE LENGTH(TRIM(Region))< 10;
+-----------+
| Region    |
+-----------+
| Caribbean |
| Caribbean |
| Caribbean |
| Polynesia |
| Caribbean |
| Caribbean |
| Caribbean |
| Polynesia |
| Caribbean |
| Caribbean |
| Caribbean |
| Caribbean |
| Melanesia |
...
39 rows in set (0.001 sec)
```
7. Having noticed duplicate records in the previous example, I use the `DISTINCT()` function to filter the duplicates:
```bash
MariaDB [(none)]> SELECT DISTINCT(Region) FROM world.country WHERE LENGTH(TRIM(Region)) < 10;
+-----------+
| Region    |
+-----------+
| Caribbean |
| Polynesia |
| Melanesia |
+-----------+
3 rows in set (0.001 sec)
```

### Challenge
I write a query to return rows that have "Micronesian/Caribbean" as the name in the region column. The output splits the region into two separate columns: one named `Region Name 1` and one named `Region Name 2`.
```bash
MariaDB [(none)]> SELECT Name, substring_index(Region, "/", 1) as "Region Name 1",substring_index(region, "/", -1) as "Region Name 2" FROM world.country WHERE Region = "Micronesia/Caribbean";
+--------------------------------------+---------------+---------------+
| Name                                 | Region Name 1 | Region Name 2 |
+--------------------------------------+---------------+---------------+
| United States Minor Outlying Islands | Micronesia    | Caribbean     |
+--------------------------------------+---------------+---------------+
1 row in set (0.000 sec)
```

## Conclusion
This lab demonstrated how to use some common database functions with the `SELECT` statement and `WHERE` clause.

After completing this lab, I am now able to:
* Use aggregate functions `SUM()`, `MIN()`, `MAX()`, and `AVG()` to summarize data
* Use the `SUBSTRING_INDEX()` function to split strings
* Use the `LENGTH()` and `TRIM()` functions to determine the length of a string
* Use the `DISTINCT()` function to filter duplicate records
* Use functions in the `SELECT` statement and `WHERE` clause

## Additional resources
- Country, city, and language data, Statistics Finland: The material was downloaded from Statistics Finland's interface 
service on February 4, 2022, with the [license CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en). 
The original data source is available from [Statistics Finland](https://tilastokeskus.fi/tup/kvportaali/index_en.html).

- For more information about database functions and operators, see the following resources:
  - [SELECT statements](https://mariadb.com/kb/en/select/)
  - [Count function](https://mariadb.com/kb/en/count/)
  - [SUM function](https://mariadb.com/kb/en/sum/)
  - [AVG function](https://mariadb.com/kb/en/avg/)
  - [MIN function](https://mariadb.com/kb/en/min/)
  - [MAX function](https://mariadb.com/kb/en/max/)
  - [SUBSTRING_INDEX function](https://mariadb.com/kb/en/substring_index/)
  - [LENGTH function](https://mariadb.com/kb/en/length/)
  - [TRIM function](https://mariadb.com/kb/en/trim/)
