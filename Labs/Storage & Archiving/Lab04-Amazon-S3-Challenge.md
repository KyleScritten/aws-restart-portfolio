# Challenge Lab: Amazon S3
In this challenge lab, I create an Amazon Simple Storage Service (Amazon S3) bucket and perform some routine tasks, such as uploading objects and configuring permissions to make those objects publicly accessible through a browser.

## Objectives
By the end of this challenge, I should be able to:
- Create an S3 bucket. 
- Upload an object into this bucket. 
- Access the object by using a web browser. 
- List the contents of the S3 bucket by using the AWS Command Line Interface (AWS CLI).

## Task 1: Connecting to the CLI Host instance

To start the challenge, I connect to the CLI Host instance that is already provisioned for me.

1. On the AWS Management Console, in the Search bar, I enter and choose `EC2` to open the EC2 Management Console.
2. In the navigation pane, I choose **Instances**.
3. From the list of instances, I select the CLI Host instance.
4. I choose **Connect**.
5. On the **EC2 Instance Connect** tab, I choose **Connect**.

## Task 2: Configuring the AWS CLI

1. To set up the AWS CLI profile with credentials, I run the following command in the EC2 Instance Connect terminal:
```bash
aws configure
```
2. At the prompts, I copy the values I pasted into my text editor, and paste them into the terminal window as directed:
   * **AWS Access Key ID:** Enter the value for AccessKey.
   * **AWS Secret Access Key:** Enter the value for SecretKey.
   * **Default region name:** Enter `us-west-2`.
   * **Default output format:** Enter `json`.
```bash

```
