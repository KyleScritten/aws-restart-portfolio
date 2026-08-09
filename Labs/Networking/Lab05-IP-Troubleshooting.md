# Internet Protocol Troubleshooting Commands
In this lab, I will act as a new network administrator troubleshooting customer issues. I will explore troubleshooting techniques by following the OSI model, focusing specifically on Layers 3, 4, and 7, and I will correlate each layer with commonly used troubleshooting commands. Through practical examples and customer-based scenarios, I will apply these commands to identify and resolve networking issues. While this lab will not cover an exhaustive list of troubleshooting tools, I will use some of the most common and effective commands to diagnose typical networking problems.

## Task 1: Use SSH to connect to an Amazon Linux EC2 instance

In this task, I will connect to an Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP `44.248.10.201`. From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance
```bash
kylescritten@MacBookAir ~ % cd ~/Downloads
kylescritten@MacBookAir Downloads % chmod 400 labsuser.pem
kylescritten@MacBookAir Downloads % ssh -i labsuser.pem ec2-user@44.248.10.201
The authenticity of host '44.248.10.201 (44.248.10.201)' can't be established.
ED25519 key fingerprint is: SHA256:AIPFzwOLbeZzgshYW3vmeJ9n7vD8RegPBGcVrXc8ZAo
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
#### Terminal Output
```text
Warning: Permanently added '44.248.10.201' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-0-10-33 ~]$ 
```

## Task 2: Practice troubleshooting commands
Some layers have commands related to them to help with troubleshooting. The following is an example of how the troubleshooting commands flow with the Open Systems Interconnection (OSI) model:

<p align="center">
  <img src="images/OSI-troubleshooting.png" alt="How Troubleshooting Commands have Similarities to the OSI Model” width="900">
</p>

*Figure: This is an example of how troubleshooting commands have similarities to the OSI model.*

### Layer 3 (network): The ping and traceroute commands

#### 1. ping

The `ping` command is used to test connectivity between a local machine and a specified destination. It works by sending Internet Control Message Protocol (ICMP) echo request packets to a target host, such as `amazon.com` or `8.8.8.8`. The destination responds with echo reply packets, allowing measurement of the round-trip time (RTT).

This command is primarily used to verify whether a host is reachable and to troubleshoot network connectivity issues. By examining the responses, it is possible to assess latency and detect packet loss. Many implementations also allow continuous transmission of requests, which can be useful for ongoing monitoring of network stability.

The `ping` command accepts an IP address or URL along with optional parameters. The `-c` option specifies the number of echo requests to send.

*Example usage:*
```bash
[ec2-user@ip-10-0-10-33 ~]$ ping 8.8.8.8 -c 5
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=6.75 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=6.98 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=113 time=6.76 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=117 time=6.75 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=113 time=6.76 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 6.755/6.806/6.989/0.117 ms
[ec2-user@ip-10-0-10-33 ~]$ 
```

In this example, five ICMP echo requests are sent to `8.8.8.8`, a public DNS server operated by Google, to test connectivity and measure response times.

#### 2. traceroute

The `traceroute` command is used to analyze the path that packets take from a local machine to a destination, such as `8.8.8.8`. Each intermediate device along the route is referred to as a *hop*.

The output displays each hop in sequence, along with the latency for reaching that hop. This information helps identify where delays or disruptions occur along the network path.

Packet loss may appear at individual hops and is often associated with issues in the local area network (LAN) or the Internet Service Provider (ISP). If packet loss occurs closer to the final hops, it may indicate a problem near the destination server.

A failed hop is typically shown as three asterisks (`***`), indicating that no response was received within the timeout period. By comparing the hostnames and IP addresses before and after such failures, it is possible to locate potential points of failure or filtering.

*Example usage:*
```bash
[ec2-user@ip-10-0-10-33 ~]$ traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  ec2-44-233-117-81.us-west-2.compute.amazonaws.com (44.233.117.81)  7.262 ms ec2-44-233-117-85.us-west-2.compute.amazonaws.com (44.233.117.85)  4.167 ms ec2-44-233-117-105.us-west-2.compute.amazonaws.com (44.233.117.105)  7.413 ms
 2  240.0.68.6 (240.0.68.6)  0.265 ms 240.0.68.5 (240.0.68.5)  0.285 ms 240.0.68.4 (240.0.68.4)  0.232 ms
 3  242.1.47.97 (242.1.47.97)  0.339 ms 242.1.47.229 (242.1.47.229)  3.098 ms 242.1.46.229 (242.1.46.229)  3.098 ms
 4  240.4.12.36 (240.4.12.36)  8.031 ms 240.4.12.10 (240.4.12.10)  9.011 ms 240.4.12.38 (240.4.12.38)  8.078 ms
 5  242.11.43.3 (242.11.43.3)  8.721 ms 242.11.42.3 (242.11.42.3)  8.714 ms 242.11.42.135 (242.11.42.135)  8.899 ms
 6  240.1.228.34 (240.1.228.34)  7.559 ms 240.1.228.2 (240.1.228.2)  8.405 ms  7.833 ms
 7  99.83.116.81 (99.83.116.81)  7.509 ms * 99.82.10.7 (99.82.10.7)  6.882 ms
 8  * * *
 9  dns.google (8.8.8.8)  6.740 ms  6.809 ms  6.848 ms
[ec2-user@ip-10-0-10-33 ~]$ 
```

This command reveals the route taken to reach the destination and provides insight into network performance and potential issues along the path.

### Layer 4 (transport): The netstat and telnet commands

#### 3. netstat

The `netstat` command is used to display network connections, listening ports, and associated processes on a system. It is a useful tool for troubleshooting network issues and verifying whether specific ports are open or in use.

For example, during a routine security scan, a compromised port may be detected on a subnet. To investigate further, `netstat` can be run on a local host within that subnet to determine whether the port is actively listening when it should not be.

The command provides insight into active TCP connections and listening services, helping identify unexpected or unauthorized network activity. It is particularly valuable when diagnosing issues starting from the host machine and working outward through the network.

Common options include:

* `netstat -tp`: Displays established TCP connections along with the associated processes
* `netstat -tlp`: Shows services that are currently listening for incoming connections
* `netstat -ntlp`: Displays listening services without resolving port names (shows numeric ports only)

*Example usage:*
```bash
[ec2-user@ip-10-0-10-33 ~]$ netstat -tp
(No info could be read for "-p": geteuid()=1000 but you should be root.)
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0    296 ip-10-0-10-33.us-we:ssh 152-110-72-98.ftt:52954 ESTABLISHED -                   
[ec2-user@ip-10-0-10-33 ~]$ 
```

This command outputs currently established TCP connections, allowing verification of which remote hosts are connected and which processes are involved.

Overall, `netstat` provides a snapshot of Layer 4 (transport layer) connectivity. By revealing active connections and listening ports, it helps narrow down potential network or security issues efficiently.



## Conclusion
After completing this lab, I am able to:

* Practice troubleshooting commands
* Identify how I can use these commands in customer scenarios


## Additional resources
- [ping](https://docs.aws.amazon.com/vpn/latest/s2svpn/HowToTestEndToEnd_Linux.html)
- [telnet](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-windows-unable-connect-port/)
- [traceroute](https://aws.amazon.com/premiumsupport/knowledge-center/network-issue-vpc-onprem-ig/)
