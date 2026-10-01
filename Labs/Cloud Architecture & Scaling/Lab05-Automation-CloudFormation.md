# Automating Deployments with AWS CloudFormation








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
