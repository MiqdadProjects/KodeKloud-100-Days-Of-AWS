<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 48: Deploy AWS Lambda App via CloudFormation</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=rzFCBmH0PKw">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Automate the provisioning of a serverless Lambda function and its required IAM Execution Role seamlessly using AWS CloudFormation Infrastructure as Code (IaC).

---

### 🛠️ Hands-On CloudFormation & Commands

```yaml
# nautilus-lambda.yml
AWSTemplateFormatVersion: '2010-09-09'
Description: >
  Nautilus Lambda App - Creates a Lambda function that returns
  "Welcome to KKE AWS Labs!" with status code 200.

Resources:
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: lambda_execution_role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

  NautilusLambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: nautilus-lambda
      Runtime: python3.12
      Handler: index.lambda_handler
      Role: !GetAtt LambdaExecutionRole.Arn
      Timeout: 30
      MemorySize: 128
      Code:
        ZipFile: |
          import json

          def lambda_handler(event, context):
              return {
                  'statusCode': 200,
                  'body': 'Welcome to KKE AWS Labs!'
              }
```

**Deploy and Test:**
```bash
aws cloudformation create-stack \
  --stack-name nautilus-lambda-app \
  --template-body file:///root/nautilus-lambda.yml \
  --capabilities CAPABILITY_NAMED_IAM

aws cloudformation wait stack-create-complete --stack-name nautilus-lambda-app

aws lambda invoke --function-name nautilus-lambda --payload '{}' response.json && cat response.json
```

---


## 🎯 Key Takeaways & Best Practices

- 📦 **Inline Lambda Code:** For very small serverless functions, CloudFormation allows embedding python code directly in the template `ZipFile` property.
- 🔒 **Managed Policies:** Relying exclusively on AWS Managed Policies (e.g. `AWSLambdaBasicExecutionRole`) strictly avoids custom inline IAM role blockages in restricted sandbox environments.

---

## 💡 Real-World Scenario

> **Rapid Prototyping:** A DevOps team leverages CloudFormation to rapidly spin up and tear down a testing environment involving Lambda hundreds of times a day perfectly consistently.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **AWS Lambda:** A massively scalable serverless compute service that runs your precise code logic synchronously or asynchronously in response to triggers (events). It automatically provisions and manages all underlying servers, charging only for active execution time.
- **AWS CloudFormation:** An Infrastructure as Code (IaC) service that intelligently provisions, cleanly updates, and predictably tears down vast architectures of AWS resources seamlessly using simple YAML or JSON templates.
- **AWS IAM (Identity and Access Management):** A foundational service enabling you to securely manage access to AWS resources via strict policies.
- **IAM Roles:** An identity that you can dynamically assume to temporarily grant specific permissions. Instead of sharing fragile access keys, services like Lambda assume execution roles seamlessly.
