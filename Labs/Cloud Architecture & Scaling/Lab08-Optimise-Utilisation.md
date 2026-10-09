# Optimize Utilization



<p align="center">
  <img src="images/optimization-lab-topologies.png" alt="Topology of the Café web application runtime environment Before and After optimization” width="900">
</p>

*This diagram illustrates the topology of the Café web application runtime environment before and after the optimization.*

## Task 1: Optimize the website to reduce costs

### Task 1.1: Connect to the Café instance by using SSH

### Task 1.2: Connect to the CLI Host instance by using SSH

### Task 1.3: Uninstall MariaDB and resize the instance



<p align="center">
  <img src="images/cafe-website-downsized.png" alt="Downsized CafeInstance website” width="900">
</p>

*Exercise the website's functions to verify that it works properly. I have successfully uninstalled the decommissioned local database and downsized the Café instance.*

## Task 2: Use the AWS Pricing Calculator to estimate AWS service costs

### Task 2.1: Calculate the costs before optimization



<p align="center">
  <img src="images/calculator-before.png" alt=" AWS Calculator before optimization” width="900">
</p>

```
AWS Services Before Optimization Estimated Monthly Cost: $
```

### Task 2.2: Calculate the costs after optimization



<p align="center">
  <img src="images/calculator-after.png" alt="AWS Calculator after optimization” width="900">
</p>

```
AWS Services After Optimization Estimated Monthly Cost: $
```

### Task 2.3: Estimate the projected cost savings for Café

I calculated the costs of the AWS services that were needed to run the Café website both before and after I optimize the instance. Therefore, I can estimate the overall projected cost savings as follows:

```
Before optimization monthly costs:
    - Amazon EC2 service         $ 
    - Amazon RDS service         $
                                --------
    Total                        $

After optimization monthly costs:
    - Amazon EC2 service         $  
    - Amazon RDS service         $
                                --------
    Total                        $


Overall monthly cost savings      $
```

By removing the decommissioned local database and downsizing the Café instance type, the project will save about $ per month in AWS service costs.

## Conclusion

In this lab, I successfully optimized the Café web application infrastructure by removing an unused local database and downsizing the EC2 instance. 
These changes reduced both compute and storage costs without affecting application functionality.

Using the AWS Pricing Calculator, I confirmed that the optimizations resulted in an estimated monthly savings of $10.42. This exercise demonstrated 
how small architectural improvements can lead to meaningful cost reductions in cloud environments while maintaining performance and reliability.

After completing this activity, I am able to:
* I optimized an Amazon Elastic Compute Cloud (Amazon EC2) instance to reduce costs.
* I used the AWS Pricing Calculator to estimate AWS service costs.


## Bash Commands

```bash
# Stop the MariaDB service on the CafeInstance
sudo systemctl stop mariadb

# Remove the MariaDB server package from the CafeInstance
sudo yum -y remove mariadb-server

# Retrieve the AWS region from the instance metadata
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region

# Configure AWS CLI with credentials, region, and output format
aws configure

# Describe EC2 instances filtered by the CafeInstance tag to get the instance ID
aws ec2 describe-instances \
--filters "Name=tag:Name,Values= CafeInstance" \
--query "Reservations[*].Instances[*].InstanceId"

# Stop the CafeInstance EC2 instance (replace <instance-id> with actual ID)
aws ec2 stop-instances --instance-ids <instance-id>

# Modify the instance type to t3.micro (replace <instance-id> with actual ID)
aws ec2 modify-instance-attribute \
--instance-id <instance-id> \
--instance-type "{\"Value\": \"t3.micro\"}"

# Start the CafeInstance EC2 instance (replace <instance-id> with actual ID)
aws ec2 start-instances --instance-ids <instance-id>

# Check instance details including type, DNS, IP, and status (replace <instance-id>)
aws ec2 describe-instances \
--instance-ids <instance-id> \
--query "Reservations[*].Instances[*].[InstanceType,PublicDnsName,PublicIpAddress,State.Name]"
```
