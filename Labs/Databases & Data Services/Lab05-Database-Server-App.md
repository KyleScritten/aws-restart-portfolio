# Build Your DB Server and Interact With Your DB Using an App

## Overview

This lab is designed to reinforce the concept of leveraging an AWS-managed database instance for solving relational database needs.

***Amazon Relational Database Service (Amazon RDS)*** makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, which allows me to focus on my applications and business. Amazon RDS provides six familiar database engines to choose from: Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL, and MariaDB.

<p align="center">
  <img src="images/db-server-app-architecture.png" alt="DB Server App Architecture” width="1000">
</p>

## Task 1: Create a Security Group for the RDS DB Instance

In this task, I create a security group to allow my web server to access my RDS DB instance. This security group will be used when I launch the database instance.

1. In the AWS Management Console, in the search bar, I type `VPC` and select **VPC**.
2. In the left navigation pane, I click **Security groups**.
3. I click **Create security group** and configure:
   * **Security group name:** `DB Security Group`
   * **Description:** `Permit access from Web Security Group`
   * **VPC:** Select **Lab VPC** from the dropdown
4. Since the security group currently has no rules, I add a rule to permit inbound database requests from the Web Security Group. In the **Inbound rules** section, I click **Add rule** and configure:
   * **Type:** MySQL/Aurora (3306)
   * **Source type:** Custom
   * **Source:** Type `sg` in the search field and select **Web Security Group**

   This configures the Database security group to permit inbound traffic on port 3306 from any EC2 instance associated with the Web Security Group.
5. I scroll to the bottom of the screen and click **Create security group**.

I will use this security group when launching the Amazon RDS database.

## Task 2: Create a DB Subnet Group

In this task, I create a DB subnet group that is used to tell RDS which subnets can be used for the database. Each DB subnet group requires subnets in at least two Availability Zones.

1. In the AWS Management Console, in the search bar, I type `RDS` and select **Aurora and RDS**.
2. In the left navigation pane, I click **Subnet groups**.
   * Note: If the navigation pane is not visible, I click the menu icon in the top-left corner.
3. I click **Create DB Subnet Group** and configure:
   * **Name:** `DB Subnet Group`
   * **Description:** `DB Subnet Group`
   * **VPC:** Lab VPC
4. In the **Add subnets** section, for **Availability Zones**, I choose the first and second Availability Zones from the dropdown.
5. For **Subnets**, I select the following subnets:
   * 10.0.1.0/24 (Private Subnet 1)
   * 10.0.3.0/24 (Private Subnet 2)
6. I click **Create**.

This adds Private Subnet 1 (10.0.1.0/24) and Private Subnet 2 (10.0.3.0/24). I will use this DB subnet group when creating the database in the next task.











## Conclusion

After completing this lab, I can:

* Launch an Amazon RDS DB instance with high availability.
* Configure the DB instance to permit connections from my web server.
* Open a web application and interact with my database.
