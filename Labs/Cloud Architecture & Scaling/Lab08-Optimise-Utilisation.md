# Optimize Utilization



<p align="center">
  <img src="images/optimization-lab-topologies.png" alt="Topology of the Café web application runtime environment Before and After optimization” width="900">
</p>

*This diagram illustrates the topology of the Café web application runtime environment before and after the optimization.*

## Task 2: Use the AWS Pricing Calculator to estimate AWS service costs

### Task 2.1: Calculate the costs before optimization


```
AWS Services Before Optimization Estimated Monthly Cost: $
```

### Task 2.2: Calculate the costs after optimization


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

