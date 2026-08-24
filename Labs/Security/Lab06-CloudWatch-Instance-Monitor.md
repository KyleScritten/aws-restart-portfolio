# Monitor an EC2 Instance with Amazon CloudWatch

## Lab overview

In this lab, I create an Amazon CloudWatch alarm that triggers when the Amazon Elastic Compute Cloud (Amazon EC2) instance exceeds a specific central processing unit (CPU) utilization threshold. I create a subscription using Amazon Simple Notification Service (Amazon SNS) that sends me an email if this alarm goes off. I then log in to the EC2 instance and run a stress test command that causes the CPU utilization of the EC2 instance to reach 100 percent.

This test simulates a malicious actor gaining control of the EC2 instance and spiking the CPU. CPU spiking has various possible causes, one of which is malware.

> [!NOTE]
> Logging refers to recording and storing data events as log files. Logs contain low-level details that can provide visibility into how an application or system performs under certain circumstances. From a security standpoint, logging helps security administrators identify red flags that are easily overlooked in their system.
>
> Monitoring is the process of analyzing and collecting data to help ensure optimal performance. Monitoring helps detect unauthorized access and helps align service usage with organizational security.

## Conclusion

After completing this lab, I am able to:

* Create an Amazon SNS notification
* Configure a CloudWatch alarm
* Stress test an EC2 instance
* Confirm that an Amazon SNS email was sent
* Create a CloudWatch dashboard
