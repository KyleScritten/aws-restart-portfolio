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
