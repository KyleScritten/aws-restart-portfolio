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

<p align="center">
  <img src="images/creating-vpc.png" alt="Creating a VPC” width="900">
</p>

*EC2 instances launched into the VPC now automatically receive a public IPv4 Domain Name System (DNS) hostname.*

## Task 2: Creating subnets
In this task, I create a public subnet and a private subnet.

1. In the left navigation pane, for **Virtual private cloud**, I choose **Subnets**.
2. I choose **Create subnet** and configure the following options:
   * **VPC ID:** Choose **Lab VPC**
   * **Subnet name:** Enter `Public Subnet`
   * **Availability Zone:** Choose the first Availability Zone in the list (not **No preference**)
   * **IPv4 CIDR block:** Enter `10.0.0.0/24`
3. I choose **Create subnet**.
4. I now configure the public subnet to automatically assign a public IP address for all EC2 instances launched within it. I select **Public Subnet**, choose **Actions**, then choose **Edit subnet settings**.
5. In the **Auto-assign IP settings** section, I select **Enable auto-assign public IPv4 address**, then choose **Save**.

> [!NOTE]
> Even though this subnet has been named Public Subnet, it is not yet public. A public subnet must have an Internet Gateway, which I attach in a later task in the lab.

6. To create the private subnet, which is used for resources that remain isolated from the internet, I repeat the steps from the previous task and choose the following options:
   * **VPC ID:** Choose **Lab VPC**
   * **Subnet name:** Enter `Private Subnet`
   * **Availability Zone:** Choose the first Availability Zone in the list (not **No preference**)
   * **IPv4 CIDR block:** Enter `10.0.2.0/23`
7. I choose **Create subnet**.

> [!NOTE]
> The CIDR block `10.0.2.0/23` includes all IP addresses that start with `10.0.2.x` and `10.0.3.x`. This range is twice as large as the public subnet, since most resources should be kept in private subnets unless they specifically need to be accessible from the internet.

<p align="center">
  <img src="images/creating-subnets.png" alt="Created a public subnet and a private subnet." width="900">
</p>

*My VPC now has two subnets. However, the VPC is totally isolated and cannot communicate with resources outside the VPC.*

## Task 3: Creating an internet gateway
In this task, I create an Internet Gateway for my VPC. I need an Internet Gateway to establish outside connectivity to EC2 instances in my VPC.

1. In the left navigation pane, for **Virtual private cloud**, I choose **Internet gateways**.
2. I choose **Create internet gateway**, and for **Name tag**, I enter `Lab IGW`.
3. I choose **Create internet gateway**.
4. I choose **Actions**, then choose **Attach to a VPC**.

<p align="center">
  <img src="images/create-internet-gateway.png" alt="Created an internet gateway” width="900">
</p>

*My public subnet now has a connection to the internet. However, to route traffic to the internet, I must also configure the public subnet's route table so that it uses the Internet Gateway.*

## Task 4: Configuring route tables
In this task, I do the following:

* Create a public route table for internet-bound traffic.
* Add a route to the route table to direct internet-bound traffic to the Internet Gateway.
* Associate the public subnet with the new route table.

1. In the left navigation pane, for **Virtual private cloud**, I choose **Route tables**. Several route tables are listed.
2. I select the route table that includes **Lab VPC** in the **VPC** column.
3. In the **Name** column, I choose the edit icon, enter `Private Route Table` for **Edit Name**, then choose **Save**.
4. I choose the **Routes** tab.

> [!NOTE]
> There is currently only one route. It shows that all traffic destined for `10.0.0.0/16` (the range of the Lab VPC) is routed locally. This allows all subnets within a VPC to communicate with each other.

5. I now create a new public route table to send public traffic to the Internet Gateway. I choose **Create route table** and configure the following options:
   * **Name - optional:** Enter `Public Route Table`
   * **VPC:** Choose **Lab VPC**
6. I choose **Create route table**.
7. After the route table is created, in the **Routes** tab, I choose **Edit routes**.

> [!NOTE]
> I now add a route to direct internet-bound traffic (`0.0.0.0/0`) to the Internet Gateway.

8. I choose **Add route** and configure the following options:
   * **Destination:** Enter `0.0.0.0/0`
   * **Target:** Choose **Internet Gateway**, then choose **Lab IGW** from the list
9. I choose **Save changes**.
10. The final step is to associate this new route table with the public subnet. I choose the **Subnet associations** tab, choose **Edit subnet associations**, select **Public Subnet**, and choose **Save associations**.

<p align="center">
  <img src="images/config-route-table.png" alt="Configuring route tables” width="900">
</p>

*The public subnet is now public because it has a route table entry that sends traffic to the internet through the Internet Gateway.*

## Task 5: Launching a bastion server in the public subnet
In this task, I launch an EC2 instance bastion server in the public subnet I created earlier.

> [!NOTE]
> A bastion server (also known as a jump box) is an EC2 instance in a public subnet that is securely configured to provide access to resources in a private subnet. Systems operators can connect to the bastion server and then jump into resources in the private subnet.

1. On the AWS Management Console, in the search bar, I enter and choose `EC2` to go to the EC2 Management Console, then choose **Instances**.
2. I choose **Launch instances** and configure the following options:
   * In the **Name and tags** section, I enter `Bastion Server`.
   * In the **Application and OS Images (Amazon Machine Image)** section, I configure the following options:
     * **Quick Start:** Choose **Amazon Linux**
     * **Amazon Machine Image (AMI):** Choose **Amazon Linux 2023 AMI**
   * In the **Instance type** section, I choose **t3.micro**.
   * In the **Key pair (login)** section, I choose **Proceed without a key pair (Not recommended)**.

> [!NOTE]
> I use EC2 Instance Connect to access the shell running on the EC2 instance, so a key pair is not needed in this lab.

3. In the **Network settings** section, I choose **Edit** and configure the following options:
   * **VPC - required:** Choose **Lab VPC**
   * **Subnet:** Choose **Public Subnet**
   * **Auto-assign public IP:** Choose **Enable**
   * **Firewall (security groups):** Choose **Create security group**
     * **Security group name - required:** Enter `Bastion Security Group`
     * **Description - required:** Enter `Allow SSH`
   * **Inbound security group rules:**
     * **Type:** Choose **SSH**
     * **Source type:** Choose **Anywhere**
4. I choose **Launch instance**.

<p align="center">
  <img src="images/ec2-bastion-instance.png" alt="Launching a bastion server in the public subnet" width="900">
</p>

*The EC2 instance named **Bastion Server** is initially in a **Pending** state. The instance state then changes to **Running** to indicate that the instance has finished booting. The bastion server is launched in the public subnet.*

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
