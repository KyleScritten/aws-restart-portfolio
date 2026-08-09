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
  <img src="images/customer-vpc-architecture.png" alt="VPC Networking Resources Architecture” width="900">
</p>

## Task 1: Investigate the customer's needs
