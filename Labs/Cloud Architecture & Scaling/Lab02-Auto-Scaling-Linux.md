# Using Auto Scaling in AWS (Linux)

## Lab overview
In this lab, I use the AWS Command Line Interface (AWS CLI) to create an Amazon Elastic Compute Cloud (EC2) instance to host a web server and create an Amazon Machine Image (AMI) from that instance. I then use that AMI as the basis for launching a system that scales automatically under variable load using Amazon EC2 Auto Scaling. I also create an Elastic Load Balancer to distribute the load across EC2 instances created in multiple Availability Zones by the Auto Scaling configuration.

*Starting architecture:*

<p align="center">
  <img src="images/02-starting-architecture.png" alt="Starting lab architecture” width="800">
</p>

*Final architecture:*

<p align="center">
  <img src="images/02-final-architecture.png" alt="Final lab architecture” width="800">
</p>

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
