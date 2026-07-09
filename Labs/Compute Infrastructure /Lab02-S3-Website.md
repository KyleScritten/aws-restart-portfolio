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

3. I login in with the new IAM user credentials:
- Account ID: ID of the account VocLabsUser from the AWS Management Console
- IAM user name: `awsS3user`
- Password: `Training123!`

>[!Note]
> The bucket that I created was not be visible. I refreshed the Amazon S3 console page to see if it appears. The awsS3user user does not have Amazon S3 access to the bucket that I created, so I have an error for Access to this bucket. The `awsS3user` needs to granted access using the SSH terminal.

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

4. To find the AWS managed policy that grants full access to Amazon S3 I ran the following command which outputs the policies available for Amazon S3.
```bash
[ec2-user@ip-10-200-0-23 ~]$ aws iam list-policies --query "Policies[?contains(PolicyName,'S3')]"
[
    {
        "PolicyName": "AmazonS3FullAccess",
        "PermissionsBoundaryUsageCount": 0,
        "CreateDate": "2015-02-06T18:40:58Z",
        "AttachmentCount": 0,
        "IsAttachable": true,
        "PolicyId": "ANPAIFIR6V6BVTRAHWINE",
        "DefaultVersionId": "v2",
        "Path": "/",
        "Arn": "arn:aws:iam::aws:policy/AmazonS3FullAccess",
        "UpdateDate": "2021-09-27T20:16:37Z"
    },
    {
        "PolicyName": "AmazonS3ReadOnlyAccess",
        "PermissionsBoundaryUsageCount": 0,
        "CreateDate": "2015-02-06T18:40:59Z",
        "AttachmentCount": 0,
        "IsAttachable": true,
        "PolicyId": "ANPAIZTJ4DXE7G6AGAE6M",
        "DefaultVersionId": "v3",
        "Path": "/",
        "Arn": "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
        "UpdateDate": "2023-08-10T21:31:39Z"
    },
…
```

5. I then grant the awsS3user user full access to the S3 bucket:
```
[ec2-user@ip-10-200-0-23 ~]$ aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name awsS3user
```

## Task 5: Adjust S3 bucket permissions
I changed the permission for the S3 bucket:
- Under Block public access (bucket settings), Block all public access: unchecked
- Under Object Ownership, ACLs enabled: selected
- Under Object Ownership, I acknowledge that ACLs will be restored: selected

<p align="center">
<img src="images/edit-block-access.png" alt="Block Public Access Disabled" width="700">
</p>
<p align="center">
<img src="images/acl-enabled.png" alt="Edit Object Ownership" width="700">
</p>

## Task 6: Extract the files that you need for this lab
1. A file containing the static-website contents for the Amazon S3 bucket is loaded and the following is output in the terminal:
```bash
[ec2-user@ip-10-200-0-23 ~]$ cd ~/sysops-activity-files
[ec2-user@ip-10-200-0-23 sysops-activity-files]$ tar xvzf static-website-v2.tar.gz
static-website/
static-website/css/
static-website/css/styles.css
static-website/images/
static-website/images/Cafe-Owners.png
static-website/images/Cake-Vitrine.png
static-website/images/Coffee-and-Pastries.png
static-website/images/Coffee-Shop.png
static-website/images/Cookies.png
static-website/images/Cup-of-Hot-Chocolate.png
static-website/images/Strawberry-&-Blueberry-Tarts.png
static-website/images/Strawberry-Tarts.png
static-website/index.html
```
2. To confirm that the files were extracted correctly, I ran the `ls` command. This show the files listed in the static website folder.
```bash
[ec2-user@ip-10-200-0-23 sysops-activity-files]$ cd static-website
[ec2-user@ip-10-200-0-23 static-website]$ ls
css  images  index.html
```

## Task 7: Upload files to Amazon S3 by using the AWS CLI
1. Once the files are extracted, I uploaded the contents of the file to Amazon S3 so that the bucket can function as a website:
```
[ec2-user@ip-10-200-0-23 static-website]$ aws s3 website s3://kscr080726/ --index-document index.html
```
2. I run the following command to upload the files to the bucket I created:
```
[ec2-user@ip-10-200-0-23 static-website]$ aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://kscr080726/ --recursive --acl public-read
upload: css/styles.css to s3://kscr080726/css/styles.css
upload: images/Coffee-Shop.png to s3://kscr080726/images/Coffee-Shop.png
upload: ./index.html to s3://kscr080726/index.html
upload: images/Cafe-Owners.png to s3://kscr080726/images/Cafe-Owners.png
upload: images/Strawberry-Tarts.png to s3://kscr080726/images/Strawberry-Tarts.png
upload: images/Cookies.png to s3://kscr080726/images/Cookies.png
upload: images/Coffee-and-Pastries.png to s3://kscr080726/images/Coffee-and-Pastries.png
upload: images/Cake-Vitrine.png to s3://kscr080726/images/Cake-Vitrine.png
upload: images/Cup-of-Hot-Chocolate.png to s3://kscr080726/images/Cup-of-Hot-Chocolate.png
upload: images/Strawberry-&-Blueberry-Tarts.png to s3://kscr080726/images/Strawberry-&-Blueberry-Tarts.png
```
3. To verify that the files were uploaded
```
[ec2-user@ip-10-200-0-23 static-website]$ aws s3 ls kscr080726
                           PRE css/
                           PRE images/
2026-07-08 02:37:38       2980 index.html
```
4. Bucket website endpoint URL : `http://kscr080726.s3-website-us-west-2.amazonaws.com` deploys the website in a new browser tab.
<p align="center">
<img src="images/s3-website.png" alt="Cafe Website Hosted" width="700">
</p>

## Task 8: Create a batch file to make updating the website repeatable
1. To pull up the history of recent commands, I ran the `history` command and received the following ouput from the console:
```bash
[ec2-user@ip-10-200-0-23 static-website]$ history
    1  pwd
    2  aws configure
    3  aws s3api create-bucket --bucket kscr080726 --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
    4  aws iam create-user --user-name awsS3user
    5  aws iam create-login-profile --user-name awsS3user --password Training123!
    6  aws iam list-policies --query "Policies[?contains(PolicyName,'S3')]"
    7  aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name awsS3user
    8  cd ~/sysops-activity-files
    9  tar xvzf static-website-v2.tar.gz
   10  cd static-website
   11  ls
   12  aws s3 website s3://kscr080726/ --index-document index.html
   13  aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://kscr080726/ --recursive --acl public-read
   14  aws s3 ls kscr080726
   15  history
```
2. To change directories and create an empty file, I ran:
```
[ec2-user@ip-10-200-0-23 static-website]$ cd ~
[ec2-user@ip-10-200-0-23 ~]$ touch update-website.sh
```
3. To open the empty file in the VI editor. I entered edit mode in the VI editor, and pressed `i` to make changes to the file.

4. To make the file an executable batch file, I ran:
```bash
[ec2-user@ip-10-200-0-23 ~]$ chmod +x update-website.sh
```
5. To open the local copy of the index.html file in a text editor, I ran:
```bash
[ec2-user@ip-10-200-0-23 ~]$ vi sysops-activity-files/static-website/index.html
```
<p align="center">
<img src="images/vi-editor.png" alt="The vi Editor" width="800">
</p>

6. To update the website, run your batch file.
```bash
[ec2-user@ip-10-200-0-23 ~]$ ./update-website.sh
upload: sysops-activity-files/static-website/css/styles.css to s3://kscr080726/css/styles.css
upload: sysops-activity-files/static-website/images/Coffee-Shop.png to s3://kscr080726/images/Coffee-Shop.png
upload: sysops-activity-files/static-website/index.html to s3://kscr080726/index.html
upload: sysops-activity-files/static-website/images/Cafe-Owners.png to s3://kscr080726/images/Cafe-Owners.png
upload: sysops-activity-files/static-website/images/Strawberry-Tarts.png to s3://kscr080726/images/Strawberry-Tarts.png
upload: sysops-activity-files/static-website/images/Cookies.png to s3://kscr080726/images/Cookies.png
upload: sysops-activity-files/static-website/images/Strawberry-&-Blueberry-Tarts.png to s3://kscr080726/images/Strawberry-&-Blueberry-Tarts.png
upload: sysops-activity-files/static-website/images/Coffee-and-Pastries.png to s3://kscr080726/images/Coffee-and-Pastries.png
upload: sysops-activity-files/static-website/images/Cake-Vitrine.png to s3://kscr080726/images/Cake-Vitrine.png
upload: sysops-activity-files/static-website/images/Cup-of-Hot-Chocolate.png to s3://kscr080726/images/Cup-of-Hot-Chocolate.png
```
Here is the updated static website:
<p align="center">
<img src="images/s3-website-new.png" alt="Updated Cafe Website Hosted With Colour Changes" width="700">
</p>

# Conclusion
I have now successfully done the following:
* Ran AWS CLI commands that use IAM and Amazon S3 services
* Deployed a static website to an S3 bucket
* Created a script that uses the AWS CLI to copy files in a local directory to Amazon S3
