# Using Auto Scaling in AWS (Linux)

## Lab overview
In this lab, I use the AWS Command Line Interface (AWS CLI) to create an Amazon Elastic Compute Cloud (EC2) instance to host a web server and create an Amazon Machine Image (AMI) from that instance. I then use that AMI as the basis for launching a system that scales automatically under variable load using Amazon EC2 Auto Scaling. I also create an Elastic Load Balancer to distribute the load across EC2 instances created in multiple Availability Zones by the Auto Scaling configuration.

*Starting architecture:*

<p align="center">
  <img src="images/02-starting-architecture.png" alt="Starting lab architecture” width="600">
</p>

*Final architecture:*

<p align="center">
  <img src="images/02-final-architecture.png" alt="Final lab architecture” width="600">
</p>

## Task 1: Creating a new AMI for Amazon EC2 Auto Scaling
In this task, I launch a new EC2 instance and then create a new AMI based on that running instance. I use the AWS CLI on the Command Host EC2 instance to perform all of these operations.

### Task 1.1: Connecting to the Command Host instance
In this task, I use EC2 Instance Connect to connect to the Command Host EC2 instance that was created when the lab was provisioned. I use this instance to run AWS CLI commands.

I navigate to the EC2 Management Console by entering `EC2` in the search bar of the AWS Management Console, then choose **Instances** in the navigation pane. From the list of instances, I select the **Command Host** instance, choose **Connect**, and on the **EC2 Instance Connect** tab, choose **Connect**.


### Task 1.2: Configuring the AWS CLI
The AWS CLI is preconfigured on the Command Host instance.

1. To confirm that the Region in which the Command Host instance is running matches the lab's Region (`us-west-2`), I run the following command:
```bash
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
```

2. To update the AWS CLI software with the correct credentials, I run the following command:
```bash
aws configure
```

3. At the prompts, I enter the following information:
   * **AWS Access Key ID:** Press Enter
   * **AWS Secret Access Key:** Press Enter
   * **Default region name:** Enter the Region name from the previous step (for example, `us-west-2`). If the Region is already displayed, press Enter.
   * **Default output format:** Enter `json`
4. To access the scripts, I run the `cd /home/ec2-user/` command to navigate to their directory

**Terminal output:**
```bash
   ,     #_
   ~\_  ####_        Amazon Linux 2
  ~~  \_#####\
  ~~     \###|       AL2 End of Life is 2026-06-30.
  ~~       \#/ ___
   ~~       V~' '->
    ~~~         /    A newer version of Amazon Linux is available!
      ~~._.   _/
         _/ _/       Amazon Linux 2023, GA and supported until 2029-06-30.
       _/m/'           https://aws.amazon.com/linux/amazon-linux-2023/

[ec2-user@ip-10-0-1-187 ~]$ curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   475  100   475    0     0   471k      0 --:--:-- --:--:-- --:--:--  463k
  "region" : "us-west-2",
[ec2-user@ip-10-0-1-187 ~]$ aws configure
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [us-west-2]: us-west-2
Default output format [None]: json
[ec2-user@ip-10-0-1-187 ~]$ 
```

### Task 1.3: Creating a new EC2 Instance
In this task, I use the AWS CLI to create a new instance that hosts a web server.

1. To inspect the `UserData.txt` script that was installed as part of the Command Host creation, I run the `more UserData.txt` command:

**Terminal output:**
```bash
[ec2-user@ip-10-0-1-187 ~]$ more UserData.txt
#!/bin/bash
yum update -y --security
amazon-linux-extras install epel -y
yum -y install httpd php stress
systemctl enable httpd.service
systemctl start httpd
cd /var/www/html
wget http://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-TULABS-1/10-lab-autoscaling-linux/s3/ec2-stress.zip
unzip ec2-stress.zip

echo 'UserData has been successfully executed. ' >> /home/ec2-user/result
find -wholename /root/.*history -wholename /home/*/.*history -exec rm -f {} \;
find / -name 'authorized_keys' -exec rm -f {} \;
rm -rf /var/lib/cloud/data/scripts/*
[ec2-user@ip-10-0-1-187 ~]$ 
```

> [!NOTE]
> This script performs a number of initialization tasks, including updating all installed software on the box and installing a small PHP web application that I can use to simulate a high CPU load on the instance.

2. From the Vocareum Lab Environment, I save the lab details, including the `KEYNAME`, `AMIID`, `HTTPACCESS`, and `SUBNETID` credential values.
3. In the following script, I replace the corresponding text with the values from the Vocareum Lab Environment:
```bash
aws ec2 run-instances --key-name KEYNAME --instance-type t3.micro --image-id AMIID --user-data file:///home/ec2-user/UserData.txt --security-group-ids HTTPACCESS --subnet-id SUBNETID --associate-public-ip-address --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' --output text --query 'Instances[*].InstanceId'
```

4. I enter my modified script into the terminal window and run it.

**Terminal output:**
```bash
[ec2-user@ip-10-0-1-187 ~]$ aws ec2 run-instances --key-name vockey --instance-type t3.micro --image-id ami-07d99f9a9d64e297d --user-data file:///home/ec2-user/UserData.txt --security-group-ids sg-04847ccd83a12b4e4 --subnet-id subnet-038c6488cc740773f --associate-public-ip-address --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' --output text --query 'Instances[*].InstanceId'
i-0ba722db5a584e6ca
[ec2-user@ip-10-0-1-187 ~]$ 
```

The output of this command provides an **InstanceId:** `i-0ba722db5a584e6ca`. Subsequent steps in this lab refer to this value as `NEW-INSTANCE-ID`.

5. To use the `aws ec2 wait instance-running` command to monitor this instance's status, I replace `NEW-INSTANCE-ID` in the following command with the InstanceID value I copied in the previous step, then run the modified command:
```bash
aws ec2 wait instance-running --instance-ids NEW-INSTANCE-ID
```

My instance starts a new web server. To test that the web server was installed properly, I must obtain the public DNS name.

6. To obtain the **Public DNS Name**, I replace `NEW-INSTANCE-ID` in the following command with the value I copied previously, then run the modified command:
```bash
aws ec2 describe-instances --instance-id NEW-INSTANCE-ID --query 'Reservations[0].Instances[0].NetworkInterfaces[0].Association.PublicDnsName'
```

7. I copy the output of this command without the quotation marks. The value of this output is referred to as `PUBLIC-DNS-ADDRESS`:
```bash
ec2-35-85-49-62.us-west-2.compute.amazonaws.com
```

8. In the following command, I replace `PUBLIC-DNS-ADDRESS` with the value I copied in the previous step, then run the modified command:
```bash
http://PUBLIC-DNS-ADDRESS/index.php
```

<p align="center">
  <img src="images/02-ec2-instance-web-app.png" alt="Load EC2 web server" width="900">
</p>

*I access the web application through the browser using the URL `http://ec2-35-85-49-62.us-west-2.compute.amazonaws.com/index.php` to confirm that the web server is functioning correctly.*

### Task 1.4: Creating a Custom AMI
Next, I created a custom AMI from the running EC2 instance using the AWS CLI by running the `aws ec2 create-image` command. This AMI captured the configured web server environment and would later be used to launch identical instances in the Auto Scaling Group.

```bash
[ec2-user@ip-10-0-1-187 ~]$ aws ec2 create-image --name WebServerAMI --instance-id i-0ba722db5a584e6ca
{
    "ImageId": "ami-0d3c084d1b74a0398"
}
```

## Task 2: Creating an auto scaling environment
In this section, I create a load balancer that pools a group of EC2 instances under a single Domain Name System (DNS) address. I use Auto Scaling to create a dynamically scalable pool of EC2 instances based on the image I created in the previous task. Finally, I create a set of alarms that scale out or scale in the number of instances in my load balancer group whenever the CPU performance of any machine within the group exceeds or falls below a set of specified thresholds.

### Task 2.1: Creating an Application Load Balancer
In this task, I create a load balancer that can balance traffic across multiple EC2 instances and Availability Zones.

1. I locate the **Load Balancing** section and choose **Load Balancers**.
2. I choose **Create load balancer**.
3. In the **Load balancer types** section, for **Application Load Balancer**, I choose **Create**.
4. In the **Basic configuration** section, I configure the following option:
   * **Load balancer name:** `WebServerELB`
5. In the **Network mapping** section, I configure the following options:
   * **VPC:** Choose `Lab VPC`
   * **Mappings:** Choose both Availability Zones listed
   * For the first Availability Zone, choose `Public Subnet 1`
   * For the second Availability Zone, choose `Public Subnet 2`
6. In the **Security groups** section, I choose the `X` for the default security group to remove it.
7. From the **Security groups** dropdown list, I choose `HTTPAccess`.
8. In the **Listeners and routing** section, I choose the **Create target group** link.

> [!NOTE]
> This link opens a new browser tab with the Create target group configuration options.

9. On the new **Create target group** page, in the **Settings - *immutable*** section, I configure the following and choose **Next**:
   * **Choose a target type:** `Instances`
   * **Target group name:** `webserver-app`
10. In the **Health checks** section, for **Health check path**, I enter `/index.php` and choose **Next**.
11. On the **Register targets** page, I choose **Next**. Once the target group is created successfully, I close the Target groups browser tab.
12. I return to the **Load balancers** browser tab. In the **Listeners and routing** section, I choose **Refresh** to the right of the **Forward to** dropdown list for **Default action**.
13. From the **Forward to** dropdown list, I choose `webserver-app`.
14. At the bottom of the page, I choose **Create load balancer**.

<p align="center">
  <img src="images/app-load-balance-create.png" alt="Creating an Application Load Balancer" width="1000">
</p>

*I receive a message similar to the following: "**Successfully created load balancer: WebServerELB**"*

15. To view the **WebServerELB** load balancer I created, I choose **View load balancer**.
16. I copy the DNS name of the load balancer, for later use in the lab:

```
WebServerELB-1545391657.us-west-2.elb.amazonaws.com
```

### Task 2.2: Creating a launch template
In this task, I create a launch template for my Auto Scaling group. A launch template is a template that an Auto Scaling group uses to launch EC2 instances. When creating a launch template, I specify information for the instances, such as the AMI, instance type, key pair, security group, and disks.

1. In the EC2 Management Console, I locate the **Instances** section and choose **Launch Templates**.
2. I choose **Create launch template**.
3. On the **Create launch template** page, in the **Launch template name and description** section, I configure the following options:
   * **Launch template name - required:** `web-app-launch-template`
   * **Template version description:** `A web server for the load test app`
   * **Auto Scaling guidance:** Choose `Provide guidance to help me set up a template that I can use with EC2 Auto Scaling`
4. In the **Application and OS Images (Amazon Machine Image) - required** section, I choose the **My AMIs** tab.
5. In the **Instance type** section, I choose `t3.micro`.
6. In the **Key pair (login)** section, I confirm that the **Key pair name** dropdown list is set to **Don't include in launch template**.

> [!NOTE]
> Amazon EC2 uses public key cryptography to encrypt and decrypt login information. To log in to an instance, I must create a key pair, specify the name of the key pair when launching the instance, and provide the private key when connecting to the instance.

7. In the **Network settings** section, I choose the **Security groups** dropdown list and choose `HTTPAccess`.
8. I choose **Create launch template**.

I receive a message similar to the following: "**Successfully created web-app-launch-template.**"

9. I choose **View launch templates**.

<p align="center">
  <img src="images/02-launch-template.png" alt="Launch Template Creation Success" width="1000">
</p>

*I have successfully created a launch template, for the Auto Scaling group, named `web-app-launch-template`.*

### Task 2.3: Creating an Auto Scaling group
In this task, I use my launch template to create an Auto Scaling group.

1. I choose **web-app-launch-template**, then from the **Actions** dropdown list, choose **Create Auto Scaling group**.
2. On the **Choose launch template or configuration** page, in the **Name** section, for **Auto Scaling group name**, I enter `Web App Auto Scaling Group`.
3. On the **Choose instance launch options** page, in the **Network** section, I configure the following options:
   * **VPC:** Choose `Lab VPC`
   * **Availability Zones and subnets:** Choose `Private Subnet 1 (10.0.2.0/24)` and `Private Subnet 2 (10.0.4.0/24)`
4. I choose **Next**.
5. On the **Configure advanced options – *optional*** page, I configure the following options:
   * In the **Load balancing** section, I choose `Attach to an existing load balancer`.
   * In the **Attach to an existing load balancer** section, I configure the following options:
     * Choose `Choose from your load balancer target groups`
     * From the **Existing load balancer target groups** dropdown list, choose `webserver-app | HTTP`
   * In the **Health checks** section, for **Additional health check type - optional**, I choose `Turn on Elastic Load Balancing health checks`.
6. I choose **Next**, and on the **Configure group size and scaling – optional** page, I configure the following options:
   * In the **Group size** and **Scaling** sections, I enter the following values:
     * **Desired capacity:** `2`
     * **Minimum desired capacity:** `2`
     * **Maximum desired capacity:** `4`
   * In the **Automatic scaling policies – optional** section, I configure the following options:
     * Choose `Target tracking scaling policy`
     * **Metric type:** Choose **Average CPU utilization**
     * I change the **Target value** to `50`

> [!NOTE]
> This change tells Auto Scaling to maintain an average CPU utilization across all instances of 50 percent. Auto Scaling automatically adds or removes capacity as required to keep the metric at or close to the specified target value. It adjusts to fluctuations in the metric due to a fluctuating load pattern.

7. On the **Add notifications – optional** page, I choose **Next**.
8. On the **Add tags – optional** page, I choose **Add tag** and configure the following options, then choose **Next**:
   * **Key:** `Name`
   * **Value - optional:** `WebApp`
9. I choose **Create Auto Scaling group**. These options launch EC2 instances in private subnets across both Availability Zones.

<p align="center">
  <img src="images/webapp-auto-scaling-group.png" alt="Auto Scaling Group Overview" width="1000">
</p>

*My Auto Scaling group initially shows an **Instances** count of zero, but new instances will be launched to reach the desired count of two instances.*

> [!CAUTION]
> If I experience an error related to the `t3.micro` instance type not being available, I rerun this task by choosing the `t2.micro` instance type instead.

## Task 3: Verifying the auto scaling configuration
In this task, I verify that both the Auto Scaling configuration and the load balancer are working by accessing a pre-installed script on one of my servers that consumes CPU cycles, invoking the scale-out alarm.

1. I choose **Instances**. Two new instances named `WebApp` are being created as part of my Auto Scaling group.

<p align="center">
  <img src="images/auto-scaling-instances.png" alt="WebApp instances created by Auto Scaling Group” width="900">
</p>

*While these instances are being created, the **Status check** for them is **Initializing**. I observe the **Status check** field for the instances until the status shows **2/2 checks passed**.*

2. Once the instances have completed *initialization*, in the **Load Balancing** section, I choose **Target Groups**, then select my target group, `webserver-app`.
3. On the **Targets** tab, I verify that two instances are being created, refreshing this list until the **Health status** of these instances changes to ***healthy***.

<p align="center">
  <img src="images/healthy-EC2-targets.png" alt="Auto Scaling group successfully launched two EC2 instances" width="900">
</p>

*A **healthy** status indicates that an instance has passed the load balancer's health check, meaning the load balancer will send traffic to the instance.*

## Task 4: Testing auto scaling configuration

1. I open a new web browser tab, paste the `DNS name` of the load balancer I copied earlier into the address bar, and press `Enter`.
2. On the web page, I choose **Start Stress**. 

>[!Note]
> This calls the application **stress** in the background, causing the CPU utilization on the instance that serviced this request to spike to 100 percent.

3. On the EC2 Management Console, in the **Auto Scaling** section, I choose **Auto Scaling Groups**.
4. I select **Web App Auto Scaling Group**.
5. I choose the **Activity** tab.

<p align="center">
  <img src="images/auto-scale-overview.png" alt="Web App Auto Scaling Group Overview” width="900">
</p>

*After a few minutes, I see my Auto Scaling group add a new instance. This occurs because Amazon CloudWatch detects that the average CPU utilization of my Auto Scaling group exceeded 50 percent, and my scale-up policy has been invoked in response.*

## Conclusion
After completing this lab, I am able to:

* Create an EC2 instance using an AWS CLI command
* Create a new AMI using the AWS CLI
* Create an Amazon EC2 launch template
* Create an Amazon EC2 Auto Scaling launch configuration
* Configure scaling policies and create an Auto Scaling group to scale in and scale out the number of servers based on variable load

## Additional resources
* [Amazon EC2 Auto Scaling Getting Started](https://aws.amazon.com/ec2/autoscaling/getting-started/)
* [Getting Started with Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/getting-started)
