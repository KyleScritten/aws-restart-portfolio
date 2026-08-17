# Systems Hardening with Patch Manager via AWS Systems Manager

## Lab overview

In organizations with hundreds and often thousands of workstations, it can be logistically challenging to keep all the operating system (OS) and application software up to date. In most cases, OS updates on workstations can be automatically applied via the network. However, administrators must have a clear security policy and baseline plan to ensure that all workstations are running a certain minimum version of software.

In this lab, I use Patch Manager, a capability of AWS Systems Manager, to create a patch baseline. I then use the patch baseline I created to scan the Amazon Elastic Compute Cloud (Amazon EC2) instances for Windows that were pre-created for this lab. I also use the default patch baseline to patch EC2 Linux instances.

## Task 1: Patch Linux instances using default baselines
In this task, I patch Linux EC2 instances using default baselines available for the OS.

> [!NOTE]
> Patch Manager provides predefined patch baselines for each of the operating systems it supports. I can use custom patch baselines for greater control over which patches are approved or rejected for my environment.

1. In the AWS Management Console, I enter `Systems Manager` and select it.
2. In the Systems Manager console page, under **Node Management**, I choose **Fleet Manager**.

<p align="center">
  <img src="images/config-ec2-instances.png" alt="Pre-configured EC2 instances" width="900">
</p>

*Here are the pre-configured EC2 instances — three Linux instances and three Windows instances. These EC2 instances have a specific IAM role associated with them that allows me to manage them using Systems Manager.*

3. Under **Node Management**, I choose **Patch Manager**.
4. I choose **Start with an overview**.
5. I choose **Patch now** to patch the Linux instances with **AWS-AmazonLinux2DefaultPatchBaseline**.
6. Under **Basic configuration**, I configure as follows:
   * **Patching operation:** Scan and install
   * **Reboot option:** Reboot if needed
   * **Instances to patch:** Patch only the target instances I specify
   * **Target selection:** Specify instance tags
     * **Tag key:** `Patch Group`
     * **Tag value:** `LinuxProd`
   * I choose **Add**.
7. I choose **Patch now**.

A new page displays. In the **AWS-PatchNowAssociation** panel, a **Status** field shows that three instances will be affected, along with the progress made.

<p align="center">
  <img src="images/ops-summary-panel.png" alt="Patch Linux instances using default baselines" width="900">
</p>

*A Scan/Install operation summary panel also displays the status of the affected EC2 instances visually. I monitor this page until the patch operation on all three instances completes.*

## Conclusion
After completing this lab, I am able to:

* Patch Linux instances using default baseline
* Create a custom patch baseline
* Use patch groups to patch Windows instances using a custom patch baseline
* Verify patch compliance
