# Configuring a VPC

## Lab overview
Amazon Virtual Private Cloud (Amazon VPC) gives me the ability to provision a logically isolated section of the Amazon Web Services (AWS) Cloud where I can launch AWS resources in a virtual network that I define. I have complete control over my virtual networking environment, including selecting my IP address ranges, creating subnets, and configuring route tables and network gateways.

In this lab, I build a virtual private cloud (VPC) and other network components required to deploy resources, such as an Amazon Elastic Compute Cloud (Amazon EC2) instance.

<p align="center">
  <img src="images/config-vpc-architecture.png" alt="Configuring a VPC Architecture” width="900">
</p>

## Task 1: Creating a VPC
In this task, I create a new VPC.

1. On the AWS Management Console, in the search bar, I enter and choose `VPC` to go to the VPC Management Console.
2. In the left navigation pane, for **Virtual private cloud**, I choose **Your VPCs**.
   
> [!NOTE]
> In every Region, a default VPC with a Classless Inter-Domain Routing (CIDR) block of `172.31.0.0/16` has already been created for me. Even if I haven't created anything in my account yet, I see some pre-existing VPC resources already there.

3. I choose **Create VPC** and configure the following options:
   * **Resources to create:** Choose **VPC only**
   * **Name tag:** Enter `Lab VPC`
   * **IPv4 CIDR block:** Choose **IPv4 CIDR manual input**
   * **IPv4 CIDR:** Enter `10.0.0.0/16`
   * **IPv6 CIDR block:** Choose **No IPv6 CIDR block**
   * **Tenancy:** Choose **Default**
   * **Tags:** Leave the suggested tags as is
4. I choose **Create VPC**. At the top of the page, a message displays similar to the following: "You successfully created vpc-NNNNNNNNNNN / Lab VPC."
5. I choose **Actions**, then choose **Edit VPC settings**.
6. In the **DNS settings** section, I select **Enable DNS hostnames**, then choose **Save**.

*EC2 instances launched into the VPC now automatically receive a public IPv4 Domain Name System (DNS) hostname.*











## Conclusion
By the end of this lab, I am able to:

* Create a VPC with a private and public subnet, an Internet Gateway, and a NAT Gateway
* Configure route tables associated with subnets to local and internet-bound traffic by using an Internet Gateway and a NAT Gateway
* Launch a bastion server in a public subnet
* Use a bastion server to log in to an instance in a private subnet
* Completed the optional challenge section in which I created an Amazon EC2 instance in a private subnet and connected to it through the bastion server

## Additional resources
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html)
