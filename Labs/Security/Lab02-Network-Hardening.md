# Networking Hardening: Using Amazon Inspector for Vulnerability Assessment and Remediation

## Lab overview
In this lab, I utilize Amazon Inspector to scan for vulnerabilities in my AWS resources, specifically AWS Lambda functions. I learn how to activate Amazon Inspector, interpret the vulnerability reports, and remediate the findings.

## Scenario
The developers at AnyCompany are in the initial phases of building an application primarily using AWS Lambda. Throughout the development process, they need an automated security tool that not only scans for vulnerable software packages, but also scans within the code itself. I decide to utilize Amazon Inspector to fill this need.

**Amazon Inspector** meets the requirement of being able to scan AWS Lambda functions by quickly responding to new deployments. It also automatically scans additional resources, such as EC2 instances and Amazon ECRs, within AnyCompany's AWS account.

## Task 1: Activate the Amazon Inspector

I began by navigating to the AWS Management Console, searching for and choosing **Inspector**, then choosing **Activate Inspector** to activate the service for my account and continuously scan my Lambda functions.

After activation, the dashboard indicated that scanning was in progress. I monitored the **Environment coverage** section, refreshing the page periodically until **Lambda functions** coverage reached 100%, confirming that all functions were being scanned.

The dashboard now shows my account number and activation status for AWS Lambda, with Lambda coverage at 100%. By default, scanning is activated for Amazon EC2, Amazon ECR, and AWS Lambda standard scanning.

## Conclusion
After completing this lab, I am able to:

* Activate Amazon Inspector
* Analyze and interpret vulnerability findings
* Remediate the vulnerabilities found by Amazon Inspector
