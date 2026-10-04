# Monitoring Infrastructure

The ability to monitor my applications and infrastructure is critical for delivering reliable, consistent IT services.

Monitoring requirements range from collecting statistics for long-term analysis to quickly reacting to changes and outages. Monitoring can also support compliance reporting by continuously checking that infrastructure is meeting organizational standards.

This lab shows me how to use Amazon CloudWatch Metrics, Amazon CloudWatch Logs, Amazon CloudWatch Events, and AWS Config to monitor my applications and infrastructure.

## Task 1: Installing the CloudWatch agent

In this task, I use Systems Manager to install the CloudWatch agent on an EC2 instance, and configure it to collect both application and system metrics.

<p align="center">
  <img src="images/mi-lab-diagram.png" alt="Lab Diagram” width="900">
</p>

>[!Note]
> I can use the CloudWatch agent to collect metrics from EC2 instances and on-premises servers, including:
> * System-level metrics from EC2 instances, such as CPU allocation, free disk space, and memory utilization — these metrics are collected from the machine itself and complement the standard CloudWatch metrics that CloudWatch collects
>  * System-level metrics from on-premises servers, enabling the monitoring of hybrid environments and servers not managed by AWS
> * System and application logs from both Linux and Windows servers
> * Custom metrics from applications and services using the [StatsD](https://github.com/etsy/statsd) and [collectd](https://collectd.org/) protocols






## Conclusion

After completing this lab, I am able to successfully:

* Use the AWS Systems Manager Run Command to install the CloudWatch agent on Amazon Elastic Compute Cloud (Amazon EC2) instances
* Monitor application logs using the CloudWatch agent and CloudWatch Logs
* Monitor system metrics using the CloudWatch agent and CloudWatch Metrics
* Create real-time notifications using CloudWatch Events
* Track infrastructure compliance using AWS Config
