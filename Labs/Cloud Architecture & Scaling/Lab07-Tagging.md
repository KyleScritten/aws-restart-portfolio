# Managing Resources with Tagging

This lab is divided into two parts. In the **Task** portion, I use the AWS Command Line Interface (CLI) to inspect the tags assigned to a number of Amazon EC2 instances, then use pre-provided scripts to shut down and start up multiple Amazon EC2 instances simultaneously based on their tags. In the **Challenge** portion, I am challenged to think of a way to terminate instances that fail to implement specific tags.

The environment for this lab (pictured below) consists of:

* An Amazon VPC named Lab VPC
* A public subnet
* A private subnet
* An Amazon EC2 Linux instance named CommandHost (AWS Command Line Interface (CLI) tools have been pre-installed and configured on this instance)
* 8 Amazon EC2 Linux instances

The private instances have three custom tags applied to them:

| Tag Name | Content |
|---|---|
| Project | The project that the instance belongs to. The instances in this lab belong to one of two projects: **ERPSystem** and **Experiment1**. |
| Version | The version of the project that this instance belongs to. All Version tags are currently set to 1.0. |
| Environment | One of three values: **development**, **staging**, or **production**. |

In the Task portion of this lab, I log in to the Command Host and run commands to find and change the Version tag on all development instances. I run several examples that show how I can use the JMESPath syntax supported by the AWS CLI `--query` option to return richly formatted output. I then use a set of pre-provided scripts to stop and re-start all instances tagged as belonging to the development environment.

<p align="center">
  <img src="images/tagging-resources-diagram.png" alt="Resources with Tagging Architecture" width="900">
</p>

## Task 1: Using Tags to Manage Resources

In this task, I log in to the Command Host and use the AWS CLI to find a set of resources according to their tags. I then use the AWS CLI to change the value of one of the tags.

### Use SSH to connect to the Command Host instance

I connect to an Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 `Command Host` instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP `16.147.78.7`. From my terminal, I changed the permissions on the key to be read-only using my `PublicIP` allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance

```bash
kylescritten@MacBookAir ~ % cd ~/Downloads
kylescritten@MacBookAir Downloads % chmod 400 labsuser.pem
kylescritten@MacBookAir Downloads % ssh -i labsuser.pem ec2-user@16.147.78.7
The authenticity of host '16.147.78.7 (16.147.78.7)' can't be established.
ED25519 key fingerprint is: SHA256:bPT2SCMLcALbuswfS1gPvDyN2EOhc41AcNPBQmt8n0Q
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
#### Terminal Output
```text
Warning: Permanently added '16.147.78.7' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-5-0-100 ~]$ 
```

### Finding Development Instances For The Project

To find all instances in my account tagged with `Project=ERPSystem`, I run the following command in the Linux terminal window:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem"
```

I use the `--query` parameter to limit the output of the previous command to only the instance ID of the discovered instances:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].InstanceId'
```

#### Terminal output
```bash
[ec2-user@ip-10-5-0-100 ~]$ aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].InstanceId'
[
    [
        "i-05a85de6d9fb6285d"
    ], 
    [
        "i-0ec3a9e433529c861"
    ], 
    [
        "i-0615a40e7c96ad8ff"
    ], 
    [
        "i-060219fe71f1a628f"
    ], 
    [
        "i-0b0adc44474c18274"
    ], 
    [
        "i-0183d43308bebd837"
    ], 
    [
        "i-0278679e9a5745ca5"
    ]
]
```

I run the following command to include both the instance ID and the Availability Zone of each instance in my return result:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}'
```

To include the value of the Project tag in my output, I run the following command:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value}'
```

#### Terminal output
```bash
[ec2-user@ip-10-5-0-100 ~]$ aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value}'
[
    [
        {
            "Project": "ERPSystem", 
            "AZ": "us-west-2a", 
            "ID": "i-05a85de6d9fb6285d"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "AZ": "us-west-2a", 
            "ID": "i-0ec3a9e433529c861"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "AZ": "us-west-2a", 
            "ID": "i-0615a40e7c96ad8ff"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "AZ": "us-west-2a", 
            "ID": "i-060219fe71f1a628f"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "AZ": "us-west-2a", 
            "ID": "i-0b0adc44474c18274"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "AZ": "us-west-2a", 
            "ID": "i-0183d43308bebd837"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "AZ": "us-west-2a", 
            "ID": "i-0278679e9a5745ca5"
        }
    ]
]
```

I run the following command to also include the Environment and Version tags in my output:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```

#### Terminal output
```bash
[ec2-user@ip-10-5-0-100 ~]$ aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
[
    [
        {
            "Project": "ERPSystem", 
            "Environment": "production", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-05a85de6d9fb6285d"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "staging", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0ec3a9e433529c861"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "production", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0615a40e7c96ad8ff"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "development", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-060219fe71f1a628f"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "development", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0b0adc44474c18274"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "staging", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0183d43308bebd837"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "staging", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0278679e9a5745ca5"
        }
    ]
]

```

Finally, I add a second tag filter to see only the instances associated with the `ERPSystem` project that also belong to the `development` environment:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```

#### Terminal output
```bash
[ec2-user@ip-10-5-0-100 ~]$ aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
[
    [
        {
            "Project": "ERPSystem", 
            "Environment": "development", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-060219fe71f1a628f"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "development", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0b0adc44474c18274"
        }
    ]
]
```

*I should see only two instances returned by this command, both with a Project tag value of `ERPSystem` and an Environment tag value of `development`.*

### Changing Version Tag for Development Process

In this procedure, I change all of the Version tags on the instances marked as development for the ERPSystem project.

I could individually set these properties on each affected instance, but an automated approach is more practical. I use a simple Linux Bash shell script to build on the queries I ran earlier and modify tag entries as a batch operation.

On the CommandHost, I open the file `/home/ec2-user/change-resource-tags.sh`:
```bash
nano change-resource-tags.sh
```

<p align="center">
  <img src="images/change-resource-tags-file.png" alt="change-resource-tags.sh Bash Terminal Screenshot" width="900">
</p>

I close the nano editor and run this command from the Linux command prompt:
```bash
./change-resource-tags.sh
```

To verify that the version number on these instances has been incremented, and that other non-development instances in the ERPSystem project have been unaffected, I run the following command:
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId, AZ:Placement.AvailabilityZone, Project:Tags[?Key==`Project`] |[0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```

#### Terminal output
```bash
[ec2-user@ip-10-5-0-100 ~]$ aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId, AZ:Placement.AvailabilityZone, Project:Tags[?Key==`Project`] |[0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
[
    [
        {
            "Project": "ERPSystem", 
            "Environment": "production", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-05a85de6d9fb6285d"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "staging", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0ec3a9e433529c861"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "production", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0615a40e7c96ad8ff"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "development", 
            "AZ": "us-west-2a", 
            "Version": "1.1", 
            "ID": "i-060219fe71f1a628f"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "development", 
            "AZ": "us-west-2a", 
            "Version": "1.1", 
            "ID": "i-0b0adc44474c18274"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "staging", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0183d43308bebd837"
        }
    ], 
    [
        {
            "Project": "ERPSystem", 
            "Environment": "staging", 
            "AZ": "us-west-2a", 
            "Version": "1.0", 
            "ID": "i-0278679e9a5745ca5"
        }
    ]
]
```

## Task 2: Stop and Start Resources by Tag

In this task, I will use a pre-provided script to stop and start a set of instances tagged as `development` instances.  





## Conclusion

After completing this lab, I am able to:

* Apply tags to existing AWS resources
* Find resources based on tags
* Use the AWS CLI or AWS SDK for PHP to stop and terminate Amazon EC2 instances based on certain attributes of the resource

