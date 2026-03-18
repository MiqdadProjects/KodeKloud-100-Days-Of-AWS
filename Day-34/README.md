<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 34: Create Lambda Function Using AWS CLI</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=iaoMIZxZKH4">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Automate the deployment and testing of a Lambda function strictly using the AWS Command Line Interface (CLI).

---

### 🛠️ Hands-On Commands

```bash
echo "def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Welcome to KKE AWS Labs!'
    }" > lambda_function.py

zip function.zip lambda_function.py

ROLE_ARN=$(aws iam get-role --role-name lambda_execution_role --query 'Role.Arn' --output text)

aws lambda create-function \
    --function-name datacenter-lambda-cli \
    --runtime python3.9 \
    --role $ROLE_ARN \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip

aws lambda invoke --function-name datacenter-lambda-cli output.json

cat output.json
```

---


## 🎯 Key Takeaways & Best Practices

- 💻 **Automation First:** The CLI enables rapid, repeatable infrastructure deployments without manual UI clicks.
- 📜 **Inline Handlers:** Small functions can be quickly packaged as zip files and deployed programmatically over the CLI.

---

## 💡 Real-World Scenario

> **CI/CD Pipelines:** DevOps teams universally rely on the AWS CLI or automated scripting to update Lambda functions instantly via GitHub Actions.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **AWS IAM (Identity and Access Management):** A foundational service enabling you to securely manage access to AWS resources. You create Users (people), Groups, Roles (temporary service permissions), and govern access using JSON Policies.
- **AWS Lambda:** The pioneer of serverless compute services. It runs your strict code logic synchronously in response to triggers (events) and automatically provisions/manages the underlying servers. You simply pay precisely for the milliseconds your code executes.
