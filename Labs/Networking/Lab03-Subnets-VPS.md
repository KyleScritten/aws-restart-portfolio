# Create Subnets and Allocate IP addresses in an Amazon Virtual Private Cloud (Amazon VPC)
In this lab, I investigated the customer's environment and analyzed the customer's request to build a successful walkthrough of their environment. Through this experience, I learned how to launch a VPC, which CIDR block and range to give the customer, and how to show the customer how to build a VPC.

## Scenario
My role is a cloud support engineer at Amazon Web Services (AWS). During my shift, a customer from a Fortune 500 company requests assistance regarding a networking issue within their AWS infrastructure. The following is the email and an attachment regarding their architecture:

**Ticket from the customer**

> Hello, Cloud Support!
>
> I'm new to AWS, and I need help setting up a VPC. Can you please help me through the setup process? I would like to build only the VPC part and would like to make it look something like the following picture. Can you help me ensure I have around 15,000 private IP addresses in this VPC available? I would also like the VPC IPv4 CIDR block to be a 192.x.x.x. I don't remember which is a private range though. Can you confirm that? I would also like to allocate at least 50 IP addresses for the public subnet.
>
> Thanks!
>
> Paulo Santos
> Startup Owner

**Architecture diagram**

<p align="center">
  <img src="images/vpc-subnet-architecture.png" alt="VPC Subnets and IP addresses Customer Architecture” width="900">
</p>

*Figure: In the customer's VPC architecture, the customer needs approximately 15,000 IP addresses for their Seattle office headquarters and 50 IP addresses for their operations department, which will be in the public subnet.*










## Conclusion
In this lab, I have successfully:

* Summarized the customer scenario
* Created an Amazon Virtual Private Cloud (Amazon VPC) and learned how to create subnets and allocate IP addresses
* Familiarized myself with the Amazon Web Services (AWS) Management Console
* Developed a solution to the customer's issue in this lab
* Summarized and described my findings (group activity)

## Additional resources
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [IP Addressing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
- [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918)
- [VPC CIDR](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#add-cidr-block-restrictions)
- [Subnet calculator](https://www.subnet-calculator.com/)
