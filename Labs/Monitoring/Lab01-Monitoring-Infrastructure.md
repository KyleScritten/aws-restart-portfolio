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

In the AWS Management Console, I select **Systems Manager** from the **Services** menu, then choose **Run Command** in the left navigation pane. I use Run Command to deploy a pre-written command that installs the CloudWatch agent, choosing **Run a Command** and selecting the button next to **AWS-ConfigureAWSPackage**. In the **Command parameters** section, I set **Action** to Install, **Name** to `AmazonCloudWatchAgent`, and **Version** to `latest`. In the **Targets** section, I select **Choose instances manually** and select the check box next to **Web Server**, installing the CloudWatch agent on the web server.

<p align="center">
  <img src="images/NAME.png" alt="AWS-ConfigureAWSPackage command configuration" width="900">
</p>

I choose **Run** and wait for the **Overall status** to change to **Success**, occasionally refreshing the page to check progress. To confirm the job ran successfully, I choose the instance under **Targets and outputs**, click **View output**, and expand **Step 1 - Output**, where I see the message "Successfully installed arn:aws:ssm:::package/AmazonCloudWatchAgent." Since the instance was created from a Linux AMI, if I instead see a precondition skip message referencing `createDownloadFolder`, I check **Step 2 - Output** instead — this is expected and can be safely ignored.

<p align="center">
  <img src="images/NAME.png" alt="Successful CloudWatch agent installation output" width="900">
</p>

I now configure the CloudWatch agent to collect the desired log information. Since the instance has a web server installed, I configure the agent to collect the web server logs and general system metrics, storing the configuration file in AWS Systems Manager Parameter Store so the CloudWatch agent can retrieve it. In the left navigation pane, I choose **Parameter Store**, then **Create parameter**, and set **Name** to `Monitor-Web-Server`, **Description** to `Collect web logs and system metrics`, and paste the following configuration as the **Value**:

```json
{
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "log_group_name": "HttpAccessLog",
            "file_path": "/var/log/httpd/access_log",
            "log_stream_name": "{instance_id}",
            "timestamp_format": "%b %d %H:%M:%S"
          },
          {
            "log_group_name": "HttpErrorLog",
            "file_path": "/var/log/httpd/error_log",
            "log_stream_name": "{instance_id}",
            "timestamp_format": "%b %d %H:%M:%S"
          }
        ]
      }
    }
  },
  "metrics": {
    "metrics_collected": {
      "cpu": {
        "measurement": [
          "cpu_usage_idle",
          "cpu_usage_iowait",
          "cpu_usage_user",
          "cpu_usage_system"
        ],
        "metrics_collection_interval": 10,
        "totalcpu": false
      },
      "disk": {
        "measurement": [
          "used_percent",
          "inodes_free"
        ],
        "metrics_collection_interval": 10,
        "resources": [
          "*"
        ]
      },
      "diskio": {
        "measurement": [
          "io_time"
        ],
        "metrics_collection_interval": 10,
        "resources": [
          "*"
        ]
      },
      "mem": {
        "measurement": [
          "mem_used_percent"
        ],
        "metrics_collection_interval": 10
      },
      "swap": {
        "measurement": [
          "swap_used_percent"
        ],
        "metrics_collection_interval": 10
      }
    }
  }
}
```

This configuration defines two web server log files to be collected and sent to CloudWatch Logs, along with CPU, disk, and memory metrics to be sent to CloudWatch Metrics. I choose **Create parameter**; this parameter is referenced when starting the CloudWatch agent.

<p align="center">
  <img src="images/NAME.png" alt="Parameter Store configuration for CloudWatch agent" width="900">
</p>

I now use another Run Command to start the CloudWatch agent on the web server. In the left navigation pane, I choose **Run Command**, then **Run command**, and filter by **Document name prefix : Equals : AmazonCloudWatch-ManageAgent**. Before running the command, I view its definition by choosing **AmazonCloudWatch-ManageAgent**, which opens a new tab showing the command's details. On the **Content** tab, I see the script that runs on the target instance, which references AWS Systems Manager Parameter Store to retrieve the CloudWatch agent configuration I defined earlier. I close this tab and return to the **Run a command** tab.

I select the button next to **AmazonCloudWatch-ManageAgent**, and in the **Command parameters** section, set **Action** to configure, **Mode** to ec2, **Optional Configuration Source** to ssm, **Optional Configuration Location** to `Monitor-Web-Server`, and **Optional Restart** to yes — configuring the agent to use the configuration I previously stored in Parameter Store. In the **Targets** section, I select **Choose instances manually**, select the check box next to **Web Server**, and choose **Run**.

<p align="center">
  <img src="images/NAME.png" alt="AmazonCloudWatch-ManageAgent command configuration" width="900">
</p>

I wait for the **Overall status** to change to **Success**, occasionally refreshing to check progress. The CloudWatch agent is now running on the instance and sending log and metric data to CloudWatch.




## Conclusion

After completing this lab, I am able to successfully:

* Use the AWS Systems Manager Run Command to install the CloudWatch agent on Amazon Elastic Compute Cloud (Amazon EC2) instances
* Monitor application logs using the CloudWatch agent and CloudWatch Logs
* Monitor system metrics using the CloudWatch agent and CloudWatch Metrics
* Create real-time notifications using CloudWatch Events
* Track infrastructure compliance using AWS Config
