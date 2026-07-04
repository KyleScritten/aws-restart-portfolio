# Working with Amazon EBS

Amazon Elastic Block Store (Amazon EBS) is a scalable, high-performance block-storage service that is designed for Amazon Elastic Compute Cloud (Amazon EC2). In this lab, I will create an EBS volume and perform operations on it, such as attaching it to an instance, creating a file system, and taking a snapshot backup.

<p align="center">
  <img src="images/amazon-EBS-architecture.png" alt="Amazon EBS Architecture Lab Scenario" width="800">
</p>

## Objectives
- Create an EBS volume.
- Attach and mount an EBS volume to an EC2 instance.
- Create a snapshot of an EBS volume.
- Create an EBS volume from a snapshot.

## Task 1: Creating a new EBS volume
An EC2 instance named **Lab** has already been launched for this lab in the **Availability Zone** `us-west-2a`.
In the left navigation pane, for **Elastic Block Store**, I choose **Volumes**. I see an existing (8 GiB) volume that the EC2 instance is using.
I click **Create Volune** to add a new volume to the instance. I use the following options:
- **Volume type**: `General Purpose SSD (gp2)`.
- **Size (GiB)**: `1`. 
- **Availability Zone**: `us-west-2a`
- **Tag - optional**:
    - **Key**: `Name`
    - **Value**: `My Volume`

<p align="center">
  <img src="images/ebs-create-volume.png" alt="Amazon EBS Volume creation" width="800">
</p>

I wait for the **Volume state** to became *Available*.

<p align="center">
  <img src="images/volume-state.png" alt="Amazon EBS Volume State View" width="800">
</p>

## Task 2: Attaching the volume to an EC2 instance
Now I attach my new volume to the EC2 instance. I use these options:
- **Instance**: `Lab`
- **Device name**: `/dev/sdb`

<p align="center">
  <img src="images/images/my-volume-attach.png" alt="Attaching an Amazon EC2 Instance" width="800">
</p>

I wait for the **Volume state** to became *In Use*.

<p align="center">
  <img src="images/images/volume-in-use.png" alt="Amazon EC2 Instance Volume State Change" width="800">
</p>
