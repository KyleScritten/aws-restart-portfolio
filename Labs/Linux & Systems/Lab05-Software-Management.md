# Software Management

## Objectives

In this lab, I learnt how to:

- Update the Linux machine using the package manager
- Roll back or downgrade a previously updated package through the package manager
- Install the AWS Command Line Interface (AWS CLI)

## Task 1: Use SSH to connect to an Amazon Linux EC2 instance

In this task, I will connect to a Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP 35.165.155.183 From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance

```bash
kylescritten@Kyles-MacBook-Air ~ % cd ~/Downloads
kylescritten@Kyles-MacBook-Air Downloads % chmod 400 labsuser.pem
kylescritten@Kyles-MacBook-Air Downloads % ssh -i labsuser.pem ec2-user@35.165.155.183
The authenticity of host '35.165.155.183 (35.165.155.183)' can't be established.
ED25519 key fingerprint is: SHA256:fWpOX1gJ8RjphiEFsT590duiOy8aqQoBYpzBlgp3JUs
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
#### Terminal Output
```text
Warning: Permanently added '35.165.155.183' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-0-10-134 ~]$ 
```

## Task 2: Update your Linux machine
Here I used the yum package manager to update and upgrade my Linux machine, including relevant security packages.

1. I changed to the `companyA` directory and entered `sudo yum -y check-update` to query repositories for available updates.
```bash
[ec2-user@ip-10-0-10-134 ~]$ pwd
/home/ec2-user
[ec2-user@ip-10-0-10-134 ~]$ cd companyA
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum -y check-update
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
amzn2-core                                                                  | 3.6 kB  00:00:00 
```
2. I entered `sudo yum update --security` to apply security-related updates.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum update --security
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
No packages needed for security; 0 packages available
No packages marked for update
```
3. I entered `sudo yum -y upgrade` to update packages.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum -y upgrade
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
No packages marked for update
```
4. Eventually, I used the command `sudo yum install httpd -y` to view the install of httpd and view the history of updates.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum install httpd -y
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Resolving Dependencies
--> Running transaction check
---> Package httpd.x86_64 0:2.4.68-1.amzn2.0.1 will be installed
--> Processing Dependency: httpd-filesystem = 2.4.68-1.amzn2.0.1 for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: httpd-tools = 2.4.68-1.amzn2.0.1 for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: /etc/mime.types for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: httpd-filesystem for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: mod_http2 for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: system-logos-httpd for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: libapr-1.so.0()(64bit) for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: libaprutil-1.so.0()(64bit) for package: httpd-2.4.68-1.amzn2.0.1.x86_64
--> Running transaction check
---> Package apr.x86_64 0:1.7.2-1.amzn2.0.1 will be installed
---> Package apr-util.x86_64 0:1.6.3-1.amzn2.0.1 will be installed
--> Processing Dependency: apr-util-bdb(x86-64) = 1.6.3-1.amzn2.0.1 for package: apr-util-1.6.3-1.amzn2.0.1.x86_64
---> Package generic-logos-httpd.noarch 0:18.0.0-4.amzn2 will be installed
---> Package httpd-filesystem.noarch 0:2.4.68-1.amzn2.0.1 will be installed
---> Package httpd-tools.x86_64 0:2.4.68-1.amzn2.0.1 will be installed
--> Processing Dependency: libcrypto.so.1.1(OPENSSL_1_1_0)(64bit) for package: httpd-tools-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: libssl.so.1.1(OPENSSL_1_1_0)(64bit) for package: httpd-tools-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: libssl.so.1.1(OPENSSL_1_1_1)(64bit) for package: httpd-tools-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: libcrypto.so.1.1()(64bit) for package: httpd-tools-2.4.68-1.amzn2.0.1.x86_64
--> Processing Dependency: libssl.so.1.1()(64bit) for package: httpd-tools-2.4.68-1.amzn2.0.1.x86_64
---> Package mailcap.noarch 0:2.1.41-2.amzn2 will be installed
---> Package mod_http2.x86_64 0:2.0.42-1.amzn2.0.1 will be installed
--> Running transaction check
---> Package apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1 will be installed
---> Package openssl11-libs.x86_64 1:1.1.1zh-1.amzn2.0.1 will be installed
--> Processing Dependency: openssl11-pkcs11 for package: 1:openssl11-libs-1.1.1zh-1.amzn2.0.1.x86_64
--> Running transaction check
---> Package openssl11-pkcs11.x86_64 0:0.4.10-6.amzn2.0.1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================
 Package                     Arch           Version                       Repository          Size
===================================================================================================
Installing:
 httpd                       x86_64         2.4.68-1.amzn2.0.1            amzn2-core         1.4 M
Installing for dependencies:
 apr                         x86_64         1.7.2-1.amzn2.0.1             amzn2-core         130 k
 apr-util                    x86_64         1.6.3-1.amzn2.0.1             amzn2-core         101 k
 apr-util-bdb                x86_64         1.6.3-1.amzn2.0.1             amzn2-core          22 k
 generic-logos-httpd         noarch         18.0.0-4.amzn2                amzn2-core          19 k
 httpd-filesystem            noarch         2.4.68-1.amzn2.0.1            amzn2-core          26 k
 httpd-tools                 x86_64         2.4.68-1.amzn2.0.1            amzn2-core          90 k
 mailcap                     noarch         2.1.41-2.amzn2                amzn2-core          31 k
 mod_http2                   x86_64         2.0.42-1.amzn2.0.1            amzn2-core         173 k
 openssl11-libs              x86_64         1:1.1.1zh-1.amzn2.0.1         amzn2-core         1.4 M
 openssl11-pkcs11            x86_64         0.4.10-6.amzn2.0.1            amzn2-core          61 k

Transaction Summary
===================================================================================================
Install  1 Package (+10 Dependent packages)

Total download size: 3.5 M
Installed size: 9.1 M
Downloading packages:
(1/11): apr-1.7.2-1.amzn2.0.1.x86_64.rpm                                    | 130 kB  00:00:00     
(2/11): apr-util-1.6.3-1.amzn2.0.1.x86_64.rpm                               | 101 kB  00:00:00     
(3/11): apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64.rpm                           |  22 kB  00:00:00     
(4/11): generic-logos-httpd-18.0.0-4.amzn2.noarch.rpm                       |  19 kB  00:00:00     
(5/11): httpd-filesystem-2.4.68-1.amzn2.0.1.noarch.rpm                      |  26 kB  00:00:00     
(6/11): httpd-2.4.68-1.amzn2.0.1.x86_64.rpm                                 | 1.4 MB  00:00:00     
(7/11): httpd-tools-2.4.68-1.amzn2.0.1.x86_64.rpm                           |  90 kB  00:00:00     
(8/11): mailcap-2.1.41-2.amzn2.noarch.rpm                                   |  31 kB  00:00:00     
(9/11): mod_http2-2.0.42-1.amzn2.0.1.x86_64.rpm                             | 173 kB  00:00:00     
(10/11): openssl11-libs-1.1.1zh-1.amzn2.0.1.x86_64.rpm                      | 1.4 MB  00:00:00     
(11/11): openssl11-pkcs11-0.4.10-6.amzn2.0.1.x86_64.rpm                     |  61 kB  00:00:00     
---------------------------------------------------------------------------------------------------
Total                                                               13 MB/s | 3.5 MB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : apr-1.7.2-1.amzn2.0.1.x86_64                                                   1/11 
  Installing : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64                                          2/11 
  Installing : apr-util-1.6.3-1.amzn2.0.1.x86_64                                              3/11 
  Installing : 1:openssl11-libs-1.1.1zh-1.amzn2.0.1.x86_64                                    4/11 
  Installing : openssl11-pkcs11-0.4.10-6.amzn2.0.1.x86_64                                     5/11 
  Installing : httpd-tools-2.4.68-1.amzn2.0.1.x86_64                                          6/11 
  Installing : generic-logos-httpd-18.0.0-4.amzn2.noarch                                      7/11 
  Installing : mailcap-2.1.41-2.amzn2.noarch                                                  8/11 
  Installing : httpd-filesystem-2.4.68-1.amzn2.0.1.noarch                                     9/11 
  Installing : httpd-2.4.68-1.amzn2.0.1.x86_64                                               10/11 
  Installing : mod_http2-2.0.42-1.amzn2.0.1.x86_64                                           11/11 
  Verifying  : mod_http2-2.0.42-1.amzn2.0.1.x86_64                                            1/11 
  Verifying  : apr-1.7.2-1.amzn2.0.1.x86_64                                                   2/11 
  Verifying  : httpd-tools-2.4.68-1.amzn2.0.1.x86_64                                          3/11 
  Verifying  : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64                                          4/11 
  Verifying  : openssl11-pkcs11-0.4.10-6.amzn2.0.1.x86_64                                     5/11 
  Verifying  : 1:openssl11-libs-1.1.1zh-1.amzn2.0.1.x86_64                                    6/11 
  Verifying  : httpd-filesystem-2.4.68-1.amzn2.0.1.noarch                                     7/11 
  Verifying  : apr-util-1.6.3-1.amzn2.0.1.x86_64                                              8/11 
  Verifying  : mailcap-2.1.41-2.amzn2.noarch                                                  9/11 
  Verifying  : generic-logos-httpd-18.0.0-4.amzn2.noarch                                     10/11 
  Verifying  : httpd-2.4.68-1.amzn2.0.1.x86_64                                               11/11 

Installed:
  httpd.x86_64 0:2.4.68-1.amzn2.0.1                                                                

Dependency Installed:
  apr.x86_64 0:1.7.2-1.amzn2.0.1                   apr-util.x86_64 0:1.6.3-1.amzn2.0.1             
  apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1          generic-logos-httpd.noarch 0:18.0.0-4.amzn2     
  httpd-filesystem.noarch 0:2.4.68-1.amzn2.0.1     httpd-tools.x86_64 0:2.4.68-1.amzn2.0.1         
  mailcap.noarch 0:2.1.41-2.amzn2                  mod_http2.x86_64 0:2.0.42-1.amzn2.0.1           
  openssl11-libs.x86_64 1:1.1.1zh-1.amzn2.0.1      openssl11-pkcs11.x86_64 0:0.4.10-6.amzn2.0.1    

Complete!
```
## Task 3: Roll back a package
In this task I'll be downgrading a package that was updated through the yum package manager. To do this, I'll first check the yum history to see what has been installed and updated, then roll back to the most recent update in the history list.

1. In the folder **companyA**, I typed `sudo yum history list` to view the history of updates.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum history list
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
ID     | Command line             | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
     1 | install httpd -y         | 2026-06-27 20:02 | Install        |   11   
history list
```
>[!Note]
> The output is defferent than expected. It does not show the column for the **Login user** but the **Command Line**.
>To see the **Login User** column I added the option `history_list_view=users`.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum --setopt=history_list_view=users history list
Loaded plugins: extras_suggestions, langpacks, priorities, update-
              : motd
ID     | Login user               | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
     1 | EC2 ... <ec2-user>       | 2026-06-27 20:02 | Install        |   11   
history list
```
2. To view the most recent set of updates for the command `install httpd -y`, I entered `sudo yum history info 1`, where `1` is the ID of the command.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum history info 1
Loaded plugins: extras_suggestions, langpacks, priorities, update-
              : motd
Transaction ID : 1
Begin time     : Sat Jun 27 20:02:43 2026
Begin rpmdb    : 455:25c0c9dbbdce0a1b7df22a8c18b961715776281f
End time       :            20:02:44 2026 (1 seconds)
End rpmdb      : 466:a5ef2d24d06fbb673d90c197a3d8af4b225d5e70
User           : EC2 Default User <ec2-user>
Return-Code    : Success
Command Line   : install httpd -y
Transaction performed with:
    Installed     rpm-4.11.3-48.amzn2.0.5.x86_64 installed
    Installed     yum-3.4.3-158.amzn2.0.7.noarch installed
Packages Altered:
    Dep-Install apr-1.7.2-1.amzn2.0.1.x86_64                @amzn2-core
    Dep-Install apr-util-1.6.3-1.amzn2.0.1.x86_64           @amzn2-core
    Dep-Install apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64       @amzn2-core
    Dep-Install generic-logos-httpd-18.0.0-4.amzn2.noarch   @amzn2-core
    Install     httpd-2.4.68-1.amzn2.0.1.x86_64             @amzn2-core
    Dep-Install httpd-filesystem-2.4.68-1.amzn2.0.1.noarch  @amzn2-core
    Dep-Install httpd-tools-2.4.68-1.amzn2.0.1.x86_64       @amzn2-core
    Dep-Install mailcap-2.1.41-2.amzn2.noarch               @amzn2-core
    Dep-Install mod_http2-2.0.42-1.amzn2.0.1.x86_64         @amzn2-core
    Dep-Install openssl11-libs-1:1.1.1zh-1.amzn2.0.1.x86_64 @amzn2-core
    Dep-Install openssl11-pkcs11-0.4.10-6.amzn2.0.1.x86_64  @amzn2-core
history info
```
3. Entually, I rolled back to the most recent updates by typing `sudo yum -y history undo 1`.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo yum -y history undo 1
Loaded plugins: extras_suggestions, langpacks, priorities, update-
              : motd
Undoing transaction 1, from Sat Jun 27 20:02:43 2026
    Dep-Install apr-1.7.2-1.amzn2.0.1.x86_64                @amzn2-core
    Dep-Install apr-util-1.6.3-1.amzn2.0.1.x86_64           @amzn2-core
    Dep-Install apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64       @amzn2-core
    Dep-Install generic-logos-httpd-18.0.0-4.amzn2.noarch   @amzn2-core
    Install     httpd-2.4.68-1.amzn2.0.1.x86_64             @amzn2-core
    Dep-Install httpd-filesystem-2.4.68-1.amzn2.0.1.noarch  @amzn2-core
    Dep-Install httpd-tools-2.4.68-1.amzn2.0.1.x86_64       @amzn2-core
    Dep-Install mailcap-2.1.41-2.amzn2.noarch               @amzn2-core
    Dep-Install mod_http2-2.0.42-1.amzn2.0.1.x86_64         @amzn2-core
    Dep-Install openssl11-libs-1:1.1.1zh-1.amzn2.0.1.x86_64 @amzn2-core
    Dep-Install openssl11-pkcs11-0.4.10-6.amzn2.0.1.x86_64  @amzn2-core
Resolving Dependencies
--> Running transaction check
---> Package apr.x86_64 0:1.7.2-1.amzn2.0.1 will be erased
---> Package apr-util.x86_64 0:1.6.3-1.amzn2.0.1 will be erased
---> Package apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1 will be erased
---> Package generic-logos-httpd.noarch 0:18.0.0-4.amzn2 will be erased
---> Package httpd.x86_64 0:2.4.68-1.amzn2.0.1 will be erased
---> Package httpd-filesystem.noarch 0:2.4.68-1.amzn2.0.1 will be erased
---> Package httpd-tools.x86_64 0:2.4.68-1.amzn2.0.1 will be erased
---> Package mailcap.noarch 0:2.1.41-2.amzn2 will be erased
---> Package mod_http2.x86_64 0:2.0.42-1.amzn2.0.1 will be erased
---> Package openssl11-libs.x86_64 1:1.1.1zh-1.amzn2.0.1 will be erased
---> Package openssl11-pkcs11.x86_64 0:0.4.10-6.amzn2.0.1 will be erased
--> Finished Dependency Resolution
amzn2-core/2/x86_64                          | 3.6 kB     00:00     

Dependencies Resolved

====================================================================
 Package             Arch   Version               Repository   Size
====================================================================
Removing:
 apr                 x86_64 1.7.2-1.amzn2.0.1     @amzn2-core 275 k
 apr-util            x86_64 1.6.3-1.amzn2.0.1     @amzn2-core 206 k
 apr-util-bdb        x86_64 1.6.3-1.amzn2.0.1     @amzn2-core  11 k
 generic-logos-httpd noarch 18.0.0-4.amzn2        @amzn2-core  21 k
 httpd               x86_64 2.4.68-1.amzn2.0.1    @amzn2-core 4.2 M
 httpd-filesystem    noarch 2.4.68-1.amzn2.0.1    @amzn2-core 366  
 httpd-tools         x86_64 2.4.68-1.amzn2.0.1    @amzn2-core 173 k
 mailcap             noarch 2.1.41-2.amzn2        @amzn2-core  62 k
 mod_http2           x86_64 2.0.42-1.amzn2.0.1    @amzn2-core 457 k
 openssl11-libs      x86_64 1:1.1.1zh-1.amzn2.0.1 @amzn2-core 3.5 M
 openssl11-pkcs11    x86_64 0.4.10-6.amzn2.0.1    @amzn2-core 187 k

Transaction Summary
====================================================================
Remove  11 Packages

Installed size: 9.1 M
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : httpd-2.4.68-1.amzn2.0.1.x86_64                 1/11 
  Erasing    : mod_http2-2.0.42-1.amzn2.0.1.x86_64             2/11 
  Erasing    : mailcap-2.1.41-2.amzn2.noarch                   3/11 
  Erasing    : httpd-filesystem-2.4.68-1.amzn2.0.1.noarch      4/11 
  Erasing    : generic-logos-httpd-18.0.0-4.amzn2.noarch       5/11 
  Erasing    : httpd-tools-2.4.68-1.amzn2.0.1.x86_64           6/11 
  Erasing    : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64           7/11 
  Erasing    : apr-util-1.6.3-1.amzn2.0.1.x86_64               8/11 
  Erasing    : openssl11-pkcs11-0.4.10-6.amzn2.0.1.x86_64      9/11 
  Erasing    : 1:openssl11-libs-1.1.1zh-1.amzn2.0.1.x86_64    10/11 
  Erasing    : apr-1.7.2-1.amzn2.0.1.x86_64                   11/11 
  Verifying  : mod_http2-2.0.42-1.amzn2.0.1.x86_64             1/11 
  Verifying  : apr-1.7.2-1.amzn2.0.1.x86_64                    2/11 
  Verifying  : httpd-tools-2.4.68-1.amzn2.0.1.x86_64           3/11 
  Verifying  : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64           4/11 
  Verifying  : openssl11-pkcs11-0.4.10-6.amzn2.0.1.x86_64      5/11 
  Verifying  : 1:openssl11-libs-1.1.1zh-1.amzn2.0.1.x86_64     6/11 
  Verifying  : httpd-filesystem-2.4.68-1.amzn2.0.1.noarch      7/11 
  Verifying  : apr-util-1.6.3-1.amzn2.0.1.x86_64               8/11 
  Verifying  : mailcap-2.1.41-2.amzn2.noarch                   9/11 
  Verifying  : generic-logos-httpd-18.0.0-4.amzn2.noarch      10/11 
  Verifying  : httpd-2.4.68-1.amzn2.0.1.x86_64                11/11 

Removed:
  apr.x86_64 0:1.7.2-1.amzn2.0.1                                    
  apr-util.x86_64 0:1.6.3-1.amzn2.0.1                               
  apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1                           
  generic-logos-httpd.noarch 0:18.0.0-4.amzn2                       
  httpd.x86_64 0:2.4.68-1.amzn2.0.1                                 
  httpd-filesystem.noarch 0:2.4.68-1.amzn2.0.1                      
  httpd-tools.x86_64 0:2.4.68-1.amzn2.0.1                           
  mailcap.noarch 0:2.1.41-2.amzn2                                   
  mod_http2.x86_64 0:2.0.42-1.amzn2.0.1                             
  openssl11-libs.x86_64 1:1.1.1zh-1.amzn2.0.1                       
  openssl11-pkcs11.x86_64 0:0.4.10-6.amzn2.0.1                      

Complete!
```
## Task 4: Install the AWS CLI on Red Hat Linux
In this task, I'll be installing the AWS CLI on Amazon Elastic Compute Cloud (Amazon EC2) Linux. First, I'll make sure all packages are installed and up to date, then I'll go ahead and install the AWS CLI.

1. I verified that Python is installed.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ python3 --version
Python 3.7.16
```
I have Python 3 version 3.7.16, so I can continue with the AWS CLI installation.

2. To see if the pip package manager is already installed, I entered the following command:
```bash
[ec2-user@ip-10-0-10-134 companyA]$ pip3 --version
pip 20.2.2 from /usr/lib/python3.7/site-packages/pip (python 3.7)
```
>[!Note]
>The primary distribution method for the AWS CLI on Linux, Windows, and macOS is pip. pip is a package manager for Python that provides you with an easy way to install, upgrade, and remove Python packages and their dependencies.

3. In order to install the AWS CLI, download the installation file using the `curl` command.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 69.3M  100 69.3M    0     0   328M      0 --:--:-- --:--:-- --:--:--  330M
```
The `-o` option specifies the file name that the downloaded package is written to. In this case, the command write the downloaded file to the current directory with the local name `awscliv2.zip`.

4. I unzipped the installer.
The following command unzips the package and creates a directory named `aws` under the current directory
```bash
[ec2-user@ip-10-0-10-134 companyA]$ unzip awscliv2.zip
Archive:  awscliv2.zip
   creating: aws/
   creating: aws/dist/
  inflating: aws/README.md           
  inflating: aws/install
....
[ec2-user@ip-10-0-10-134 companyA]$ ll
total 70988
drwxr-xr-x 3 ec2-user ec2-user        78 Jun 23 01:29 aws
-rw-rw-r-- 1 ec2-user ec2-user  72686667 Jun 27 20:24 awscliv2.zip
drwxr-xr-x 2 ec2-user Personnel        6 Jun 27 19:40 CEO
drwxr-xr-x 2 ec2-user Personnel        6 Jun 27 19:40 Documents
drwxr-xr-x 2 ec2-user Personnel        6 Jun 27 19:40 Employees
-rw-r--r-- 1 ec2-user Personnel     2828 Jun 27 19:40 FolderListing.csv
drwxr-xr-x 6 ec2-user HR              72 Jun 27 19:40 HR
drwxr-xr-x 2 ec2-user Personnel        6 Jun 27 19:40 Management
-rw-r--r-- 1 ec2-user Personnel        0 Jun 27 19:40 Roster.csv
drwxr-xr-x 2 ec2-user Sales            6 Jun 27 19:40 Sales
drwxr-xr-x 2 ec2-user Personnel       94 Jun 27 19:40 SharedFolders
drwxr-xr-x 2 ec2-user Shipping         6 Jun 27 19:40 Shipping
```
5. I run the install program.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo ./aws/install
You can now run: /usr/local/bin/aws --version
```

>[!Note]
>The installation command uses a file named `install` in the newly unzipped `aws` directory. By default, the files are all installed to `/usr/local/aws-cli`, and a symbolic link is created in `/usr/local/bin`. The command includes `sudo` to grant write permissions to those directories.


6. To verify that the AWS CLI is now working, I typed `aws help`. The `help` command displayed the help information for the AWS CLI.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ aws help

AWS()                                                                    AWS()



NAME
       aws -

DESCRIPTION
       The  AWS  Command  Line  Interface is a unified tool to manage your AWS
       services.

SYNOPSIS
          aws [options] <command> <subcommand> [parameters]

       Use aws command help for information on a  specific  command.  Use  aws
       help  topics  to view a list of available help topics. The synopsis for
       each command shows its parameters and their usage. Optional  parameters
       are shown in square brackets.

GLOBAL OPTIONS
       --debug (boolean)

       Turn on debug logging.

       --endpoint-url (string)

       Override command's default URL with the given URL.

       --no-verify-ssl (boolean)
:
```
And then press `q` to exit.

## Task 5: Configure the AWS CLI to connect to my AWS account
1. I configured the **AWS CLI** with these options.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ aws configure

Tip: You can deliver temporary credentials to the AWS CLI using your AWS Console session by running the command 'aws login'.

AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: us-west-2
Default output format [None]: json
```
2. In the file `~/.aws/credentials` I copied the `aws_access_key_id` and `aws_secret_access_key` for my lab. It followed this general structure:
```
[default]
aws_access_key_id=<your access key id>
aws_secret_access_key=<your secret access key>
aws_session_token=<your session token>
```
3. To edit the file I used the `nano` editor with `sudo`, `crl+o` and `enter` to save the file, `crl+x` to exit the editor.
```bash
[ec2-user@ip-10-0-10-134 companyA]$ sudo nano ~/.aws/credentials
```
4. From the **AWS Management Console** I copied the istance ID `i-075f930b0caacf43d` of the **Command Host** istance
5. Then on the terminal, I used the command `aws ec2` with the option to retrive the `istanceType` from the given `istance ID i-075f930b0caacf43d`
```bash
[ec2-user@ip-10-0-10-134 companyA]$ aws ec2 describe-instance-attribute --instance-id i-075f930b0caacf43d --attribute instanceType
{
    "InstanceId": "i-075f930b0caacf43d",
    "InstanceType": {
        "Value": "t3.micro"
    }
}
```
