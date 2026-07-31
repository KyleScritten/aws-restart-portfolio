# Introduction to Amazon Aurora

This lab introduces me to Amazon Aurora and provides a basic understanding of how to use Aurora. I follow the steps to create an Aurora instance and then connect to it.

To successfully complete this lab, I should have some experience using the Linux operating system and have a basic understanding of structured query language (SQL).

## Introducing the technologies

**Amazon Aurora**

Aurora is a fully managed, MySQL-compatible, relational database engine that combines the performance and reliability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. It delivers up to five times the performance of MySQL without requiring changes to most existing applications that use MySQL databases.

**Amazon Elastic Compute Cloud (Amazon EC2)**

Amazon EC2 is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2 reduces the time required to provision new server instances to minutes, giving me the ability to quickly scale capacity, both up and down, as my computing requirements change.

**Amazon Relational Database Service (Amazon RDS)**

Amazon RDS makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, freeing me up to focus on my applications and business. Amazon RDS provides six database engines to choose from, including Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL, and MariaDB.

## Task 1: Create an Aurora instance

In this task, I create an Aurora database (DB) instance.

1. At the top of the AWS Management Console, in the search bar, I search for and choose `RDS`.
2. In the left navigation menu, I choose **Databases**.
3. I choose **Create database** and configure the following options:
   * **Choose a database creation method:** Standard create
   * **Engine type:** Aurora (MySQL Compatible)
   * **Engine version:** the version specified as the default for major version 8.0
   * **Templates:** Dev/Test
4. In the **Settings** section, I configure the following options:
   * **DB cluster identifier:** `aurora`
   * **Master username:** `admin`
   * **Master password:** `admin123`
   * **Confirm password:** `admin123`
5. In the **Instance configuration** section, for **DB instance class**, I choose **Burstable classes (includes t classes)**, and choose **db.t3.medium** from the dropdown list.
6. In the **Availability & durability** section, for **Multi-AZ deployment**, I choose **Don't create an Aurora Replica**.
>[!Note]
> Amazon RDS Multi-AZ deployments provide enhanced availability and durability for DB instances, making them a natural fit for production database workloads. When I provision a Multi-AZ DB instance, Amazon RDS automatically creates a primary DB instance and synchronously replicates the data to a standby instance in a different Availability Zone. Since this is a lab environment, I do not need to perform a multi-AZ deployment.
7. In the **Connectivity** section, I configure the following options and leave any not mentioned at their default value:
   * **Virtual private cloud (VPC):** LabVPC
   * **Subnet group:** dbsubnetgroup
   * **Public access:** No
   * **VPC security group:** Choose existing
   * **Existing VPC security groups:** Remove the **default** security group, then choose **DBSecurityGroup** from the dropdown list.
8. In the **Monitoring** section, I clear the check box for **Enable Enhanced monitoring**.
9. I expand the **Additional configuration** section, and for **Initial database name**, I enter `world`.
10. In the **Encryption** section, I clear the check box for **Enable encryption**.
11. In the **Maintenance** section, I clear the check box for **Enable auto minor version upgrade**.
12. I scroll to the bottom of the screen and choose **Create database**.

<p align="center">
  <img src="images/db-aurora.png" alt="Created an Aurora instance” width="1000">
</p>

I have successfully created an Aurora instance.
















## Conclusion

Through this lab, I have now successfully:

* Created an Aurora instance.
* Connected to a pre-created Amazon EC2 instance.
* Configured the Amazon EC2 instance to connect to Aurora.
* Queried the Aurora instance.
