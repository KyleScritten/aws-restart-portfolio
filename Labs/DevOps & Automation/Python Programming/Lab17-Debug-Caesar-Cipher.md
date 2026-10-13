# Debugging the Caesar Cipher Program

A *debugger* is a computer program that is used to test and find bugs (debug) other programs. 
In this lab, I will use the Python Debugger (pdb) to find and fix bugs in a Python program.

The correct output of the Caesar Cipher program `caesar_cipher.py` is:
```bash
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: AWS Restart rocks!
AWS Restart rocks!
Please enter a key (whole number from 1-25): 2
2
Encrypted Message: CYU TGUVCTV TQEMU!
Decypted Message: AWS RESTART ROCKS!
```

## Caesar Cipher Program Bug #1

The buggy Caesar Cipher program [debug-caesar-1.py](./python-scripts/debug-caesar-1.py) returns this error:
```bash
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: AWS Restart rocks!
AWS Restart rocks!
Please enter a key (whole number from 1-25): 2
2
Traceback (most recent call last):
  File "/home/ec2-user/environment/debug-caesar-1.py", line 56, in <module>
    runCaesarCipherProgram()
  File "/home/ec2-user/environment/debug-caesar-1.py", line 50, in runCaesarCipherProgram
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ec2-user/environment/debug-caesar-1.py", line 28, in encryptMessage
    newPosition = position + cipherKey
                  ~~~~~~~~~^~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

However, errors that result in a traceback are usually easier to fix because the traceback provides helpful clues, like line numbers.
The error is at line 28: `newPosition = position + cipherKey`. The variable `cipherKey` is a string and needs to be converted into an integer in order to be added to the position and return an integer.
To fix the program, I just modified the line to `newPosition = position + int(cipherKey)`.

## Caesar Cipher Program Bug #2

The buggy Caesar Cipher Program [debug-caesar-2.py](./python-scripts/debug-caesar-2.py) returns an incorrect encrypted message, indicating the presence of a bug in the encryption function.
```bash
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: AWS Restart rocks!
AWS Restart rocks!
Please enter a key (whole number from 1-25): 2
2
Encrypted Message: CYU Testart rocks!
Decrypted Message: AWS Restart rocks!
``` 

However, no explanation of the issue is provided. To investigate the bug, I executed the program multiple times with different inputs and observed that uppercase letters were correctly encrypted, while lowercase letters were not. This indicates that line 25 in the `encryptMessage` function is missing the conversion to uppercase. The correct statement should be: `uppercaseMessage = message.upper()`.

## Caesar Cipher Program Bug #3

The buggy Caesar Cipher Program [debug-caesar-3.py](./python-scripts/debug-caesar-3.py) returns an incorrect decrypted message, indicating a bug in the decryption function.
```bash
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: AWS Restart rocks!
AWS Restart rocks!
Please enter a key (whole number from 1-25): 2
2
Encrypted Message: CYU TGUVCTV TQEMU!
Decrypted Message: EAW VIWXEVX VSGOW!
```

Indeed, in the `decryptMessage` function, the code incorrectly uses `cipherKey` instead of `decryptKey` when calling `encryptMessage`. 
The correct decryption function is:
```python
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, cipherKey, alphabet)
```

## Caesar Cipher Program Bug #4

The buggy Caesar Cipher Program [debug-caesar-4.py](./python-scripts/debug-caesar-4.py) produces a decrypted output that is the same as the encrypted message, indicating a bug in the decryption logic.
```bash
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: AWS Restart rocks!
AWS Restart rocks!
Please enter a key (whole number from 1-25): 2
2
Encrypted Message: CYU TGUVCTV TQEMU!
Decrypted Message: CYU TGUVCTV TQEMU!
```

Indeed, the final print statement in the main program is incorrect. It prints `myEncryptedMessage` instead of `myDecryptedMessage`.
The correct statement is: 
```bash
print(f'Decrypted Message: {myDecryptedMessage}')
```

## Conclusion
After completing this lab, I am able to:

* Use the Python Debugger
* Debug the different versions of the Caesar cipher program that you created in a previous lab
