# Troubleshooting the Creation of an EC2 Instance

## Activity overview

In this activity, I use the AWS Command Line Interface (AWS CLI) to launch Amazon Elastic Compute Cloud (Amazon EC2) instances.

When creating the instance, I reference a user data script to configure it with an Apache web server, a MariaDB relational database (a fork of the MySQL relational database), and PHP. Together, these software packages installed on a single machine are often referred to as a LAMP stack (**L**inux, **A**pache web server, **M**ySQL, and **P**HP) — a common way to create a website with a database backend on a single machine.

The same user data file deploys website files and runs database configuration scripts on the instance, resulting in an instance that hosts the Café Web Application.

<p align="center">
  <img src="images/troubleshoot-create-ec2.png" alt="Troubleshooting the Creation of an EC2 Instance Architecture" width="900">
</p>

*The following diagram shows the architecture I create in this activity.*

