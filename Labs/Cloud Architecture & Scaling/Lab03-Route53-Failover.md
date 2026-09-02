# Amazon Route 53 Failover Routing

## Lab overview
In this activity, I configure failover routing for a simple web application.

The activity environment starts with two Amazon Elastic Compute Cloud (Amazon EC2) instances that have already been created. Each instance has the full LAMP stack installed and the café website deployed and running. The EC2 instances are deployed in different Availability Zones. For example, if the web servers are running in the us-west-2 Region, one web server runs in the us-west-2a Availability Zone and the other runs in the us-west-2b Availability Zone.

I configure my domain such that, if the website in the primary Availability Zone becomes unavailable, Amazon Route 53 automatically fails over application traffic to the instance in the secondary Availability Zone.

*When finished, my environment looks like the following architecture:*

<p align="center">
  <img src="images/03-final-architecture.png" alt="Amazon Route 53 Failover Routing Final Architecture" width="900">
</p>

*Route 53 records store the IP address of the EC2 instance in each Availability Zone. User requests are normally sent to the IP address corresponding to Café Instance1 in Availability Zone 1. If Café Instance1 is unavailable, requests are routed to Café Instance2 in Availability Zone 2, based on the configuration in the Route 53 records. When Café Instance1 becomes unavailable, a Route 53 health check alarm is invoked, and an email alert is sent to the email address provided.*

## Task 1: Confirming the café websites
In this task, I analyze the resources that AWS CloudFormation has automatically created for me.

1. I copy the values for the following parameters from the predefined lab credentials:
   * **CafeInstance1IPAddress:** ``
   * **PrimaryWebSiteURL:** ``
   * **SecondaryWebsiteURL:** ``
   * **CafeInstance2IPAddress:** ``
2. I navigate to the EC2 Management Console, and in the **Instances** section, choose **Instances**.

Two EC2 instances have already been created for me. `CafeInstance1` is running in **Cafe Public Subnet 1** (us-west-2a), and `CafeInstance2` is running in **Cafe Public Subnet 2** (us-west-2b).

> [!NOTE]
> The URLs from the lab credentials section correspond to the café application running on each instance.

3. I open a new browser tab and navigate to the `PrimaryWebSiteURL`.

<p align="center">
  <img src="images/primary-web-url.png" alt="PrimaryWebSiteURL Homepage" width="900">
</p>

*The café application webpage opens.*

4. I open the `SecondaryWebsiteURL` in another browser tab.

<p align="center">
  <img src="images/secondary-web-url.png" alt="SecondaryWebsiteURL Homepage" width="900">
</p>

*These configurations confirm that the café application is running on both instances.*

5. On the first website, I choose **Menu**, choose any item on the menu, then select **Submit Order**.

<p align="center">
  <img src="images/order-confirmation.png" alt="The Order Confirmation page from the PrimaryWebSiteURL" width="900">
</p>

*The **Order Confirmation** page reflects the time the order was placed in the time zone where the web server is running.*

I have now confirmed that two instances are running the café application, each in a different Availability Zone to provide high availability.

## Task 2: Configuring a Route 53 health check
The first step to configure failover is to create a health check for my primary website.

1. In the AWS Management Console, I open the Route 53 Management Console.
2. I choose **Health checks**, then choose **Create health check**, and configure the following options:
   * **Name:** `Primary-Website-Health`
   * **What to monitor:** Choose `Endpoint`
   * **Specify endpoint by:** Choose `IP address`
   * **IP address:** Paste in the Public IPv4 address of `CafeInstance1`. I find this value in the EC2 console, or copy the IP address from the `CafeInstance1IPAddress` value I copied earlier.
   * **Path:** Enter `cafe`
3. I expand **Advanced configuration** and configure the following options:
   * **Request interval:** Choose `Fast (10 seconds)`
   * **Failure threshold:** Enter `2`
4. For **Get notified when health check fails**, I configure the following options:
   * **Create alarm:** Choose `Yes`
   * **Send notification to:** Choose `New SNS topic`
   * **Topic name:** Enter `Primary-Website-Health`
   * **Recipient email address:** `<My Email address>`
5. I choose **Create health check**.

> [!NOTE]
> Route 53 now checks the health of my site by periodically requesting the domain name I provided and verifying that it returns a successful response. The health check might take up to a minute to show a **Healthy** status.

6. I select **Primary-Website-Health**, then choose the **Monitoring** tab.
7. I check my email have an email from AWS Notifications.
8. In the email, I choose the **Confirm subscription** link to finish setting up the email alerting I configured when creating the health check.

<p align="center">
  <img src="images/health-check-config.png" alt="Configuring a Route 53 Health Check" width="900">
</p>

*This tab provides a view of the status of the `Primary-Website-Health` health check over time. It might take a few seconds before the chart becomes available.*

## Conclusion
After completing this activity, I am able to:

* Configure a Route 53 health check that sends emails when the health of an HTTP endpoint becomes unhealthy
* Configure failover routing in Route 53

## Additional resources
* [Amazon Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html)
* [Amazon Route 53 Failover routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)
