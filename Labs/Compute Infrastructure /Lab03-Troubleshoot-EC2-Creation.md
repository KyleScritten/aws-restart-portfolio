# Troubleshooting the Creation of an EC2 Instance

## Activity overview

In this activity, I use the AWS Command Line Interface (AWS CLI) to launch Amazon Elastic Compute Cloud (Amazon EC2) instances.

When creating the instance, I reference a user data script to configure it with an Apache web server, a MariaDB relational database (a fork of the MySQL relational database), and PHP. Together, these software packages installed on a single machine are often referred to as a ***LAMP*** stack (**L**inux, **A**pache web server, **M**ySQL, and **P**HP) — a common way to create a website with a database backend on a single machine.

The same user data file deploys website files and runs database configuration scripts on the instance, resulting in an instance that hosts the Café Web Application.

<p align="center">
  <img src="images/troubleshoot-create-ec2.png" alt="Troubleshooting the Creation of an EC2 Instance Architecture" width="1000">
</p>

*The following diagram shows the architecture I create in this activity.*

## Task 1: Connecting to the CLI Host instance
In this task, I use EC2 Instance Connect to connect to the CLI Host EC2 instance that was created when the lab was provisioned. I use this instance to run CLI commands.

1. On the Amazon EC2 Management Console, I choose **Instances**.
2. From the list of instances, I select the `CLI Host` instance.
3. Above the list of instances, I choose **Connect**.
4. On the **EC2 Instance Connect** tab, I choose **Connect**.

## Task 2: Configuring the AWS CLI
In this task, I configure the AWS CLI using the configuration parameters made available to me when the lab was provisioned. After configuration, I run CLI commands to interact with AWS services.

> [!NOTE]
> Amazon Linux Amazon Machine Images (AMIs) already have the AWS CLI preinstalled.

1. In the SSH session terminal window, I run the `aws configure` command to set up the AWS CLI profile with credentials.
2. At the prompt, I configure the following:
   * **AWS Access Key ID:** `<AWS Access Key ID>`
   * **AWS Secret Access Key:** `<AWS Secret Access Key>`
   * **Default region name:** Enter `us-west-2`
   * **Default output format:** Enter `json`

#### Terminal output
```bash
PASTE_FROM_LAB
```





## Task 4: Verifying the functionality of the website

1. I verify that the website is deployed. In a browser, I navigate to the following address: `http://<public-ip>/cafe`

<p align="center">
  <img src="images/verify-web-deploy.png" alt="Verify that the website deploys" width="900">
</p>

*If successful, I see the home page for the café website.*

2. I now test whether I can order items through the website.
   * I choose the **Menu** link, and a new page loads at `http://<public-ip>/cafe/menu.php`.
   * I choose a few desserts to order, then choose **Submit Order**. The **Order Confirmation** page displays with line-item details.
   * I place another order for different items, then choose the **Order History** page, and confirm that the details of both orders were captured.

<p align="center">
  <img src="images/order-history-test.png" alt="Website order history page" width="900">
</p>

*The order details are being captured and stored in the database running on the LAMP instance I launched.*

## Conclusion

After completing this activity, I am able to:
* Launch an EC2 instance using the AWS CLI
* Troubleshoot AWS CLI commands and Amazon EC2 service settings using basic troubleshooting tips and the open-source `nmap` utility
