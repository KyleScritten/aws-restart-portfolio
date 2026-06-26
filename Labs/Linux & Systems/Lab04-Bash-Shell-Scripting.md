# Challenge Lab: Bash Shell Scripting Exercise

## Assignment

Write a Bash script based on the following requirements:
- Creates 25 empty (0 KB) files. (Hint: Use the **touch** command.)
- The file names should be **<yourName><number>, <yourName><number+1>, <yourName><number+2>**, and so on.
- Design the script so that each time you run it, it creates the next batch of 25 files with increasing numbers starting with the last or maximum number that already exists.
- Do not hard code these numbers. You need to generate them by using automation.
- Test the script. Display a long list of the directory and its contents to validate that the script created the expected files.

## Task 1: Use SSH to connect to an Amazon Linux EC2 instance

In this task, I will connect to a Amazon Linux EC2 instance. I run macOS and will use an SSH utility to perform all of these operations. The Amazon EC2 instance is configured as part of this lab environment. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP 35.86.247.199 From my terminal, I changed the permissions on the key to be read-only using my PublicIP allowing the first connection to this remote SSH server. 

#### Connect to the EC2 Instance

```bash
kylescritten@Kyles-MacBook-Air ~ % cd ~/Downloads
kylescritten@Kyles-MacBook-Air Downloads % chmod 400 labsuser.pem
kylescritten@Kyles-MacBook-Air Downloads % ssh -i labsuser.pem ec2-user@35.86.247.199
The authenticity of host '35.86.247.199 (35.86.247.199)' can't be established.
ED25519 key fingerprint is: SHA256:HvYonbFWFJEqXA6GaOibOPHLy24mUp9N9jNCwIuoqmI
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```
#### Terminal Output
```text
Warning: Permanently added '35.86.247.199' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-0-10-84 ~]$ 
```

## Challenge: My Solution

1. Created a new file called `bash_script.sh`.
```bash
touch bash_script.sh
```

2. Inserted the code using the `vi` editor by running `vi bash_script.sh` and pressing `i`
```bash
#!/bin/bash

prefix="Kyle"

max=$(ls ${prefix}* 2>/dev/null | sed 's/[^0-9]//g' | sort -n | tail -1)
max=${max:-0}
echo "Previous number: $max"

for i in {1..25}
do
#echo ${prefix}$(($i+$max))
touch ${prefix}$(($i+$max))
done
```

> [!Note]
> - `ls ${prefix}*` lists existing files; `2>/dev/null` suppresses errors if none exist yet
> - `sed 's/[^0-9]//g'` strips the prefix, leaving only numbers
> - `sort -n | tail -1` picks the highest number
> - `${max:-0}` defaults to `0` if no files exist yet, so the first run creates `Kyle1`–`Kyle25`, the second creates `Kyle26`–`Kyle50`, and so on

3. Saved and exited the editor by pressing `ESC` then `:wq` and `Enter` 

3. I made the file executable and ran it using the following commands:
```bash
chmod 744 bash_script.sh
./bash_script.sh
```

4. After the first run, below is the content displayed of my directory
```bash
[ec2-user@ip-10-0-10-84 ~]$ ./bash_script.sh
Previous number: 0
[ec2-user@ip-10-0-10-84 ~]$ ll -v
total 4
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle1
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle2
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle3
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle4
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle5
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle6
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle7
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle8
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle9
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle10
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle11
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle12
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle13
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle14
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle15
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle16
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle17
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle18
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle19
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle20
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle21
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle22
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle23
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle24
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle25
-rwxr--r--  1 ec2-user ec2-user  226 Jun 26 21:27 bash_script.sh
drwxr-xr-x 11 ec2-user Personnel 184 Jun 26 20:58 companyA
```

5. The content of the directory after the second run is as shown below
```bash
[ec2-user@ip-10-0-10-84 ~]$ ./bash_script.sh
Previous number: 25
[ec2-user@ip-10-0-10-84 ~]$ ll -v
total 4
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle1
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle2
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle3
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle4
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle5
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle6
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle7
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle8
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle9
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle10
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle11
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle12
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle13
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle14
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle15
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle16
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle17
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle18
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle19
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle20
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle21
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle22
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle23
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle24
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:27 Kyle25
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle26
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle27
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle28
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle29
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle30
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle31
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle32
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle33
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle34
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle35
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle36
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle37
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle38
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle39
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle40
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle41
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle42
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle43
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle44
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle45
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle46
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle47
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle48
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle49
-rw-rw-r--  1 ec2-user ec2-user    0 Jun 26 21:29 Kyle50
-rwxr--r--  1 ec2-user ec2-user  226 Jun 26 21:27 bash_script.sh
drwxr-xr-x 11 ec2-user Personnel 184 Jun 26 20:58 companyA
```
