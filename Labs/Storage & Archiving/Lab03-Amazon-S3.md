# Working with Amazon S3

In this lab, I will create and configure an Amazon Simple Storage Service (Amazon S3) bucket to share images with an external 
user at a media company (mediacouser) who has been hired to provide pictures of the products that the café sells. I will also 
configure the S3 bucket to automatically send an email notification to the administrator when the bucket contents are modified.

The following diagram shows the component architecture of the Amazon S3 file-sharing solution and illustrates its usage flow.

![Working with Amazon S3 Archtecture](./images/lab03-archtecture.png)

An AWS Identity and Access Management (IAM) user named mediacouser, which represents an external user at a media company, 
has been pre-created with the appropriate Amazon S3 permissions to allow the user to add, change, or delete images from the bucket. 
The necessary Amazon S3 permissions are reviewed for each user to make sure that access to the bucket is secure and appropriate for each role.  

The following steps describe the usage flow in the diagram:

1. When new product pictures are available or when existing pictures must be updated, a representative from the media company 
signs in to the AWS Management Console as **mediacouser** to upload, change, or delete the bucket contents.
2. As an alternative, **mediacouser** can use the AWS Command Line Interface (AWS CLI) to change the contents of the S3 bucket.
3. When Amazon S3 detects a change in the contents of the bucket, it publishes an email notification to the **s3NotificationTopic**
Amazon Simple Notification Service (Amazon SNS) topic.
4. The administrator who is subscribed to the **s3NotificationTopic** SNS topic receives an email message that contains the details 
of the changes to the contents of the bucket.

>[!Note]
> In real-world implementations, external users might not receive direct access to CLI Host as depicted in the diagram.

## Objectives
- Use the s3api and s3 AWS CLI commands to create and configure an S3 bucket.
- Verify write permissions to a user on an S3 bucket.
- Configure event notification on an S3 bucket.

## Task 1: Connecting to the CLI Host EC2 instance and configuring the AWS CLI
Here I connect to the CLI Host EC2 instance by using EC2 Instance Connect and configure the AWS CLI.
