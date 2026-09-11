
# Exercise 1: Retrieving the protein sequence of human preproinsulin

# 1.1 delete ORIGIN, 1, 61, //, and the spaces and return carriages
cleaned = ""

with open("preproinsulin-seq.txt", "r") as file:
    for line in file:
        if "ORIGIN" in line or "//" in line:
            continue
        parts = line.strip().split()
        # Skip the first element (line number like 1, 61)
        cleaned += "".join(parts[1:])

with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(cleaned)
    
    
# 1.2 Confirm that your file has 110 characters of lowercase letters
# which represent the amino acids in the sequence of human preproinsulin
with open("preproinsulin-seq-clean.txt", "r") as file:
    content = file.read()

print("Length:", len(content))
print("All lowercase:", content.islower())


# 1.3 Obtaining the protein sequence of human insulin

# Read cleaned sequence
with open("preproinsulin-seq-clean.txt", "r") as file:
    seq = file.read().strip()

# 1.4 Split regions (convert from 1-based to 0-based indexing)

# 1–24 amino acids
is_seq = seq[0:24]
with open("isinsulin-seq-clean.txt", "w") as file:
    file.write(is_seq)
print("I:", len(is_seq))

# 25–54 amino acids
b_seq = seq[24:54]
with open("binsulin-seq-clean.txt", "w") as file:
    file.write(b_seq)
print("B:", len(b_seq))

# 55–89 amino acids
c_seq = seq[54:89]
with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(c_seq)
print("C:", len(c_seq))

# 90–110 amino acids
a_seq = seq[89:110]
with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(a_seq)
print("A:", len(a_seq))


# 1.5 Combine fragments into mature insulin

# Read fragments
with open("binsulin-seq-clean.txt", "r") as file:
    b = file.read().strip()

with open("ainsulin-seq-clean.txt", "r") as file:
    a = file.read().strip()

# 1.6 Combine to form mature insulin
insulin = b + a

print("Mature insulin sequence:", insulin)
print("Length:", len(insulin))