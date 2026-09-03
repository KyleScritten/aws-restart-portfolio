# Install and Configure the AWS CLI

## Lab overview
The AWS Command Line Interface (AWS CLI) is a command line tool that provides an interface for interacting with products and services from Amazon Web Services (AWS). I can install the AWS CLI on my local machine or a virtual machine such as an Amazon Elastic Compute Cloud (Amazon EC2) instance.

In this activity, I install and configure the AWS CLI on a Red Hat Linux instance, because this instance type does not have the AWS CLI pre-installed. Some instance types, such as Amazon Linux, do come pre-installed with the AWS CLI.

During this activity, I establish a Secure Shell (SSH) connection to the instance, then configure the installation with an access key that can connect to my AWS account. Finally, I practice using the AWS CLI to interact with AWS Identity and Access Management (IAM).

*When I finish the activity, it reflects the following diagram:*

<p align="center">
  <img src="images/aws-cli-architecture.png" alt="Install and Configure the AWS CLI" width="900">
</p>

*In the preceding diagram, I access the AWS Cloud through an SSH connection. Within the AWS Cloud, a virtual private cloud (VPC) with a Red Hat EC2 instance is configured with the AWS CLI. IAM is configured, and I use the AWS CLI to interact with IAM.*

## Task 1: Connect to the Red Hat EC2 instance using SSH
In this task, I will connect to a Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP `PLACEHOLDER_PUBLIC_IP`. From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance
```bash
kylescritten@Kyles-MacBook-Air ~ % cd ~/Downloads
kylescritten@Kyles-MacBook-Air Downloads % chmod 400 labsuser.pem
kylescritten@Kyles-MacBook-Air Downloads % ssh -i labsuser.pem ec2-user@52.42.122.142
The authenticity of host '52.42.122.142 (52.42.122.142)' can't be established.
ED25519 key fingerprint is: SHA256:iR8ngHw5JuO15w804j32BygrHWl2D3DPLbZ7yhCAoc8
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
#### Terminal Output
```text
Warning: Permanently added '52.42.122.142' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
   ,     #_
   ~\_  ####_        Amazon Linux 2
  ~~  \_#####\
  ~~     \###|       AL2 End of Life is 2026-06-30.
  ~~       \#/ ___
   ~~       V~' '->
    ~~~         /    A newer version of Amazon Linux is available!
      ~~._.   _/
         _/ _/       Amazon Linux 2023, GA and supported until 2028-03-15.
       _/m/'           https://aws.amazon.com/linux/amazon-linux-2023/

[ec2-user@ip-10-0-10-165 ~]$ 
```

## Task 2: Install the AWS CLI on a Red Hat Linux instance

#### Terminal output
```bash
PLACEHOLDER
```

## Task 3: Observe IAM configuration details in the AWS Management Console




## Task 4: Configure the AWS CLI to connect to my AWS Account

1. In the SSH session terminal window, I run the `aws configure` command for the AWS CLI.
2. At the prompt, I configure the following:
   * **AWS Access Key ID:** `<AWS Access Key ID>`
   * **AWS Secret Access Key:** `<AWS Secret Access Key>`
   * **Default region name:** Enter `us-west-2`
   * **Default output format:** Enter `json`

#### Terminal output
```bash
PLACEHOLDER
```

## Task 5: Observe IAM configuration details using the AWS CLI
In this task, I observe the IAM configuration details for the EC2 instance using the AWS CLI.

In the terminal window, I test the IAM configuration by running the `aws iam list-users` command:

#### Terminal output
```bash
PLACEHOLDER
```

A successful test shows a JSON response that includes a list of IAM users in the account.

## Activity 1 challenge
I successfully install the AWS CLI on a Red Hat Linux instance and connect it to my AWS account. I use the AWS CLI to retrieve policy information by referencing AWS documentation.

1. In the IAM AWS CLI Command Reference [documentation page](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html), the following command lists IAM policies and filters customer managed policies:

```bash
aws iam list-policies --scope Local
```

2. Next, I use the version number ARN information and `DefaultVersionId` found inside the `lab_policy` document to retrieve the JSON IAM policy, using the `>` command to save the file:

```bash
aws iam get-policy-version --policy-arn arn:aws:iam::038946776283:policy/lab_policy --version-id v1 > lab_policy.json
```

> [!NOTE]
> I can use the AWS CLI to manage and control multiple AWS services through the command line. I can also accomplish these tasks using the AWS Management Console.
>
> To connect to the same AWS account, the AWS CLI needs an access key ID and secret access key. To sign in to the AWS Management Console, I need a user name and password.

## Conclusion
After completing this lab, I am able to:

* Install and configure the AWS CLI
* Connect the AWS CLI to an AWS account
* Access IAM using the AWS CLI

## Additional resources
* [IAM AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html)
* [Installing or Updating the Latest Version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [Troubleshooting AWS CLI Errors](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-troubleshooting.html)
