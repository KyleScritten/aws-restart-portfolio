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

```





















## Conclusion
This lab demonstrated how to use some common database functions with the `SELECT` statement and `WHERE` clause.

After completing this lab, I am now able to:
* Use aggregate functions `SUM()`, `MIN()`, `MAX()`, and `AVG()` to summarize data
* Use the `SUBSTRING_INDEX()` function to split strings
* Use the `LENGTH()` and `TRIM()` functions to determine the length of a string
* Use the `DISTINCT()` function to filter duplicate records
* Use functions in the `SELECT` statement and `WHERE` clause
