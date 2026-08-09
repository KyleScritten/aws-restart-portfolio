# Creating Networking Resources in an Amazon Virtual Private Cloud (VPC)
My role is a Cloud Support Engineer at Amazon Web Services (AWS). During my shift, a customer from a startup company requests assistance regarding a networking issue within their AWS infrastructure. The email and an attachment of their architecture are below.

## Scenario
In this lab, I will investigate the customer's environment and analyze the customer's request to build a fully functional VPC. Through this experience, I will apply a blended approach of the OSI model and how AWS cloud fits into that model. I will create resources starting with a VPC, and work my way down the left-hand navigation pane to assist the customer in having their EC2 instance successfully achieve network connectivity.

**Email from the customer**

> Hello Cloud Support!
>
> I previously reached out to you regarding help setting up my VPC. I thought I knew how to attach all the resources to make an internet connection, but I cannot even ping outside the VPC. All I need to do is ping! Can you please help me set up my VPC to where it has network connectivity and can ping? The architecture is below. Thanks!
>
> Brock, startup owner

<p align="center">
  <img src="images/network-vpc-architecture.png" alt="VPC Networking Resources Architecture” width="900">
</p>

## Task 1: Investigate the customer's needs
In the scenario, Brock, the customer requesting assistance, has requested help creating resources for his VPC to be routable to the internet. I keep the VPC CIDR at `192.168.0.0/18` and the public subnet CIDR at `192.168.1.0/26`.

>[!Note]
> Protocols which can be directly used with AWS's Security Group (SG) and Network Access Control Lists (NACLs). A VPC needs an Internet Gateway (IGW) in order for the VPC to reach the internet, which has the route as 0.0.0.0/0. These routes go on what is called a Route Table, which are associated to subnets so they know where they belong. As mentioned in previous labs, you will follow the order of the navigation console to build this VPC, and a troubleshooting method to build a fully functioning VPC. When building a VPC from scratch, it is easier to work from the top and move down to the bottom since you do not have an instance yet. Think of this as building a sandwich; the VPC is the bun, and the resources are everything in between.





## Task 2: Launch EC2 instance and SSH into instance



## Task 3: Use ping to test internet connectivity



## Conclusion
By completing this lab, I have successfully:

* Summarized the customer scenario
* Created a VPC, Internet Gateway, Route Table, Security Group, Network ACL, and EC2 instance to establish a routable network within the VPC
* Familiarized myself with the console
* Developed a solution to the customer's issue found within this lab

The lab is complete now that I have successfully used the `ping` command outside the VPC.

## Additional Resources
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [IP Addressing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
- [Route tables for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-rules)
- [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#VPCSecurityGroups)
