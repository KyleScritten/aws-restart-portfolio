# Data Protection Using Encryption
Cryptography is the conversion of communicated information into secret code that keeps the information confidential and private. Functions include authentication, data integrity, and nonrepudiation. The central function of cryptography is encryption, which transforms data into an unreadable form.

Encryption ensures privacy by keeping information hidden from people it is not intended for. Decryption, the opposite of encryption, transforms encrypted data back into readable data; it won't make any sense until it has been properly decrypted.

## Lab overview
In this lab, I connect to a file server hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance. I configure the AWS Encryption command line interface (CLI) on the instance, and create an encryption key using the AWS Key Management Service (AWS KMS). I use this key to encrypt and decrypt data. Next, I create multiple text files that are unencrypted by default, then use the AWS KMS key to encrypt the files and view them while they are encrypted. I finish the lab by decrypting the same files and viewing their contents.

## Task 1: Create an AWS KMS key
In this task, I create an AWS KMS key that I later use to encrypt and decrypt data.

> [!NOTE]
> With AWS KMS, I can create and manage cryptographic keys and control their use across a wide range of AWS services and in my applications. AWS KMS is a secure and resilient service that uses hardware security modules (HSMs) that have been validated under the Federal Information Processing Standard (FIPS) Publication 140-2, or are in the process of being validated, to protect my keys.

1. In the AWS Management Console, I choose **Key Management Service**.
2. I choose **Create a key**.
3. For **Key type**, I choose **Symmetric**, then choose **Next**.

> [!NOTE]
> *Symmetric* encryption uses the same key to encrypt and decrypt data, which makes it fast and efficient to use. *Asymmetric* encryption uses a public key to encrypt data and a private key to decrypt information.

4. On the **Add labels** page, I configure the following:
   * **Alias:** `MyKMSKey`
   * **Description:** `Key used to encrypt and decrypt data files.`
5. I choose **Next**.
6. On the **Define key administrative permissions** page, in the **Key administrators** section, I search for and select the check box for `voclabs`, then choose **Next**.
7. On the **Define key usage permissions** page, in the **This account** section, I search for and select the check box for `voclabs`, then choose **Next**. I review the settings, then choose **Finish**.
8. I choose the link for **MyKMSKey**, which I just created, and copy the **ARN (Amazon Resource Name)** value: 
```
arn:aws:kms:us-west-2:705225511426:key/d844d02d-733d-4dfd-8c2f-f29e78a1f163
```

## Task 2: Configure the File Server instance
In this task, I configure the AWS credentials file, which provides the ability to use the AWS KMS key I created earlier. I then install the AWS Encryption CLI, so that I can run encryption commands.

1. In the AWS Management Console, I choose **EC2**.
2. In the **Instances** list, I select the check box next to the **File Server** instance, then choose **Connect**.
3. I choose the **Session Manager** tab, then choose **Connect**.
4. To change to the home directory and create the AWS credentials file, I run the following commands:

```bash
cd ~
aws configure
```

**Terminal Output:**
```bash

```

5. When prompted, I configure the following:
   * **AWS Access Key ID:** Enter `1`, then press Enter.
   * **AWS Secret Access Key:** Enter `1`, then press Enter.
   * **Default region name:** Copy and paste the Region provided from the Vocareum AWS Details page.
   * **Default output format:** Press Enter.

*The AWS configuration file is created, however the entries of `1` are temporary placeholders that will be updated.*

6. I use the details provided from the Vocareum Lab console page.
7. To open the AWS credentials file, I run the following command:

```bash
vi ~/.aws/credentials
```

**Terminal Output:**
```bash

```

8. In the `~/.aws/credentials` file, I type `dd` multiple times to delete the contents of the file.
9. I paste in the code block I copied from the Vocareum Lab. The AWS credentials file now looks similar to the following:

**Terminal Output:**
```bash

```

*The AWS credentials file now includes the following: `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`. The credentials used are from the AWS Details section.*

10. To save and close the file, I press **Escape**, type `:wq`, and press Enter.
11. To view the updated contents of the file, I run the following command:

```bash
cat ~/.aws/credentials
```

**Terminal Output:**
```bash

```

Now I install the AWS Encryption CLI and export my path, so that I can run the commands to encrypt and decrypt data.

15. To install the AWS Encryption CLI and set my path, I run the following commands:

```bash
pip3 install aws-encryption-sdk-cli
export PATH=$PATH:/home/ssm-user/.local/bin
```

**Terminal Output:**
```bash

```

## Task 3: Encrypt and decrypt data
In this task, I learn how to encrypt plaintext data into ciphertext by running the `--encrypt` command. I then successfully decrypt the ciphertext back into the original, readable plaintext data.


<p align="center">
  <img src="images/encryption-diagram.png" alt="Diagram shows how encryption works” width="900">
</p>

*This diagram shows how encryption works with symmetric keys and algorithms. A symmetric key and algorithm are used to convert a plaintext message into ciphertext.*

<p align="center">
  <img src="images/decryption-diagram.png" alt="Diagram shows how decryption works” width="900">
</p>

*This diagram shows how the same secret key and symmetric algorithm from the encryption process are used to decrypt the ciphertext back into plaintext.*

## Conclusion
After completing this lab, I am able to:

* Create an AWS KMS encryption key
* Install the AWS Encryption CLI
* Encrypt plaintext
* Decrypt ciphertext
