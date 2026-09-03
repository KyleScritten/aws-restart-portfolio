# Install and Configure the AWS CLI

## Lab overview
The AWS Command Line Interface (AWS CLI) is a command line tool that provides an interface for interacting with products and services from Amazon Web Services (AWS). I can install the AWS CLI on my local machine or a virtual machine such as an Amazon Elastic Compute Cloud (Amazon EC2) instance.

In this activity, I install and configure the AWS CLI on a Red Hat Linux instance, because this instance type does not have the AWS CLI pre-installed. Some instance types, such as Amazon Linux, do come pre-installed with the AWS CLI.

During this activity, I establish a Secure Shell (SSH) connection to the instance, then configure the installation with an access key that can connect to my AWS account. Finally, I practice using the AWS CLI to interact with AWS Identity and Access Management (IAM).

*When I finish the activity, it reflects the following diagram:*

<p align="center">
  <img src="images/aws-cli-architecture.png" alt="Install and Configure the AWS CLI" width="1000">
</p>

*In the preceding diagram, I access the AWS Cloud through an SSH connection. Within the AWS Cloud, a virtual private cloud (VPC) with a Red Hat EC2 instance is configured with the AWS CLI. IAM is configured, and I use the AWS CLI to interact with IAM.*

## Task 1: Connect to the Red Hat EC2 instance using SSH
In this task, I will connect to a Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP `34.221.15.194`. From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance
```bash
kylescritten@MacBookAir ~ % cd ~/Downloads
kylescritten@MacBookAir Downloads % chmod 400 labsuser.pem
kylescritten@MacBookAir Downloads % ssh -i labsuser.pem ec2-user@34.221.15.194
The authenticity of host '34.221.15.194 (34.221.15.194)' can't be established.
ED25519 key fingerprint is: SHA256:NwytUe++pSWRP0dfUhKxdWHswWzfGkPBQBhReOP1yGk
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
#### Terminal Output
```text
Warning: Permanently added '34.221.15.194' (ED25519) to the list of known hosts.
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
         _/ _/       Amazon Linux 2023, GA and supported until 2029-06-30.
       _/m/'           https://aws.amazon.com/linux/amazon-linux-2023/

[ec2-user@ip-10-200-0-42 ~]$ 
```

## Task 2: Install the AWS CLI on a Red Hat Linux instance
In this task, I follow these steps from the terminal window to install the AWS CLI on a Red Hat Linux instance.

I write the downloaded file to the current directory by running the `curl` command with the `-o` option, then unzip the installer by running the `unzip` command with the `-u` option to skip any prompts to overwrite existing files. 

I then run the install program using `sudo`, which grants write permissions to the directory and uses a file named `install` in the unzipped `aws` directory to install the AWS CLI. Finally, I confirm the installation by running the `aws --version` command.

#### CLI commands run
```bash
# Write the downloaded file to the current directory, option -o rename the file
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Unzip the installer, option -u option to skip prompts asking you to overwrite any existing files
unzip -u awscliv2.zip

# Run the install program - The sudo command grants write permissions to the directory
sudo ./aws/install

# Confirm the installation
aws --version
```

#### Terminal output
```bash
[ec2-user@ip-10-200-0-42 ~]$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 69.9M  100 69.9M    0     0   264M      0 --:--:-- --:--:-- --:--:--  265M
[ec2-user@ip-10-200-0-42 ~]$ unzip -u awscliv2.zip
Archive:  awscliv2.zip
   creating: aws/
   creating: aws/dist/
...
  inflating: aws/dist/prompt_toolkit-3.0.51.dist-info/licenses/LICENSE  
  inflating: aws/dist/prompt_toolkit-3.0.51.dist-info/licenses/AUTHORS.rst  
[ec2-user@ip-10-200-0-42 ~]$ sudo ./aws/install
You can now run: /usr/local/bin/aws --version
[ec2-user@ip-10-200-0-42 ~]$ aws --version
aws-cli/2.36.39 Python/3.14.6 Linux/4.14.355-284.742.amzn2.x86_64 exe/x86_64.amzn.2
[ec2-user@ip-10-200-0-42 ~]$ 
```

*To verify that the AWS CLI is now working, I run the `aws help` command. The help command displays the information for the AWS CLI.*

## Task 3: Observe IAM configuration details in the AWS Management Console
In this task, I observe the IAM configuration details for the EC2 instance in the AWS Management Console.

> [!NOTE]
> The IAM page that appears contains messages indicating that I do not have permission to observe some IAM service details. I can safely ignore these messages.

1. In the AWS IAM Console, I choose **Users**, then choose `awsstudent`.
2. I am now in the **Permissions** tab. Next to `lab_policy`, I choose the arrow icon, then choose the **{} JSON** button. 

<p align="center">
  <img src="images/observe-lab-policy.png" alt="Observe IAM configuration details and User Lab Policy” width="900">
</p>

*This `lab_policy` document is formatted in JSON, and the IAM policy grants the `awsstudent` user access to specific AWS services in this account.*

3. I choose the **Security credentials** tab. In the **Access keys** section, I locate the `awsstudent` user's access key ID.

<p align="center">
  <img src="images/awsstudent-security-credentials.png" alt="IAM User Security Credentials” width="900">
</p>

## Task 4: Configure the AWS CLI to connect to my AWS Account

1. In the SSH session terminal window, I run the `aws configure` command for the AWS CLI.
2. At the prompt, I configure the following:
   * **AWS Access Key ID:** `<AWS Access Key ID>`
   * **AWS Secret Access Key:** `<AWS Secret Access Key>`
   * **Default region name:** Enter `us-west-2`
   * **Default output format:** Enter `json`

#### Terminal output
```bash
[ec2-user@ip-10-200-0-42 ~]$ aws configure

Tip: You can deliver temporary credentials to the AWS CLI using your AWS Console session by running the command 'aws login'.

AWS Access Key ID [None]: AKIARNRMGMBMOAACX3TI
AWS Secret Access Key [None]: peyP6AzViJDBpIreZnZbPrum65WMOma7GkusKRu7
Default region name [None]: us-west-2
Default output format [None]: json
[ec2-user@ip-10-200-0-42 ~]$ 
```

## Task 5: Observe IAM configuration details using the AWS CLI
In this task, I observe the IAM configuration details for the EC2 instance using the AWS CLI.

In the terminal window, I test the IAM configuration by running the `aws iam list-users` command:

#### Terminal output
```bash
[ec2-user@ip-10-200-0-42 ~]$ aws iam list-users
{
    "Users": [
        {
            "Path": "/",
            "UserName": "awsstudent",
            "UserId": "AIDARNRMGMBMAKPWOL5OM",
            "Arn": "arn:aws:iam::097803198552:user/awsstudent",
            "CreateDate": "2026-09-03T20:21:41+00:00"
        }
    ]
}
[ec2-user@ip-10-200-0-42 ~]$ 
```

*A successful test shows a JSON response that includes a list of IAM users in the account.*

## Activity 1 challenge
I successfully install the AWS CLI on a Red Hat Linux instance and connect it to my AWS account. I use the AWS CLI to retrieve policy information by referencing AWS documentation.

1. In the [IAM AWS CLI Command Reference documentation page](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html), the following command lists IAM policies and filters customer managed policies:

```bash
[ec2-user@ip-10-200-0-42 ~]$ aws iam list-policies --scope Local
{
    "Policies": [
        {
            "PolicyName": "lab_policy",
            "PolicyId": "ANPARNRMGMBMDAXO5XJA3",
            "Arn": "arn:aws:iam::097803198552:policy/lab_policy",
            "Path": "/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 1,
            "PermissionsBoundaryUsageCount": 0,
            "IsAttachable": true,
            "CreateDate": "2026-09-03T20:22:19+00:00",
            "UpdateDate": "2026-09-03T20:22:19+00:00"
        }
    ]
}
[ec2-user@ip-10-200-0-42 ~]$ 
```

2. Next, I use the version number ARN information and `DefaultVersionId` found inside the `lab_policy` document to retrieve the JSON IAM policy, using the `>` command to save the file:

```bash
[ec2-user@ip-10-200-0-42 ~]$ aws iam get-policy-version --policy-arn arn:aws:iam::097803198552:policy/lab_policy --version-id v1 > lab_policy.json
[ec2-user@ip-10-200-0-42 ~]$ ls -ltr
total 71684
drwxr-xr-x 3 ec2-user ec2-user       78 Sep  3 18:14 aws
-rw-rw-r-- 1 ec2-user ec2-user 73395047 Sep  3 20:28 awscliv2.zip
-rw-rw-r-- 1 ec2-user ec2-user     5035 Sep  3 20:45 lab_policy.json
[ec2-user@ip-10-200-0-42 ~]$ head -n 10 lab_policy.json
{
    "PolicyVersion": {
        "Document": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": [
                        "cloudformation:List*",
                        "cloudformation:Describe*",
                        "cloudformation:Detect*",
[ec2-user@ip-10-200-0-42 ~]$ 
```

*`ls -ltr` lists all files in the current directory sorted by modification time (oldest first, newest last), with `-l` giving a detailed long-format listing (permissions, owner, size, date) and `-r` reversing the default sort order — here it shows an `aws` directory, the `awscliv2.zip` installer, and a `lab_policy.json` file you saved earlier. `head -n 10 lab_policy.json` then prints just the first 10 lines of that JSON file, letting you preview its contents without dumping the entire file to the terminal.*

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
