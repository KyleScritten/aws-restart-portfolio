# Using AWS Systems Manager

## Lab overview

AWS Systems Manager is a collection of capabilities I can use to centralize operational data and automate tasks across my Amazon Web Services (AWS) resources. Systems Manager can configure and manage Amazon Elastic Compute Cloud (Amazon EC2) instances, on-premises servers, virtual machines, and other AWS resources at scale.

## Task 1: Generate inventory lists for managed instances

> [!NOTE]
> I can use Fleet Manager, a capability of Systems Manager, to collect operating system information, application information, and metadata from EC2 instances, on-premises servers, or virtual machines in a hybrid environment. I can also use Fleet Manager to query metadata to quickly understand which instances are running the software and configurations my software policy requires, and which instances need updating.

In this task, I use Fleet Manager to gather inventory from an EC2 instance.

## Task 2: Install a Custom Application using Run Command

In this task, I install a custom web application (Widget Manufacturing Dashboard) using Run Command, a capability of Systems Manager.

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION" width="900">
</p>

In the preceding diagram, Systems Manager installs an application on an EC2 instance within a virtual private cloud (VPC) using Run Command. Run Command runs the "install script" and installs the following: Apache web server, PHP, AWS SDK, and the web application. Once everything is installed, it also starts the web server.

## Task 3: Use Parameter Store to manage application settings

> [!NOTE]
> Parameter Store, a capability of Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. I can store data such as passwords, database strings, and license codes as parameter values, either as plain text or encrypted data, and can then reference values using the unique name I specified when creating the parameter.

In this task, I use Parameter Store to store a parameter that I use to activate a feature in an application.

## Task 4: Use Session Manager to access instances

> [!NOTE]
> With Session Manager, a capability of Systems Manager, I can manage my EC2 instances through an interactive one-step browser-based shell or through the AWS Command Line Interface (AWS CLI). Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys. I can also use Session Manager to help comply with corporate policies that require controlled access to instances, strict security practices, and fully auditable logs with instance access details, while still providing end users with one-step cross-platform access to EC2 instances. When using Session Manager with Microsoft Windows, Session Manager provides access to a PowerShell console on the instance.

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION" width="900">
</p>

In the preceding diagram, Systems Manager uses Session Manager to access the EC2 instance without having to connect to the instance using SSH. Session Manager is one of the secure ways to access the instance.

In this task, I access the EC2 instance through Session Manager.

## Conclusion

After completing this lab, I am able to use Systems Manager to:

* Verify configurations and permissions
* Run tasks on multiple servers
* Update application settings or configurations
* Access the command line on an instance

## Additional resources

* [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
* [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
