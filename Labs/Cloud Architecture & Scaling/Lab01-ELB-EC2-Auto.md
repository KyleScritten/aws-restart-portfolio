# Scaling and Load Balancing Your Architecture

## Lab overview
In this lab, I use Elastic Load Balancing (ELB) and Amazon EC2 Auto Scaling to load balance and automatically scale my infrastructure.

> [!NOTE]
> **ELB** automatically distributes incoming application traffic across multiple Amazon Elastic Compute Cloud (Amazon EC2) instances, providing the amount of load balancing capacity needed to route application traffic and help achieve fault tolerance in applications.
>
> **Auto Scaling** helps maintain application availability and provides the ability to scale Amazon EC2 capacity out or in automatically according to defined conditions. Auto Scaling helps ensure I am running my desired number of EC2 instances, automatically increasing capacity during spikes in demand to maintain performance and decreasing capacity during lulls to reduce costs. Auto Scaling is well suited to applications that have stable demand patterns or that experience hourly, daily, or weekly variability in usage.

*The following is the starting architecture:*

<p align="center">
  <img src="images/01-starting-architecture.png" alt="Starting Lab Architecture" width="900">
</p>

*The following is the final architecture:*

<p align="center">
  <img src="images/01-final-architecture.png" alt="Final Lab Architecture" width="900">
</p>

## Task 1: Creating an AMI for auto scaling
In this task, I create an AMI from the existing **Web Server 1**. This saves the contents of the boot disk so that new instances can be launched with identical content.

1. On the AWS Management Console, in the search bar, I enter and choose `EC2` to open the Amazon EC2 Management Console.
2. In the left navigation pane, I locate the **Instances** section and choose **Instances**. The **Web Server 1** instance is listed. I now create an AMI based on this instance.
3. I choose the **Web Server 1** instance, which appears in a **Running** state.
4. From the **Actions** dropdown list, I choose **Image and templates > Create image**, and configure the following options:
   * **Image name:** `Web Server AMI`
   * **Image description - optional:** `Lab AMI for Web Server`
5. I choose **Create image**.

<p align="center">
  <img src="images/AMI-creation.png" alt="Creating an AMI for auto scaling" width="900">
</p>

*The confirmation screen displays the AMI ID `PLACHOLDER_AMI_ID` for my new AMI. I use this AMI when launching the Auto Scaling group later in the lab.*

## Task 2: Creating a load balancer
In this task, I create a load balancer that can balance traffic across multiple EC2 instances and Availability Zones.

1. I locate the **Load Balancing** section and choose **Load Balancers**.
2. I choose **Create load balancer**.
3. In the **Load balancer types** section, for **Application Load Balancer**, I choose **Create**.
4. In the **Basic configuration** section, I configure the following option:
   * **Load balancer name:** `LabELB`
5. In the **Network mapping** section, I configure the following options:
   * **VPC:** Choose **Lab VPC**
   * **Mappings:** Choose both Availability Zones listed
   * For the first Availability Zone, choose **Public Subnet 1**
   * For the second Availability Zone, choose **Public Subnet 2**
6. In the **Security groups** section, I choose the `X` for the default security group to remove it.
7. From the **Security groups** dropdown list, I choose `Web Security Group`.
8. In the **Listeners and routing** section, I choose the **Create target group** link.

   > [!NOTE]
   > This link opens a new browser tab with the Create target group configuration options.

9. On the new **Target groups** browser tab, in the **Basic configuration** section, I configure the following and choose **Next**:
   * **Choose a target type:** `Instances`
   * **Target group name:** `lab-target-group`
10. On the **Register targets** page, I choose **Create target group**. Once the target group is created successfully, I close the Target groups browser tab.
11. I return to the Load balancers browser tab. In the **Listeners and routing** section, I choose **Refresh** to the right of the **Forward to** dropdown list for **Default action**.
12. From the **Forward to** dropdown list, I choose `lab-target-group`.
13. At the bottom of the page, I choose **Create load balancer**.

<p align="center">
  <img src="images/ELB-creation.png" alt="Creating a load balancer" width="900">
</p>

I receive a message similar to the following: "Successfully created load balancer: LabELB"

14. To view the **LabELB** load balancer I created, I choose **View load balancer**.
15. I copy the DNS name of the load balancer, for later use in the lab:

```
PLACEHOLDER_DNS_NAME
```

## Conclusion

After completing this lab, I am able to:

* Create an AMI from an EC2 instance
* Create a load balancer
* Create a launch template and an Auto Scaling group
* Configure an Auto Scaling group to scale new instances within private subnets
* Use CloudWatch alarms to monitor the performance of my infrastructure
