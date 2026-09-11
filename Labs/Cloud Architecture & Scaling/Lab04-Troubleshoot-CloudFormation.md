# Troubleshoot CloudFormation

In this lab, I practice troubleshooting AWS CloudFormation deployments. I begin by querying JavaScript Object Notation (JSON)-formatted data using JMESPath, then move into my AWS account, where the environment provides an Amazon Elastic Compute Cloud (Amazon EC2) instance named CLI Host, running in a virtual private cloud (VPC) named VPC2. I establish a Secure Shell (SSH) connection to the CLI Host, and from there use the AWS Command Line Interface (AWS CLI) to run AWS CloudFormation commands that create a stack with resources in the AWS account — my first attempt to create the stack fails and requires troubleshooting.

I then manually modify a resource created by the AWS CloudFormation stack, outside of the context of CloudFormation, and use CloudFormation to detect the resulting drift. Finally, I attempt to delete the stack and encounter issues along the way. In the Challenge section, I must figure out how to successfully delete the stack while keeping the Amazon Simple Storage Service (Amazon S3) bucket that was originally created by the stack and now contains objects.

<p align="center">
  <img src="images/architecture-cf-deployment.png" alt="Troubleshooting AWS CloudFormation Deployment Architecture” width="900">
</p>

*The architectural diagram below illustrates the setup that is used in tasks this activity.*

## Business case relevance
*A new request from the Café leadership team:*

<p align="center">
  <img src="images/cafe-logo-cf.png" alt="Cafe Business Logo" width="400">
</p>

Sofîa is discussing the AWS deployment used by the Café with Olivia. Sofîa mentions that Martha and Frank would like both her and Nikhil to have the skills to build infrastructure as code (IaC). Olivia suggests that as a first attempt, Sofîa should try working on a proof of concept (POC).

In this activity, I take on the role of Sofîa. I create a deployment of a web server inside a custom VPC that I define, performing this deployment using an AWS CloudFormation template. I also learn how to troubleshoot deployments to gain an understanding of how effective this technology can be.

## Task 1: Practice querying JSON-formatted data using JMESPath
In this first task, I practice using the JMESPath JSON query language to return results from a JSON document.

1. I open a new browser window and go to [jmespath.org/](http://jmespath.org/).
2. On the JMESPath website, in the document window that currently displays the locations JSON document, I copy the following JSON document, replacing the ***locations*** document:

```json
{
  "desserts": [
    {
      "name": "Chocolate cake",
      "price": "20.00"
    },
    {
      "name": "Ice cream",
      "price": "15.00"
    },
    {
      "name": "Carrot cake",
      "price": "22.00"
    }
  ]
}
```

3. In the **Expression** search box above the document, I delete all the text and enter `desserts`. The expression is immediately evaluated.

> [!CAUTION]
> I do not press Enter after entering an expression in the search box. If I press Enter, the entire page reloads with its original data.

#### Result panel
```json
[
  {
    "name": "Chocolate cake",
    "price": "20.00"
  },
  {
    "name": "Ice cream",
    "price": "15.00"
  },
  {
    "name": "Carrot cake",
    "price": "22.00"
  }
]
```

In the **Result** panel below the document, I notice that all the content in the desserts part of the document is returned.

4. I add `[1]` to the expression:

#### Result panel
```json
{
  "name": "Ice cream",
  "price": "15.00"
}
```

Only the second dessert element is displayed. 

> [!NOTE]
> The `[]` notation is used with an index, enabling me to refer to a specific element of an array. Because JMESPath considers the first position in an array to be 0, `1` returns the second element.

5. To retrieve only the value of the `name` attribute for the chocolate cake element, I enter `desserts[0].name`:

#### Result panel
```json
"Chocolate cake"
```

The name of the first dessert element is returned. The `.` notation allows me to specify the name of an attribute in the document.

6. To retrieve the values of both the `name` and `price` attributes of the chocolate cake element, I enter `desserts[0].[name,price]`:

#### Result panel
```json
[
  "Chocolate cake",
  "20.00"
]
```

The name and price of the chocolate cake dessert are displayed. The `[]` notation can also be used to define a list of attributes to return.

7. To return the values of the `name` attribute for all three dessert elements, without the prices, I enter `desserts[].name`:

#### Result panel
```json
[
  "Chocolate cake",
  "Ice cream",
  "Carrot cake"
]
```

An empty array index `[]`, or one with an asterisk `[*]`, refers to all of the elements in an array.

8. Now, instead of referring to elements by their position, I use a filter to return the attributes of the carrot cake element by running `desserts[?name=='Carrot cake']`:

#### Result panel
```json
[
  {
    "name": "Carrot cake",
    "price": "22.00"
  }
]
```

9. Lastly, I replace the JSON document with the following document, which describes resources in an AWS CloudFormation stack:

```json
{
    "StackResources": [
        {
            "LogicalResourceId": "VPC",
            "ResourceType": "AWS::EC2::VPC"
        },
        {
            "LogicalResourceId": "PublicSubnet1",
            "ResourceType": "AWS::EC2::Subnet"
        },
        {
            "LogicalResourceId": "CliHostInstance",
            "ResourceType": "AWS::EC2::Instance"
        }
    ]
}
```

10. To determine the correct JMESPath expression to retrieve the `LogicalResourceId` of the EC2 instance resource, I run the following query:

```bash
StackResources[?ResourceType == 'AWS::EC2::Instance'].LogicalResourceId
```

<p align="center">
  <img src="images/JSMESPath-snapshot.png" alt="JSMESPath Webpage” width="900">
</p>

*I notice that the instructions often include AWS CLI commands with `--query` or `--filter` parameters. These parameters use JMESPath expressions to filter the output returned by an AWS CLI command.*

## Task 2: Troubleshooting and working with AWS CloudFormation stacks
This task starts with an EC2 instance named `CLI Host`, which is already created for me, running in the public subnet of a VPC named `VPC2`. I first establish an SSH connection to the CLI Host so that I can work with the AWS CloudFormation service from there.

### Task 2.1 for macOS/Linux: SSH to CLI Host Instance

In this task, I will connect to a Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP `35.95.44.63` From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance
```bash
kylescritten@MacBookAir ~ % cd ~/Downloads
kylescritten@MacBookAir Downloads % chmod 400 labsuser.pem
kylescritten@MacBookAir Downloads % ssh -i labsuser.pem ec2-user@35.95.44.63
The authenticity of host '35.95.44.63 (35.95.44.63)' can't be established.
ED25519 key fingerprint is: SHA256:4M6tSGr+zuC18ZC+BP8rqx0IllMLRnYTrZHLbkyVVmU
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

#### Terminal Output
```bash
Warning: Permanently added '35.95.44.63' (ED25519) to the list of known hosts.
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

[ec2-user@cli-host ~]$ 
```

### Task 2.2: Configure the AWS CLI
The AWS CLI is preconfigured on the Command Host instance.

1. To confirm that the Region in which the Command Host instance is running matches the lab's Region (`us-west-2`), I run the following command:
```bash
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
```

2. To update the AWS CLI software with the correct credentials, I run the following command:
```bash
aws configure
```

3. At the prompts, I enter the following information:
   * **AWS Access Key ID:** `<Lab Public Access Key>`
   * **AWS Secret Access Key:** `<Lab Secret Access Key>`
   * **Default region name:** Enter the Region name of where your EC2 instances are running.
   * **Default output format:** Enter `json`

#### Terminal Output
```bash
[ec2-user@cli-host ~]$ curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   477  100   477    0     0   136k      0 --:--:-- --:--:-- --:--:--  155k
  "region" : "us-west-2",
[ec2-user@cli-host ~]$ aws configure
AWS Access Key ID [None]: <Lab Public Access Key>
AWS Secret Access Key [None]: <Lab Secret Access Key>
Default region name [None]: us-west-2
Default output format [None]: json
[ec2-user@cli-host ~]$ 
```

### Task 2.3: Attempt to create an AWS CloudFormation stack
In this task, I try to create an AWS CloudFormation stack from a provided template using the AWS CLI. The template creates a VPC with a public subnet, an EC2 instance, a `WaitCondition` tied to the instance's userdata script, an S3 bucket, and a security group.

After creating the stack, I monitor resource creation and notice that partway through, resources begin being deleted instead of completing. Investigating with `describe-stack-events`, I find the `WaitCondition` timed out waiting for a signal from the EC2 instance's userdata script.

Since CloudFormation automatically rolls back and deletes all resources when one fails, `describe-stacks` confirms the stack status is `ROLLBACK_COMPLETE`. The stack object itself still exists, so I delete it with `aws cloudformation delete-stack --stack-name myStack`, which completes quickly since there are no resources left to roll back.

#### Terminal output
```bash
PLACEHOLDER
```

### Task 2.4: Avoid rollback on an AWS CloudFormation stack
I run the `create-stack` command again, giving the stack the same name, but this time specifying `--on-failure DO_NOTHING` to prevent a rollback if the stack fails. This gives me time to introspect the EC2 instance logs once the failure occurs, since resources won't be automatically deleted.

I run `describe-stack-resources` again and see that once the `WaitCondition` reaches `CREATE_FAILED`, the other resources retain their `CREATE_COMPLETE` status. `describe-stacks` confirms the overall stack status is `CREATE_FAILED`, but this time AWS CloudFormation does not roll back the stack. The `CREATE_FAILED` event details confirm it's the same `WaitCondition` timeout issue as before.

With the EC2 instance still available, I use SSH to connect to the Web Server instance created by the stack. From the CLI Host terminal, I run `describe-instances` to get the public IP address, then open a new terminal window and connect to the Web Server instance using that IP.

I check `cloud-init-output.log` and find "No package http available," along with a warning that the userdata script (`part-001`) failed to run. Since the script uses the `-e` flag to stop immediately on any command failure, the missing `http` package causes it to fail outright — meaning the wait condition never receives its success signal, and the stack creation ultimately times out and fails.

I then exit the SSH session by entering `exit` and close the terminal window.

#### Terminal output
```bash
PLACEHOLDER
```

### Task 2.5: Fix the issue and successfully create the AWS CloudFormation stack
Back in the terminal connected to the CLI Host instance, I update the AWS CloudFormation template by running `vim template1.yaml`. I navigate to line 128 in the UserData section of the EC2 resource, and change `"http"` to `"httpd"` — the actual name of the Apache web server package — then save and exit the file.

I confirm the update by running `cat template1.yaml | grep httpd`, which returns three matching lines. I then delete the failed stack with `aws cloudformation delete-stack --stack-name myStack`, and once `describe-stacks` confirms it's gone, I run `create-stack` again with the corrected template.

I run `describe-stack-resources` and wait until no resources remain in `CREATE_IN_PROGRESS`. Running `describe-stacks` this time confirms the stack was created successfully, with a `StackStatus` of `CREATE_COMPLETE`. I notice the **Outputs** section includes the public IP address of the web server and the name of the S3 bucket that was created:

```bash
PUBLIC_IP_ADDRESS
```

I test the web server by opening a browser tab and entering the IP address.

<p align="center">
  <img src="images/web-server-test.png" alt="Test the web server" width="900">
</p>

*A "Hello from your web server!" message displays. I have successfully discovered the root cause of the problem by examining log files on the EC2 instance, and resolved it to create the stack successfully.*


## Task 3: Make manual modifications and detect drift
In this task, I intentionally modify a resource that was created by AWS CloudFormation, but I modify the resource manually in the AWS Management Console.

When resources created by AWS CloudFormation need to be modified, it is a best practice to update the AWS CloudFormation template and then run the `update-stack` command. However, it is common for other AWS account users to be unaware of this best practice, or to forget how important it is to follow it. This task gives me hands-on practice noticing when these situations have occurred.

### Task 3.1: Make manual modifications to the security groups

1. I arrange the AWS Management Console tab so that it displays alongside these instructions, ideally with both browser tabs visible at the same time to make it easier to follow the lab steps.
2. I open the AWS Management Console in a new browser tab, and from the **Services** menu, choose **EC2**.
3. I click **Instances**, then select **Web Server**.
4. I click the **Security** tab, followed by the `WebServerSG` security group.
5. I click the **Inbound rules** tab, then click **Edit inbound rules**.
6. I modify the existing SSH inbound rule. To modify the rule, in the **Source** column of the row that applies to port 22, I click **Custom** and select **My IP**.
7. I click **Save rules**.

<p align="center">
  <img src="images/manual-sg-mods.png" alt="Make manual modifications to the security groups” width="900">
</p>

### Task 3.2: Add an object to the S3 bucket
From the terminal connected to the CLI Host, I query the bucket name, assign it to a variable named `bucketName`, and echo the result to the terminal by running the command provided in the lab. 

I then create an empty file, and copy it to the bucket using the `aws s3 cp` command, which references the `bucketName` variable I defined. Finally, I verify that the file is in the bucket by running `aws s3 ls $bucketName/`.

#### Terminal output
```bash
PLACEHOLDER
```

### Task 3.3: Detect drift
To start drift detection on my stack, I run the `detect-stack-drift` command, which returns a `StackDriftDetectionId`. I monitor the status of the drift detection by running a follow-up command using this ID, and notice that the output shows `"StackDriftStatus": "DRIFTED"`.

Finally, I describe the resources that drifted by running the `describe-stack-resource-drifts` command. Since the output from this command is extensive, I try a different approach, running a `describe-stack-resources` command with a query parameter that returns only the resource type, resource status, and drift status. 

>[!Note]
> The `PropertyDifferences` section of the output, which shows that port 22 is now open only to my IP address, instead of the `0.0.0.0/0` Classless Inter-Domain Routing (CIDR) block defined in the AWS CloudFormation template.

I then try updating the stack, and the output indicates that an error occurred — this is expected. The `update-stack` command does not automatically resolve drift, even though drift has occurred; I must manually resolve these issues to eliminate the drift.

#### Terminal output
```bash
PLACEHOLDER
```

## Task 4: Attempt to delete the stack
There might be occasions when I want to completely delete a stack, such as when I finish running tests in a test environment I no longer need, or when I want to save on costs by not maintaining environment resources I don't need for a while. In such situations, I know that if I need these resources again, I can re-create them using my proven template to create a new stack.

In this last task, I try to delete the stack. The attempt fails, and I am then given a challenge to resolve the issue.

1. I try deleting the stack by running the following command:

```bash
aws cloudformation delete-stack --stack-name myStack
```

2. I observe the results by running the `describe-stack-resources` command:

#### Terminal output
```bash
PLACEHOLDER
```

I observe how the status of each resource changes. Most of the resources are successfully deleted. However, one resource fails to delete: the S3 bucket.

Once all resources have a status of either `DELETE_COMPLETE` or `DELETE_FAILED`, I use the `Ctrl-C` keyboard combination to exit the watch command.

3. I run the `describe-stacks` command to see the stack status:

#### Terminal output
```bash
PLACEHOLDER
```

I notice that the `StackStatus` shows `DELETE_FAILED`.

> [!NOTE]
> The `StackStatusReason` reads: "The following resource(s) failed to delete: [MyBucket]." CloudFormation will not delete a bucket that has objects in it. This helps guard against accidental data loss.

## Challenge: Keep the file in the S3 bucket, but Still Delete the Stack
One approach to this issue would be to manually delete or move the file object in the S3 bucket and then run the `delete-stack` command again. However, this approach may not be appropriate if people in the organization have already started storing a large number of files in the bucket, and other systems now depend on the bucket name and location remaining unchanged.

My challenge is to:
* Figure out how to keep the bucket and the file in it, while still successfully deleting the stack so that the stack status becomes `DELETE_COMPLETE`
* Use the AWS CLI to solve the problem (avoiding the AWS Management Console)

#### Solution from Terminal output
```bash
PLACEHOLDER
```

## Business case solution
*Update from Café:*

<p align="center">
  <img src="images/cafe-logo-cf.png" alt="Cafe Business Logo" width="400">
</p>

When Sofîa went into work the next morning at the Café, she was excited to tell Nikhil and the others about the proof of concept work she had done the night before using CloudFormation.

She explained how this "Infrastructure as Code" approach to creating cloud deployments was causing her to completely rethink the café's current approach to managing the AWS resources that support the café website and other business applications.

Nikhil was very interested in what she was describing. They began discussing how they could use this technology to reliably create matching but separate development and production environments, and how useful that would be for new feature development. They also saw the value provided by powerful features such as drift detection and the ability to tear down and rebuild complex cloud infrastructures consisting of resources from multiple AWS services.

## Conclusion
After completing this activity, I am able to:
* **Practice** using JMESPath to query JSON-formatted documents
* **Troubleshoot** the deployment of an AWS CloudFormation stack using the AWS CLI
* **Analyze** log files on a Linux EC2 instance to determine the cause of a `create-stack` failure
* **Troubleshoot** a failed `delete-stack` action

## Additional resources
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/delete-stack.html)
