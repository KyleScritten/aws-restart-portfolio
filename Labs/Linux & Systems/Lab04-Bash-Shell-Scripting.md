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

```
#### Terminal Output
```text

```

## Challenge: My Solution

1. Created a new file called `bash_script.sh`.
```bash
touch bash_script.sh
```

2. Inserted the code using the `vi` editor and pressing `i`
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

3. Save and exited the editor by pressing ESC then `:wq` and Enter 

3. I made the file executable and ran it using the following commands:
```bash
chmod 744 bash_script.sh
./bash_script.sh
```

4. After the first run, below is the content displayed of my directory
```bash
```

5. The content of the directory after the second run is as shown below
```bash
```
