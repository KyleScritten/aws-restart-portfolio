# Creating Networking Resources in an Amazon Virtual Private Cloud (VPC)
My role is a Cloud Support Engineer at Amazon Web Services (AWS). During my shift, a customer from a startup company requests assistance regarding a networking issue within their AWS infrastructure. The email and an attachment of their architecture are below.

## Scenario
In this lab, I will investigate the customer's environment and analyze the customer's request to build a fully functional VPC. Through this experience, I will apply a blended approach of the OSI model and how AWS cloud fits into that model. I will create resources starting with a VPC, and work my way down the left-hand navigation pane to assist the customer in having their EC2 instance successfully achieve network connectivity.

**Email from the customer**

> Hello Cloud Support!
>
> I previously reached out to you regarding help setting up my VPC. I thought I knew how to attach all the resources to make an internet connection, but I cannot even ping outside the VPC. All I need to do is ping! Can you please help me set up my VPC to where it has network connectivity and can ping? The architecture is below. Thanks!
>
> Brock, startup owner

<p align="center">
  <img src="images/network-vpc-architecture.png" alt="VPC Networking Resources Architecture” width="900">
</p>

## Task 1: Investigate the customer's needs
In the scenario, Brock, the customer requesting assistance, has requested help creating resources for his VPC to be routable to the internet. I keep the VPC CIDR at `192.168.0.0/18` and the public subnet CIDR at `192.168.1.0/26`.

>[!Note]
> Protocols which can be directly used with AWS's Security Group (SG) and Network Access Control Lists (NACLs). A VPC needs an Internet Gateway (IGW) in order for the VPC to reach the internet, which has the route as 0.0.0.0/0. These routes go on what is called a Route Table, which are associated to subnets so they know where they belong. 

1. I create the VPC:
   - Name tag: `Test VPC`
   - IPv4 CIDR block: `192.168.0.0/18`
     
2. I create the subnet:
   - VPC ID: `Test VPC`
   - Subnet name: `Public subnet`
   - IPv4 subnet CIDR block: `192.168.1.0/28` (16 IPs)
     
3. I create the route table:
   - Name: `Public route table`
   - VPC: `Test VPC`
     
4. I create the Internet Gateway and attach it:
   - Name: `IGW test VPC`
   - Attach to VPC: `Test VPC`
     
5. I add a route to the *Public route table* and associate the subnet to the route table:
   - Destination: `0.0.0.0/0`
   - Target: `IGW test VPC` (Internet Gateway)
   - Associate to `Public subnet`
     
6. I create a Network ACL:
   - Name: `Public Subnet NACL`
   - VPC: `Test VPC`
   - Add new Inbound rule:
     - Rule number: `100`
     - Type: `All traffic`
   - Add new Outbound rule:
     - Rule number: `100`
     - Type: `All traffic`
       
7. I create a Security Group:
   - Security group name: `public security group`
   - Description: `allows public access`
   - VPC: `Test VPC`
   - Inbound rules:
     - `SSH` (port 22) from `0.0.0.0/0` (Anywhere-IPv4)
     - `HTTP` (port 80) from `0.0.0.0/0` (Anywhere-IPv4)
     - `HTTPS` (port 443) from `0.0.0.0/0` (Anywhere-IPv4)
   - Outbound rule:
     - `All traffic` from `0.0.0.0/0` (custom)

I now have a functional VPC. In the next task, I launch an EC2 instance to ensure that everything works.

## Task 2: Launch EC2 instance and SSH into instance
In this task, I launch an EC2 instance within my public subnet and test connectivity by running the `ping` command. This validates that my infrastructure — including security groups and network ACLs — is correctly configured and not blocking any traffic between the instance and the internet, and confirms that I have a route to the Internet Gateway via the route table, and that the Internet Gateway is attached.

1. On the AWS Management Console, in the search bar, I enter and choose `EC2` to go to the EC2 Management Console, then choose **Instances** in the left navigation pane.
2. I choose **Launch instances** and configure the following options:
   * In the **Name and tags** section, I leave the Name blank.
   * In the **Application and OS Images (Amazon Machine Image)** section, I configure the following options:
     * Quick Start: Choose **Amazon Linux**.
     * Amazon Machine Image (AMI): Choose **Amazon Linux 2023 AMI**.
   * In the **Instance type** section, I choose **t3.micro**.
   * In the **Key pair (login)** section, I choose **vockey**.
3. In the **Network settings** section, I choose **Edit** and configure the following options:
   * **VPC - required:** Choose **Test VPC**.
   * **Subnet:** Choose **Public Subnet**.
   * **Auto-assign public IP:** Choose **Enable**.
   * **Firewall (security groups):** Choose **Select existing security group**, then choose **public security group**.
4. I choose **Launch instance**.
5. To display the launched instance, I choose **View all instances**. The EC2 instance named **Bastion Server** is initially in a **Pending** state, then the instance state changes to **Running** to indicate that the instance has finished booting.

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP 52.42.122.142. From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the Bastion Server via SSH

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


## Task 3: Use ping to test internet connectivity
I test the connectivity with a ping to the google website:

```bash
[ec2-user@ip-192-168-1-4 ~]$ ping google.com
PING google.com (142.251.46.78) 56(84) bytes of data.
64 bytes from pnseab-ad-in-f14.1e100.net (142.251.46.78): icmp_seq=1 ttl=117 time=5.63 ms
64 bytes from pnseab-ad-in-f14.1e100.net (142.251.46.78): icmp_seq=2 ttl=117 time=5.68 ms
64 bytes from pnseab-ad-in-f14.1e100.net (142.251.46.78): icmp_seq=3 ttl=117 time=5.69 ms
64 bytes from pnseab-ad-in-f14.1e100.net (142.251.46.78): icmp_seq=4 ttl=117 time=5.65 ms
64 bytes from pnseab-ad-in-f14.1e100.net (142.251.46.78): icmp_seq=5 ttl=117 time=5.65 ms
64 bytes from pnseab-ad-in-f14.1e100.net (142.251.46.78): icmp_seq=6 ttl=117 time=5.69 ms
64 bytes from pnseab-ad-in-f14.1e100.net (142.251.46.78): icmp_seq=7 ttl=117 time=5.66 ms
^C
--- google.com ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6008ms
rtt min/avg/max/mdev = 5.629/5.664/5.694/0.022 ms
[ec2-user@ip-192-168-1-4 ~]$
```

The message on the terminal screen is saying I have replies from google.com and 0% packet loss.


## Conclusion
By completing this lab, I have successfully:

* Summarized the customer scenario
* Created a VPC, Internet Gateway, Route Table, Security Group, Network ACL, and EC2 instance to establish a routable network within the VPC
* Familiarized myself with the console
* Developed a solution to the customer's issue found within this lab

The lab is complete now that I have successfully used the `ping` command outside the VPC.

## Additional Resources
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [IP Addressing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
- [Route tables for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-rules)
- [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#VPCSecurityGroups)
