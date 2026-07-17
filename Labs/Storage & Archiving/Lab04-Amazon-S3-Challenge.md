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
3. From the list of instances, I select the **CLI Host instance** and choose **Connect**.
4. On the **EC2 Instance Connect** tab, I choose **Connect**.

## Task 2: Configuring the AWS CLI

1. To set up the AWS CLI profile with credentials, I run the following command in the EC2 Instance Connect terminal:
```bash
aws configure
```
2. At the prompts, I copy the values predefined from the lab, and paste them into the terminal window as directed:
   * **AWS Access Key ID:** Enter the value for AccessKey.
   * **AWS Secret Access Key:** Enter the value for SecretKey.
   * **Default region name:** Enter `us-west-2`.
   * **Default output format:** Enter `json`.
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

[ec2-user@ip-10-200-0-140 ~]$ aws configure
AWS Access Key ID [None]: <AccessKey>
AWS Secret Access Key [None]: <SecretKey>
Default region name [None]: us-west-2
Default output format [None]: json
```
