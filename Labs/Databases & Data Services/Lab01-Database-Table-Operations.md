# Database Table Operations
In this lab I will practice creating and dropping (deleting) databases and tables previopusly configured by a database operations team.

<p align="center">
  <img src="images/db-table-ops-scenario.png" alt="Database Table Operations Lab Scenario" width="1000">
</p>

## Task 1: Connect to the Command Host

In this task, I connect to an EC2 instance configured with a database client. The client is used to run structured query language (SQL) queries against a relational database. This instance is referred to as the Command Host.

1. In the AWS Management Console, I choose the **Services** menu, choose **Compute**, and then choose **EC2**.
2. In the left navigation menu, I choose **Instances**, select the check box next to the instance labelled **Command Host**, and choose **Connect**.
   * Note: If I do not see the Command Host, the lab is probably still being provisioned, or I may be using another Region.
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
[root@ip-10-1-11-100 bin]# cd /home/ec2-user/
[root@ip-10-1-11-100 ec2-user]# mysql -u root --password='re:St@rt!9'
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 10.5.29-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

## Task 2: Create a database and a table
In this task, I create a database named `world` and a table named `country`. I then alter the `country` table.
```bash
```


## Conclusion
- Used the **CREATE** statement to create databases and tables
- Used the **SHOW** statement to view available databases and tables
- Used the **ALTER** statement to alter the structure of a table
- Used the **DROP** statement to delete databases and tables

## MySQL command-line client
1. The MySQL command-line client is an SQL shell that you can use to interact with database engines.

| Switch             | Description                                                     |
|--------------------|-----------------------------------------------------------------|
| -u or --user       | The MySQL user name used to connect to a database instance      |
| -p or --password   | The MySQL password used to connect to a database instance       |

Example: Run `mysql -u root --password='<psswd>` to connect to the relational database instance. A password was configured when the database was installed.

## Additional resources
- Country, city, and language data, Statistics Finland: The material was downloaded from Statistics Finland's interface 
service on February 4, 2022, with the [license CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en). 
The original data source is available from [Statistics Finland](https://stat.fi/tup/kvportaali/index_en.html).

- For more information about SQL table operation commands, see the following resources:

  - [CREATE database](https://mariadb.com/kb/en/create-database/)
  - [CREATE table](https://mariadb.com/kb/en/create-table/)
  - [SHOW commands](https://mariadb.com/kb/en/show/)
  - [ALTER table](https://mariadb.com/kb/en/alter-table/)
  - [DROP database](https://mariadb.com/kb/en/drop-database/)
  - [DROP table](https://mariadb.com/kb/en/drop-table/)
