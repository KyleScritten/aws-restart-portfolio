# Troubleshoot CloudFormation

# Troubleshoot CloudFormation

## Activity overview

In this activity, I practice troubleshooting AWS CloudFormation deployments. I begin by querying JavaScript Object Notation (JSON)-formatted data using JMESPath, then move into my AWS account, where the environment provides an Amazon Elastic Compute Cloud (Amazon EC2) instance named CLI Host, running in a virtual private cloud (VPC) named VPC2. I establish a Secure Shell (SSH) connection to the CLI Host, and from there use the AWS Command Line Interface (AWS CLI) to run AWS CloudFormation commands that create a stack with resources in the AWS account — my first attempt to create the stack fails and requires troubleshooting.

I then manually modify a resource created by the AWS CloudFormation stack, outside of the context of CloudFormation, and use CloudFormation to detect the resulting drift. Finally, I attempt to delete the stack and encounter issues along the way. In the Challenge section, I must figure out how to successfully delete the stack while keeping the Amazon Simple Storage Service (Amazon S3) bucket that was originally created by the stack and now contains objects.


*The architectural diagram below illustrates the setup that is used in tasks this activity:*

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="900">
</p>

*The architectural diagram below illustrates the setup that is used in tasks this activity.*











## Conclusion
After completing this activity, I am able to:
* **Practice** using JMESPath to query JSON-formatted documents
* **Troubleshoot** the deployment of an AWS CloudFormation stack using the AWS CLI
* **Analyze** log files on a Linux EC2 instance to determine the cause of a `create-stack` failure
* **Troubleshoot** a failed `delete-stack` action

## Additional resources
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/delete-stack.html)
