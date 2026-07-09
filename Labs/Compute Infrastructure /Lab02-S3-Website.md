# Creating a Website on S3

## Lab Overview
In this lab I used the AWS Command Line Interface (AWS CLI) commands from an Amazon Elastic Compute Cloud (Amazon EC2) instance to:
- Create an Amazon Simple Storage Service (Amazon S3) bucket.
- Create a new AWS Identity and Access Management (IAM) user that has full access to the Amazon S3 service.
- Upload files to Amazon S3 to host a simple website for the Café & Bakery.
- Create a batch file that can be used to update the static website when you change any of the website files locally.

<p align="center">
<img src="images/s3-website-overview.png" alt="S3 Website Architecture Lab Scenario" width="800">
</p>

## Task 1: Connect to an Amazon Linux EC2 instance using SSM
Connect to my Amazon EC2 Instance using AWS Systems Manager Session Manager.
```bash
sh-4.2$ sudo su -l ec2-user
[ec2-user@ip-10-200-0-23 ~]$ pwd
/home/ec2-user
```

## Task 2: Configure the AWS CLI
In the SSH session terminal window, run the configure command to update the AWS CLI software with credentials.
```bash
[ec2-user@ip-10-200-0-23 ~]$ aws configure
AWS Access Key ID [None]: AKIAVIEVQ7PSBZC2Q6PJ
AWS Secret Access Key [None]: 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
Default region name [None]: us-west-2
Default output format [None]: json
```

## Task 3: Create an S3 bucket using the AWS CLI
The `s3api` command creates a new S3 bucket with the AWS credentials provided in this lab
1. I created a bucket in Amazon S3, I used the `aws s3api create-bucket` command. My bucket name: `kscr080726`
```bash
[ec2-user@ip-10-200-0-23 ~]$ aws s3api create-bucket --bucket kscr080726 --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
{
    "Location": "http://kscr080726.s3.amazonaws.com/"
}
```

## Task 4: Create a new IAM user that has full access to Amazon S3
1. The AWS CLI command: `aws iam create-user` creates a new IAM user for my AWS account.
```bash
[ec2-user@ip-10-200-0-23 ~]$ aws iam create-user --user-name awsS3user
{
    "User": {
        "UserName": "awsS3user",
        "Path": "/",
        "CreateDate": "2026-07-08T02:25:11Z",
        "UserId": "AIDAVIEVQ7PSHWPEDSKCR",
        "Arn": "arn:aws:iam::361090841572:user/awsS3user"
    }
}
```

2. Created a login profile for the new user by using the following command:
```bash
[ec2-user@ip-10-200-0-23 ~]$ aws iam create-login-profile --user-name awsS3user --password Training123!
{
    "LoginProfile": {
        "UserName": "awsS3user",
        "CreateDate": "2026-07-08T02:26:06Z",
        "PasswordResetRequired": false
    }
}
```
