# Python Scripting Exercise - Challenge Lab

## Using SSH to Connect to the Linux Host

First, I will connect to the Linux Host. I run macOS and will use an SSH utility to perform all of these operations. 

I downloaded the file labsuser.pem from the lab environment and saved the PublicIP address, which for my lab is PublicIP `35.90.208.198`. From my terminal, allowing the first connection to this remote SSH server. 

#### Connect to the Linux Host
```bash
kylescritten@Kyles-MacBook-Air ~ % cd ~/Downloads
kylescritten@Kyles-MacBook-Air Downloads % chmod 400 labsuser.pem
kylescritten@Kyles-MacBook-Air Downloads % ssh -i labsuser.pem ec2-user@35.90.208.198
The authenticity of host '35.90.208.198 (35.90.208.198)' can't be established.
ED25519 key fingerprint is: SHA256:R3SEFvcsNJ6TL0JvJXKAkP+nDUSzxP5AB/dDAi1mQfA
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

#### Terminal Output
```text
Warning: Permanently added '35.90.208.198' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-1-11-229 ~]$  
```

## Challenge

* Write a Python script to:
  - Display all the **prime numbers between 1 to 250**.
  - Store the results in a **results.txt** file.
* Test the script. Verify that it produced the expected results in the **results.txt** file.
* **Save the script** and **make a note of its location (absolute path)** for future reference.
* Use ***python3***

## Solution

I decide to use a brute-force approach to find the prime numbers between 1 and 250.

After logging into the Linux Host via SSH, I create a folder `python` and change directories to this folder. To do this I run the following commands:

```bash
# Confirm you’re in your home directory
cd ~
pwd

# Create the python folder
mkdir python

# Move into the new folder
cd python

# Confirm you’re in the right place
pwd

# Create your Python script file inside this folder
nano prime_numbers.py
```

I create the program [prime-numbers.py](./python-scripts/prime-numbers.py) through the nano editor, so that the location of my python script is `/home/ec2-user/python`.

*This is the full script for this lab here:*

```python
# ----------------------------------------------------------------------------------
#                  PRIME NUMBERS BETWEEN 1 AND 250
# Python 3.11.3
# Coding: utf-8
# Author: CT, 2026.04.15
# ----------------------------------------------------------------------------------
import math

def is_prime(number):
    max_div=int(math.sqrt(number))
    d=2
    while(d<=max_div):
        if number % d == 0:
            return False
        d+=1
    return True
    
def write_on_file(filename, list):
    with open(filename, "w") as file:
        file.write("\n".join(str(n) for n in list))
        file.write("\n")
    
def main():
    start=2
    end=250
    prime_list=[]
    for n in range(start,end):
        if is_prime(n):
            prime_list.append(n)
    print(f"There are {len(prime_list)} prime numbers between {start} and {end}")
    print(",".join(str(n) for n in prime_list))
    write_on_file("results.txt", prime_list)
    
main()
```

To run the code, while in the folder `python`, I run the following command on terminal:
```bash
python3 prime-numbers.py
```

The program returns the following output on screen:
```bash
[ec2-user@ip-10-1-11-229 python]$ python3 prime-numbers.py
There are 53 prime numbers between 2 and 250
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241
```

The program also prints the prime numbers on the file [results.txt](./files/results.txt), one number per line.

First I check that the number of rows of the file is equal to the total number of prime numbers found by the program:
```bash
[ec2-user@ip-10-1-11-229 python]$ wc -l results.txt
53 results.txt
```

Then, I open the file and manually check the results:
```bash
[ec2-user@ip-10-1-11-229 python]$ cat results.txt
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
211
223
227
229
233
239
241
```

*All prime numbers were there, as expected.*
