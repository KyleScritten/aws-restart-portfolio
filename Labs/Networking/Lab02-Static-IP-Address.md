# Internet Protocols - Static and Dynamic Addresses

In this lab, I will act as a cloud support engineer at Amazon Web Services (AWS) and investigate a networking issue reported by Bob, a customer from a Fortune 500 company. I will discover that Bob's EC2 instance is assigned a dynamic IP address, which changes every time the instance is stopped and started, and that he cannot leave the instance running continuously due to the associated cost. I will recommend attaching an Elastic IP (EIP) to provide Bob's instance with a persistent, static IP address so that his other resources are not disrupted. I will verify this solution by stopping and starting the instance to confirm that the IP address remains unchanged after the Elastic IP is attached.












## Conclusion
After completing this lab, I have successfully:

* Summarized the customer scenario
* Analyzed the difference between statically and dynamically assigned IP addresses using EC2 instances
* Assigned a persistent (static) IP to an EC2 instance
* Developed a solution to the customer's issue found within this lab, and summarized and described my findings
