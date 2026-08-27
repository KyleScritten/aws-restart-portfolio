# Using Auto Scaling in AWS (Linux)

## Lab overview
In this lab, I use the AWS Command Line Interface (AWS CLI) to create an Amazon Elastic Compute Cloud (EC2) instance to host a web server and create an Amazon Machine Image (AMI) from that instance. I then use that AMI as the basis for launching a system that scales automatically under variable load using Amazon EC2 Auto Scaling. I also create an Elastic Load Balancer to distribute the load across EC2 instances created in multiple Availability Zones by the Auto Scaling configuration.

*Starting architecture:*

<p align="center">
  <img src="images/02-starting-architecture.png" alt="Starting lab architecture” width="600">
</p>

*Final architecture:*

<p align="center">
  <img src="images/02-final-architecture.png" alt="Final lab architecture” width="600">
</p>

## Task 1

## Task 2: Creating an auto scaling environment
In this section, I create a load balancer that pools a group of EC2 instances under a single Domain Name System (DNS) address. I use Auto Scaling to create a dynamically scalable pool of EC2 instances based on the image I created in the previous task. Finally, I create a set of alarms that scale out or scale in the number of instances in my load balancer group whenever the CPU performance of any machine within the group exceeds or falls below a set of specified thresholds.

### Task 2.1 Creating a load balancer
In this task, I create a load balancer that can balance traffic across multiple EC2 instances and Availability Zones.

1. I locate the **Load Balancing** section and choose **Load Balancers**.
2. I choose **Create load balancer**.
3. In the **Load balancer types** section, for **Application Load Balancer**, I choose **Create**.
4. In the **Basic configuration** section, I configure the following option:
   * **Load balancer name:** `WebServerELB`
5. In the **Network mapping** section, I configure the following options:
   * **VPC:** Choose `Lab VPC`
   * **Mappings:** Choose both Availability Zones listed
   * For the first Availability Zone, choose **Public Subnet 1**
   * For the second Availability Zone, choose **Public Subnet 2**
6. In the **Security groups** section, I choose the `X` for the default security group to remove it.
7. From the **Security groups** dropdown list, I choose `Web Security Group`.

## Conclusion
After completing this lab, I am able to:

* Create an EC2 instance using an AWS CLI command
* Create a new AMI using the AWS CLI
* Create an Amazon EC2 launch template
* Create an Amazon EC2 Auto Scaling launch configuration
* Configure scaling policies and create an Auto Scaling group to scale in and scale out the number of servers based on variable load

## Additional resources
* [Amazon EC2 Auto Scaling Getting Started](https://aws.amazon.com/ec2/autoscaling/getting-started/)
* [Getting Started with Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/getting-started)
