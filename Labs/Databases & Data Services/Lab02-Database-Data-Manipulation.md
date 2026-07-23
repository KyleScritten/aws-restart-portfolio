# Insert, Update, and Delete Data in a Database

## Scenario

The database operations team has created a relational database called `world` containing three tables: `city`, `country`, and `countrylanguage`. I have to validate the configuration of the database by running `INSERT`, `UPDATE`, and `DELETE` statements on the `country` table.

At the end, my architecture looks like the following example:
<p align="center">
  <img src="images/db-manipulation-scenario.png" alt="Database Data Manipulation Overview" width="1000">
</p>

## Task 1: Connect to a database

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

```

6. To show the existing databases, I enter the following command in the terminal and make a note of the currently available databases:

```bash

```




























## MySQL command-line client
The MySQL command-line client is an SQL shell that you can use to interact with database engines.

| Switch             | Description                                                     |
|--------------------|-----------------------------------------------------------------|
| -u or --user       | The MySQL user name used to connect to a database instance      |
| -p or --password   | The MySQL password used to connect to a database instance       |

## Conclusion
Through this lab I have now successfully:
* Inserted rows into a table
* Updated rows in a table
* Deleted rows from a table
* Imported rows from a database backup file

## Additional resources
- Country, city, and language data, Statistics Finland: The material was downloaded from Statistics Finland's interface service 
on February 4, 2022, with the [license CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en).
The original data source is available from [Statistics Finland](https://tilastokeskus.fi/tup/kvportaali/index_en.html).

- For more information about database functions and operators, see the following resources:

  - [INSERT statement](https://mariadb.com/kb/en/insert/)
  - [UPDATE statement](https://mariadb.com/kb/en/update/)
  - [DELETE statement](https://mariadb.com/kb/en/delete/)
