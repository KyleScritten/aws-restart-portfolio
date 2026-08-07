# Internet Protocols - Public and Private IP addresses

In this lab, I will investigate the customer's environment and apply troubleshooting techniques to resolve the customer's issue. Within the scenario, I will discover that the customer's EC2 instance (instance A) needs a public IP address to connect to the internet, which I will test by using an SSH utility to connect to the instance. I will note that private IP addresses are used within the VPC and cannot establish a connection to the internet. I will also discover that using a public range of IP addresses for a VPC can lead to complications, such as receiving replies from unrelated external resources.

## Scenario

My role is a cloud support engineer at Amazon Web Services (AWS). During my shift, a customer from a Fortune 500 company requests assistance regarding a networking issue within their AWS infrastructure. The following is the email and an attachment regarding their architecture:

Ticket from the customer

>Hello, Cloud Support!
>
>We currently have one virtual private cloud (VPC) with a CIDR range of 10.0.0.0/16. In this VPC, we have two Amazon Elastic Compute Cloud
>(Amazon EC2) instances: instance A and instance B. Even though both are in the same subnet and have the same configurations with AWS resources,
>instance A cannot reach the internet, and instance B can reach the internet. I think it has something to do with the EC2 instances, but I'm not sure.
>I also had a question about using a public range of IP address such as 12.0.0.0/16 for a VPC that I would like to launch. Would that cause any issues?
>Attached is our architecture for reference.
>
>Thanks!
>
>Jess
>
>Cloud Admin
