# Automating Deployments with AWS CloudFormation

Amazon Web Services (AWS) provides infrastructure automation capabilities through services such as CloudFormation, enabling consistent and repeatable deployments. In this lab, I explore how infrastructure can be defined as code using YAML templates and deployed automatically. The lab focuses on creating, modifying, and deleting a CloudFormation stack while integrating core AWS resources such as a Virtual Private Cloud (VPC), Security Groups, Amazon S3 buckets, and Amazon EC2 instances. This approach reduces manual configuration errors and improves deployment efficiency.

## Task 1: Deploy a CloudFormation Stack

*I begin by deploying a CloudFormation stack that creates a VPC as shown in this diagram:*

<p align="center">
  <img src="images/cf-stack-vpc-diagram.png" alt="Automating Deployments with AWS CloudFormation Architecture” width="900">
</p>

I started by downloading the provided [task1.yaml](./files/task1.yaml) template and examining its structure. The file contained three main sections: 
- [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html)
- [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html)
- [Outputs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html)

The Parameters section defined CIDR blocks for networking, the Resources section described the VPC and Security Group, and the Outputs section exposed useful information about the created resources.

The template is written in a format called YAML, which is commonly used for configuration files. The format of the file is important, including the indents and hyphens. CloudFormation templates can also be written in JSON.


## Task 2: Add an Amazon S3 Bucket to the Stack


## Task 3: Add an Amazon EC2 Instance to the Stack


## Task 4: Delete the Stack


## Conclusion

In this lab, I learned how to use AWS CloudFormation to automate infrastructure deployment. I created a stack from a YAML template, 
then incrementally updated it by adding an S3 bucket and an EC2 instance. This demonstrated how CloudFormation allows controlled and 
efficient modifications without redeploying existing resources. I also observed how dependencies between resources are managed automatically.

Overall, the lab highlighted the advantages of infrastructure as code, including consistency, scalability, and easier maintenance. 
Deleting the stack reinforced how CloudFormation simplifies cleanup by removing all associated resources in a single operation.

In summary, I learnt how to:
- Deploy an AWS CloudFormation stack with a defined Virtual Private Cloud (VPC), and Security Group.
- Configure an AWS CloudFormation stack with resources, such as an Amazon Simple Storage Solution (S3) bucket and Amazon Elastic Compute Cloud (EC2).
- Terminate an AWS CloudFormation and its respective resources.

## Additional resources
- [Amazon S3 Template Snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-s3.html)
- [AWS Compute Blog: Query for the latest Amazon Linux AMI IDs using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/)
- [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html)
