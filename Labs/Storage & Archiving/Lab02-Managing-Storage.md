# Managing Storage

AWS provides multiple ways to manage data on Amazon Elastic Block Store (Amazon EBS) volumes. 
In this lab, I will use AWS Command Line Interface (AWS CLI) to create snapshots of an EBS volume 
and configure a scheduler to run Python scripts to delete older snapshots.

In the challenge section, I will sync the contents of a directory on an EBS volume to an Amazon Simple 
Storage Service (Amazon S3) bucket using an Amazon S3 sync command.

<p align="center">
  <img src="images/lab02-archtecture.png" alt="Managing Storage Archtecture Lab Scenario" width="1000">
</p>

This lab environment consists of a virtual private cloud (VPC) with a public subnet. Amazon Elastic Compute 
Cloud (Amazon EC2) instances named "Command Host" and "Processor" have already been created in this VPC.

The "Command Host" instance will be used to administer AWS resources including the "Processor" instance.

## Objectives
- Create and maintain snapshots for Amazon EC2 instances.
- Use Amazon S3 sync to copy files from an EBS volume to an S3 bucket.
- Use Amazon S3 versioning to retrieve deleted files.

## Task 1: Creating and configuring resources
I create an Amazon S3 bucket and configure the "Command Host" EC2 instance to have secure access to other AWS resources.

1. I create an S3 bucket named `s3-bucket-lab02-050726`.

<p align="center">
  <img src="images/lab02-s3-bucket.png" alt="Amazon S3 Bucket Creation" width="1000">
</p>

2. I attach a pre-created IAM role `S3BucketAccessRole` as an instance profile to the EC2 instance **Processor**, 
giving it the permissions to interact with other AWS services such as EBS volumes and S3 buckets.

<p align="center">
  <img src="images/EC2-IAM-user.png" alt="EC2 Processing with IAM role" width="1000">
</p>

## Task 2: Taking snapshots of your instance
Here I use the AWS Command Line Interface (AWS CLI) to manage the processing of snapshots of an instance.

1. I connect to the Command Host EC2 instance.
```bash

```

2. I shut down the "Processor" instance, which requires its instance ID using the following code.

```bash

```

Here is the output on screen.
```bash

```

3. I take an initial snapshot.
```bash

```

Here is the output on screen.
```bash

```

4. I schedule the creation of subsequent snapshots using the command `cron`.
```bash

```

Here is the output screen.
```bash

```

5. I stop the cron job with the command `crontab -r`.

6. I examine the contents of the Python script **snapshotter_v2.py** with the command `more /home/ec2-user/snapshotter_v2.py`.
```bash

```
The script finds all EBS volumes that are associated with the current user’s account and takes snapshots. 
It then examines the number of snapshots that are associated with the volume, sorts the snapshots by date, 
and removes all but the two most recent snapshots.

8. I show all the snapshot IDs associated to the volume.
```bash

```

9. I retain the last two snapshots.
```bash

```

10. I examine the new number of snapshots for the current volume.
```bash

```
The command returns only **2** snapshot IDs.

## Task 3: Challenge: Synchronize files with Amazon S3
Here I've been challenged to sync the contents of a directory with the Amazon S3 bucket that I created earlier.

1. Downloading and unzipping sample files
```bash

```

2. Syncing files
```bash

```

Here is the output on screen.
```bash

```

There's no direct command in Amazon S3 to restore a previous version of a file. 
So I download a previous version of the deleted file from Amazon S3, with the `aws s3api list-object-versions`.

```bash

```

The **Versions** block contains a list of all available versions. I save the value for VersionId.
```bash

```

Then I re-download the old version and sync again to Amazon S3.

```bash

```
Here is the output screen.
```bash

```

## Conclusion
In this lab I learnt how to:

- create and maintain snapshots for Amazon EC2 instances.
- use Amazon S3 sync to copy files from an EBS volume to an S3 bucket.
- use Amazon S3 versioning to retrieve deleted files.


