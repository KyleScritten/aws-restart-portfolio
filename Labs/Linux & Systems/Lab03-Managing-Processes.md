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
## Task 2: Create List of Processes
In this task, I learned how to generate a log file of running processes while filtering out unwanted entries. I created a file named `processes.csv` that excluded processes owned by the `root` user and commands containing `[` or `]` .

The log file was stored in the `SharedFolders` directory.

1. Verify that I am in working directory `/home/ec2-user/companyA` by running the `pwd` command. I have not received the expected output and therefore needed to change directories.

```bash
[ec2-user@ip-10-0-10-238 ~]$ pwd
/home/ec2-user
[ec2-user@ip-10-0-10-238 ~]$ cd companyA
[ec2-user@ip-10-0-10-238 companyA]$ 
```
2. I ran the following command to list all processes, whilst excluding the `root` user
```bash
[ec2-user@ip-10-0-10-238 companyA]$ sudo ps -aux | grep -v root | sudo tee SharedFolders/processes.csv
```
This command allows me to display all running processes (`ps -aux`), filter out `root` processes (`grep -v root`) and finally save the output to a file while also viewing it (`tee`). The file was saved as `SharedFolders/processes.csv` .

3. To validate that the file correctly listed the processes and excluded the unwanted entries, I rand the command below
```bash
cat SharedFolders/processes.csv
```

#### Terminal Output
```bash
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
libstor+  1705  0.0  0.1  12628  1804 ?        Ss   22:55   0:00 /usr/bin/lsmd -d
rpc       1708  0.0  0.3  67356  3444 ?        Ss   22:55   0:00 /sbin/rpcbind -w
dbus      1719  0.0  0.4  58352  4040 ?        Ss   22:55   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
chrony    1727  0.0  0.3 120184  3048 ?        S    22:55   0:00 /usr/sbin/chronyd -F 2
rngd      1749  0.0  0.5  96464  4948 ?        Ss   22:55   0:00 /sbin/rngd -f --fill-watermark=0 --exclude=jitter
postfix   2159  0.0  0.6  90396  6548 ?        S    22:55   0:00 pickup -l -t unix -u
postfix   2160  0.0  0.7  90468  6824 ?        S    22:55   0:00 qmgr -l -t unix -u
ec2-user  2956  0.0  0.4 150748  4456 ?        S    23:00   0:00 sshd: ec2-user@pts/0
ec2-user  2957  0.0  0.4 124736  3956 pts/0    Ss   23:00   0:00 -bash
```

## Task 3: List the processes using the top command
In this exercise, I used the `top` command to display the processes and threads that were active on the system. I then observed and analyzed the output provided by the command.

1. In the main terminal I ran the command `top`
This command provided me with a live view of the system’s activity, allowing me to monitor the total number of processes, running and sleeping tasks, and overall CPU and memory usage. I was also able to observe the system’s swap usage in real time.

#### Terminal Output
```
top - 23:33:46 up 38 min,  1 user,  load average: 0.22, 0.07, 0.02
Tasks:  87 total,   1 running,  48 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.2 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :   962708 total,   265524 free,    91280 used,   605904 buff/cache
KiB Swap:        0 total,        0 free,        0 used.   721136 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                        
    1 root      20   0  189052   5420   3884 S   0.0  0.6   0:01.63 systemd                        
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd                       
    4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:0H                   
    5 root      20   0       0      0      0 I   0.0  0.0   0:00.04 kworker/u4:0                   
    6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_wq                   
    7 root      20   0       0      0      0 S   0.0  0.0   0:00.04 ksoftirqd/0                    
    8 root      20   0       0      0      0 I   0.0  0.0   0:00.09 rcu_sched                      
    9 root      20   0       0      0      0 I   0.0  0.0   0:00.00 rcu_bh                         
   10 root      rt   0       0      0      0 S   0.0  0.0   0:00.00 migration/0                    
   11 root      rt   0       0      0      0 S   0.0  0.0   0:00.00 watchdog/0                     
   12 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/0                        
   13 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/1                        
   14 root      rt   0       0      0      0 S   0.0  0.0   0:00.00 watchdog/1                     
   15 root      rt   0       0      0      0 S   0.0  0.0   0:00.20 migration/1                    
   16 root      20   0       0      0      0 S   0.0  0.0   0:00.05 ksoftirqd/1                    
   18 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/1:0H                   
   20 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kdevtmpfs                      
   21 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 netns                          
  202 root      20   0       0      0      0 S   0.0  0.0   0:00.00 khungtaskd                     
  203 root      20   0       0      0      0 S   0.0  0.0   0:00.00 oom_reaper 
```
3. I observed the task states displayed on the second line of the top command output to monitor the status of processes running on the system.

```
Tasks:  89 total,   1 running,  50 sleeping,   0 stopped,   0 zombie
```

To interpret the task states:

| State    | Meaning                                   |
| :------: | :---------------------------------------: |
| Running  | Processes currently executing             |
| Sleeping | Processes waiting for resources           |
| Stopped  | Suspended processes                       |
| Zombie   | Completed processes waiting to be removed |

4. I exited `top` by pressing `q`

## Task 4: Create a Cron Job
In this task, I learned how to automate a task using `cron`. I created a cron job that generates an audit file covering all `.csv` files. The output file was `SharedFolders/filteredAudit.csv`

1. I opened the Cron default text editor by running the following command
```bash
sudo crontab -e
```

2. Since the editor opened in `vi`, I entered insert mode by pressing `i`
3. The changes I made to configure the cron file were as follows:
```
SHELL=/bin/bash
PATH=/usr/bin:/bin:/usr/local/bin
MAILTO=root
0 * * * * ls -la $(find .) | sed -e 's/..csv/#####.csv/g' > /home/ec2-user/companyA/SharedFolders/filteredAudit.csv
```

4. To save and close the file, I pressed ESC. Then entered `:wq`
5. To validate that the file was configured and saved correctly I ran the command
```
sudo crontab -l
```

#### Terminal Output
```bash
[ec2-user@ip-10-0-10-238 companyA]$ sudo crontab -l
SHELL=/bin/bash 
PATH=/usr/bin:/bin:/usr/local/bin
MAILTO=root
0 * * * * ls -la $(find .) | sed -e 's/..csv/#####.csv/g' > /home/ec2-user/companyA/SharedFolders/filteredAudit.csv
```
