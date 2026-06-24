# Linux Administration Lab – Managing Processes and Task Automation

## Lab Objectives
In this lab, I learned essential Linux system administration skills, including process monitoring and task automation by:
- Listing and filtering system processes
- Monitoring system performance using `top`
- Creating an automated task with `cron`

## Task 1: Use SSH to connect to an Amazon Linux EC2 instance

In this task, I will connect to a Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP 54.191.47.252 From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance

```bash
kylescritten@Kyles-MacBook-Air Downloads % cd ~/Downloads
kylescritten@Kyles-MacBook-Air Downloads % chmod 400 labsuser.pem
kylescritten@Kyles-MacBook-Air Downloads % ssh -i labsuser.pem ec2-user@54.191.47.252
The authenticity of host '54.191.47.252 (54.191.47.252)' can't be established.
ED25519 key fingerprint is: SHA256:YGJxLhe0ApdGzOPMCTZerpG+Bm5Ivd88CDZv8kVdejc
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
#### Terminal Output
```text
Warning: Permanently added '54.191.47.252' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-0-10-238 ~]$ 
```
