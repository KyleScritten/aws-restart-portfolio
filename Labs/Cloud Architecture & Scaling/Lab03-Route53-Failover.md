# Amazon Route 53 Failover Routing

## Lab overview
In this activity, I configure failover routing for a simple web application.

The activity environment starts with two Amazon Elastic Compute Cloud (Amazon EC2) instances that have already been created. Each instance has the full LAMP stack installed and the café website deployed and running. The EC2 instances are deployed in different Availability Zones. For example, if the web servers are running in the us-west-2 Region, one web server runs in the us-west-2a Availability Zone and the other runs in the us-west-2b Availability Zone.

I configure my domain such that, if the website in the primary Availability Zone becomes unavailable, Amazon Route 53 automatically fails over application traffic to the instance in the secondary Availability Zone.

When finished, my environment looks like the following architecture:

<p align="center">
  <img src="images/03-final-architecture.png" alt="Amazon Route 53 Failover Routing Final Architecture" width="900">
</p>

Route 53 records store the IP address of the EC2 instance in each Availability Zone. User requests are normally sent to the IP address corresponding to Café Instance1 in Availability Zone 1. If Café Instance1 is unavailable, requests are routed to Café Instance2 in Availability Zone 2, based on the configuration in the Route 53 records. When Café Instance1 becomes unavailable, a Route 53 health check alarm is invoked, and an email alert is sent to the email address provided.




## Conclusion
After completing this activity, I am able to:

* Configure a Route 53 health check that sends emails when the health of an HTTP endpoint becomes unhealthy
* Configure failover routing in Route 53

## Additional resources
* [Amazon Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html)
* [Amazon Route 53 Failover routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)
