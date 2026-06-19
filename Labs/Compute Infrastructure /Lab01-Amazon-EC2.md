# Cloud Foundations - Introduction to Amazon Elastic Compute Cloud (EC2)
## Overview
![Amazon EC2 Lab Scenario](images/lab-scenario.jpeg)

In this lab, I explored the fundamentals of Amazon EC2 by learning how to launch, resize, manage, and monitor virtual servers in the AWS Cloud.

Amazon Elastic Compute Cloud (EC2) is a cloud computing service that provides scalable and on-demand compute capacity. It allows developers and organizations to quickly deploy virtual machines without the need to invest in physical hardware.

Through this lab, I gained hands-on experience with the EC2 management process, including instance deployment, configuration, monitoring, and resizing. One of the key advantages of EC2 is its flexibility, enabling resources to be scaled up or down based on changing requirements.

EC2 also follows a pay-as-you-go pricing model, meaning you only pay for the resources you use. This makes it a cost-effective solution for running applications while providing the reliability, performance, and fault-tolerant infrastructure of AWS.

## Lab Objectives

Through this lab I have learnt to:
- Launch a web server with termination protection enabled
- Monitor an EC2 instance
- Modify the security group that a web server is using to allow HTTP access
- Resize an Amazon EC2 instance to scale
- Test termination protection
- Terminate an EC2 instance

## Task 1: Launching an EC2 instance
In this task I launched a new Amazon EC2 instance with termination protection from the AWS Management Console.

### Steps taken to launch instance

1. Opened EC2 Dashboard, selected Launch Instance and named the instance ```Web Server```
2. Kept Amazon Linux 2023 as Amazon Machine Image (AMI) which is selected by default
3. Chose the **t3.micro** instance type
4. In the Key pair (login) pane, select **Proceed without a key pair (Not recommended)**.
5. Configured network settings by selecting the Lab VPC for **VPC - *required***. Created a security group called ```Web Server security group```, with the description ```Security group for my web server```. Removed the inbound security groups SSH rule for better security.
6. In the Configure storage pane, keep the default storage configuration.
7. Expand the **Advanced details** pane and select the dropdown for Termination protection, then choose Enable. I added a script that automatically installs and starts a web server. This script installs Apache HTTP Server, starts the service, and creates a simple web page.
  ```
#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
```
8. Launch the EC2 instance by selecting ```Launch instance```

