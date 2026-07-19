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

```
sudo su
cd /home/ec2-user/
```
