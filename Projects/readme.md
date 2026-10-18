# 🚀 Projects

[← Back to the main portfolio](../README.md)

These projects show how I apply AWS services to real business problems, from designing a multi-region architecture that can handle unpredictable traffic to building and hosting a working website for a small restaurant. Each project has its own documentation covering the problem, the AWS services chosen and why, and the trade-offs and challenges along the way.

| Project | Overview | Core Stack |
|---|---|---|
| [3D E-commerce](./3D-ecommerce%20/) | A multi-region AWS architecture design for a global 3D e-commerce platform selling EcoFlow portable power and solar systems. It handles unpredictable, weather-driven traffic surges while staying highly available, secure, and cost-efficient. | `Route 53` `CloudFront` `S3` `WAF & Shield` `ALB` `EC2 Auto Scaling` `Lambda` `EventBridge` `Aurora` `DynamoDB` `ElastiCache` `CloudWatch` |
| [S3 Website](./S3-Website/) | A static website for Ubuntu Braai & Lounge, hosted on Amazon S3, where customers can browse the menu, place orders and make reservations. It replaces a mixed-up manual booking process with a low-cost solution, backed by a planned serverless architecture for future growth. | `S3` `HTML5` `CSS3` `JavaScript` `Cognito` `API Gateway` `Lambda` `DynamoDB` `SES` `SQS` `CloudFront` |
