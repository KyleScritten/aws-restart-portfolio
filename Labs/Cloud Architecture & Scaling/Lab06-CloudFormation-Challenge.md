# Using AWS CloudFormation to create an AWS VPC and Amazon EC2 instance

This lab focused on using AWS CloudFormation to deploy infrastructure as code (IaC) in order to create a basic AWS environment. 
The environment consisted of a Virtual Private Cloud (VPC), Internet Gateway, subnet configuration, security group rules, and an EC2 instance deployed inside the network.

The purpose of the lab was to build and troubleshoot a CloudFormation template through iterative testing until all required resources were successfully deployed.

## Solution

I started by accessing the AWS CLI environment and verifying that my credentials were properly configured. I confirmed access using the identity command : 

```bash
aws sts get-caller-identity 
```

#### Terminal output
```bash
eee_W_6371970@runweb254541:~$ aws sts get-caller-identity                                            
{                                                                                                    
    "UserId": "AROA32AAZYYGE3VMS74DQ:user5168917=Kyle_Scritten",                                     
    "Account": "811750508044",                                                                       
    "Arn": "arn:aws:sts::811750508044:assumed-role/voclabs/user5168917=Kyle_Scritten"                
}                   
````

After confirming access, I wrote the CloudFormation template and uploaded it to the lab environment successfully.

*Here is the final version:* [template.yaml](./files/template.yaml).

I then proceeded to create the CloudFormation stack using the AWS CLI:

```bash
aws cloudformation create-stack \
--stack-name myStack \
--template-body file://template.yaml \
--parameters ParameterKey=KeyName,ParameterValue=vockey
```

#### Terminal output
```bash                                                            
{                                                                  
    "StackId": "arn:aws:cloudformation:us-west-2:811750508044:stack/myStack/4d6163715c5dea5"
}
```

During deployment, I monitored the stack progress using CloudFormation commands and JMESPath filtering:

```bash
aws cloudformation describe-stack-resources \
--stack-name myStack \
--query 'StackResources[*].[ResourceType,ResourceStatus]' \
--output table
```

This helped me track resource creation in real time.

![Stack Monitoring](./images/EX-05-stack-monitor.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="900">
</p>

I also validated the overall stack status:

```bash
aws cloudformation describe-stacks \
--stack-name myStack
```

PLACEHOLDER IMAGE OF TERMINAL

I waited until it reached `CREATE_COMPLETE`.

Finally, I verified that all resources were successfully deployed:

* VPC created successfully
* Internet Gateway attached
* Security group configured for SSH access
* EC2 instance launched in the VPC

![Successful Deployment](./images/EX-05-successful-deployment.png)

<p align="center">
  <img src="images/NAME.png" alt="DESCRIPTION” width="900">
</p>

## Conclusion

In this lab, I learned how to deploy and troubleshoot AWS infrastructure using CloudFormation and the AWS CLI. I gained experience identifying template validation errors, correcting configuration issues, and monitoring stack deployment using CLI commands.

I also learned how small syntax mistakes in a CloudFormation template can prevent deployment and how iterative debugging is essential for successful infrastructure creation. By the end of the lab, I was able to successfully deploy a complete AWS environment using infrastructure as code.

## Additional Resources

* [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)
* [Boto3 documentation](https://docs.aws.amazon.com/boto3/latest/)
   
