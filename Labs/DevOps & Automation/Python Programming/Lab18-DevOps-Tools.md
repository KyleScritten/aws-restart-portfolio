# Evaluate a DevOps Tool : Jenkins VS AWS CodeDeploy

## Lab overview

The landscape for DevOps tools is continuously changing as new products and technology come to market. In this lab, I research a DevOps tool and identify use cases for it.

For the purpose of this lab, I have chosen to compare **Jenkins** and **AWS CodeDeploy** as DevOps tools.

## Question 1: What does each DevOps tool do?

### Jenkins

**_Jenkins_** is an open-source automation server used for Continuous Integration and Continuous Delivery (CI/CD). It builds code, runs automated tests, and deploys applications using pipelines that can be highly customized.

### AWS CodeDeploy

_**AWS CodeDeploy**_ is a fully managed AWS deployment service that automates application deployments to EC2 instances, Lambda functions, and on-premises servers. It focuses specifically on deployment automation and release management.

## Question 2: Why is each DevOps tool important?

### Jenkins

**_Jenkins_** is important because it:

* Automates the software build and testing process
* Reduces human error in development workflows
* Enables fast feedback through continuous integration
* Supports complex and customizable DevOps pipelines

It is widely used to improve development speed and software quality.

### AWS CodeDeploy

_**AWS CodeDeploy**_ is important because it:

* Automates application deployment processes
* Reduces downtime during updates
* Provides safe deployment strategies like blue/green deployments
* Integrates well with AWS services for scalable cloud applications

It ensures reliable and consistent software releases.

## Question 3: Identify specific use cases for the DevOps tools.

### Jenkins use cases

**_Jenkins_** is used for:

* Continuous Integration (auto-building code on commit)
* Running automated test suites
* Multi-stage CI/CD pipelines
* Integrating with tools like Docker, Git, and Kubernetes
* Deploying applications across multiple environments

### AWS CodeDeploy use cases

_**AWS CodeDeploy**_ is used for:

* Deploying applications to Amazon EC2 instances
* Automating AWS Lambda function updates
* Performing rolling and blue/green deployments
* Managing production release deployments with rollback support
* Updating on-premises server applications

# Conclusion

**_Jenkins_** and AWS CodeDeploy serve different but complementary roles in the DevOps lifecycle. Jenkins is a flexible, open-source automation server that drives the build and test stages of CI/CD, offering extensive customization through pipelines and integrations with tools like Docker, Git, and Kubernetes. _**AWS CodeDeploy**_, by contrast, is a fully managed AWS service focused specifically on the deployment stage, automating releases to EC2, Lambda, and on-premises servers with built-in safety features like blue/green deployments and rollback support.

Both tools reduce manual effort and human error in the software delivery process, but they do so at different points: Jenkins improves speed and quality earlier in the pipeline through continuous integration and testing, while AWS CodeDeploy improves reliability and reduces downtime at the point of release. Used together, they can cover the full DevOps lifecycle — Jenkins managing the build-and-test workflow, and AWS CodeDeploy managing a safe, AWS-native deployment.
