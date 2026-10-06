# Working with AWS CloudTrail

## Activity overview

In this activity, I create an AWS CloudTrail trail that audits actions taken in my account. I then investigate to determine who modified the Café website.

The activity starts with an Amazon Elastic Compute Cloud (Amazon EC2) instance named Café Web Server, which runs a web application that hosts the Café website.

I first observe that the website looks normal. Soon after creating a trail with CloudTrail, I notice that the website has been hacked, and that part of the hack involved an action during which someone modified the security group settings. I use a variety of methods to analyze the CloudTrail logs, including the Linux `grep` utility and the AWS Command Line Interface (AWS CLI), and then use Amazon Athena to search the CloudTrail logs further, working to identify the hacker. Once I discover the culprit, I remove that user's access and take steps to reduce the chances that the AWS account and the Café website will be hacked again.

<p align="center">
  <img src="images/cloudtrail-lab-diagram.png" alt="The architectural diagram illustrates the setup that this activity uses” width="900">
</p>

*The architectural diagram illustrates the setup that this activity uses.*

## Business case relevance

### A new request from the Café leadership team

<p align="center">
  <img src="images/ct-cafe-logo.png" alt="Cafe Logo" width="900">
</p>

Martha and Frank are concerned because the website was hacked. They are relying on me to discover who did it and to make sure it does not happen again.

Faythe, Frank, Martha, and others make frequent changes to the website, and sometimes those changes cause issues. This morning, it looks like the website was hacked, and Martha and Frank are asking me if there is a way to track what was changed and who made the changes.

I play the role of Sofîa, becoming a detective to discover the culprit.

## Task 1: Modifying a security group and observing the website

1. From the **Services** menu, I open the **EC2 Management Console**.
2. I choose **Instances**, locate and select the **Café Web Server (WebSecurityGroup)** instance, then in the **Security** tab, choose the `sg-xxxxxxxxxx` security group.
3. In the **Inbound rules** tab, I notice that only one inbound rule has been defined, for HTTP access over TCP port 80.
4. I choose **Edit inbound rules**, then **Add rule**, and configure it as follows:
   * **Type:** `SSH`
   * **Port Range:** `22`
   * **Source:** `My IP`

> [!NOTE]
> I confirm that the `TCP port 22` access is open only to my IP address. The entry should show a Classless Inter-Domain Routing (CIDR) block with a particular IP address followed by `/32`, not open to all IP addresses (which would be shown by `0.0.0.0/0`).

5. I observe the Café website: in **Instances**, I select the **Café Web Server** instance, click the **Details** tab, and copy the **Public IPv4 address** value. I open a new browser tab and navigate to `http://<WebServerIP>/cafe/`.

<p align="center">
  <img src="images/initial-cafe-web-load.png" alt="Café website homepage appearing normal" width="900">
</p>

*I notice the website looks normal — for example, the photos are all appropriate for a bakery café.*










## Conclusion

After completing this activity, I am able to:

* Configure a CloudTrail trail
* Analyze CloudTrail logs using various methods to discover relevant information
* Import CloudTrail log data into Athena
* Run queries in Athena to filter CloudTrail log entries
* Resolve security concerns within the AWS account and on an EC2 Linux instance


## Additional resources

* [AWS CLI Reference page for CloudTrail](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/)
* [Understanding CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html)
* [Query AWS CloudTrail logs](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html)

