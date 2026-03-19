<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 47: Priority Queuing System using Amazon SQS, SNS, and Lambda</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=E0TJOxBS-gk">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Implement a highly decoupled, priority-based message queuing architecture using Amazon SNS to fan out notifications to different SQS queues, parsed by a single Lambda function via CloudFormation.

---

### 🛠️ Hands-On CloudFormation & Commands

```yaml
# nautilus-priority-stack.yml
AWSTemplateFormatVersion: '2010-09-09'
Description: >
  Nautilus Priority Queuing System using Amazon SQS, SNS, and Lambda.
  Uses only AWS managed policies.

Resources:
  # IAM Role
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
        - arn:aws:iam::aws:policy/AmazonSQSFullAccess
        - arn:aws:iam::aws:policy/AmazonSNSFullAccess

  # SQS Queues
  NautilusHighPriorityQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: nautilus-High-Priority-Queue
      VisibilityTimeout: 30
      MessageRetentionPeriod: 86400

  NautilusLowPriorityQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: nautilus-Low-Priority-Queue
      VisibilityTimeout: 30
      MessageRetentionPeriod: 86400

  # SQS Queue Policies
  NautilusHighPriorityQueuePolicy:
    Type: AWS::SQS::QueuePolicy
    Properties:
      Queues:
        - !Ref NautilusHighPriorityQueue
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: sns.amazonaws.com
            Action: sqs:SendMessage
            Resource: !GetAtt NautilusHighPriorityQueue.Arn
            Condition:
              ArnEquals:
                aws:SourceArn: !Ref NautilusPriorityQueuesTopic

  NautilusLowPriorityQueuePolicy:
    Type: AWS::SQS::QueuePolicy
    Properties:
      Queues:
        - !Ref NautilusLowPriorityQueue
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: sns.amazonaws.com
            Action: sqs:SendMessage
            Resource: !GetAtt NautilusLowPriorityQueue.Arn
            Condition:
              ArnEquals:
                aws:SourceArn: !Ref NautilusPriorityQueuesTopic

  # SNS Topic
  NautilusPriorityQueuesTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: nautilus-Priority-Queues-Topic

  # SNS Subscriptions (with Filters)
  HighPrioritySubscription:
    Type: AWS::SNS::Subscription
    Properties:
      TopicArn: !Ref NautilusPriorityQueuesTopic
      Protocol: sqs
      Endpoint: !GetAtt NautilusHighPriorityQueue.Arn
      FilterPolicy:
        priority:
          - high

  LowPrioritySubscription:
    Type: AWS::SNS::Subscription
    Properties:
      TopicArn: !Ref NautilusPriorityQueuesTopic
      Protocol: sqs
      Endpoint: !GetAtt NautilusLowPriorityQueue.Arn
      FilterPolicy:
        priority:
          - low

  # Lambda Function
  NautilusPrioritiesQueueFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: nautilus-priorities-queue-function
      Runtime: python3.12
      Handler: index.lambda_handler
      Role: !GetAtt LambdaExecutionRole.Arn
      Timeout: 60
      MemorySize: 128
      Environment:
        Variables:
          high_priority_queue: !Ref NautilusHighPriorityQueue
          low_priority_queue: !Ref NautilusLowPriorityQueue
      Code:
        ZipFile: |
          import boto3
          import os
          sqs = boto3.client('sqs')
          def delete_message(queue_url, receipt_handle, message):
              response = sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
              return "Message " + "'" + message + "'" + " deleted"

          def poll_messages(queue_url):
              QueueUrl=queue_url
              response = sqs.receive_message(
                  QueueUrl=QueueUrl,
                  AttributeNames=[],
                  MaxNumberOfMessages=1,
                  MessageAttributeNames=['All'],
                  WaitTimeSeconds=3
              )
              if "Messages" in response:
                  receipt_handle=response['Messages'][0]['ReceiptHandle']
                  message = response['Messages'][0]['Body']
                  delete_response = delete_message(QueueUrl,receipt_handle,message)
                  return delete_response
              else:
                  return "No more messages to poll"

          def lambda_handler(event, context):
              response = poll_messages(os.environ['high_priority_queue'])
              if response == "No more messages to poll":
                  response = poll_messages(os.environ['low_priority_queue'])
              return response
```

**Deploy and Test:**
```bash
aws cloudformation create-stack \
  --stack-name nautilus-priority-stack \
  --template-body file:///root/nautilus-priority-stack.yml \
  --capabilities CAPABILITY_NAMED_IAM

aws cloudformation wait stack-create-complete --stack-name nautilus-priority-stack

# Publish Test Messages
topicarn=$(aws sns list-topics --query "Topics[?contains(TopicArn, 'nautilus-Priority-Queues-Topic')].TopicArn" --output text)
aws sns publish --topic-arn $topicarn --message 'High Priority message 1' --message-attributes '{"priority" : { "DataType":"String", "StringValue":"high"}}'
aws sns publish --topic-arn $topicarn --message 'High Priority message 2' --message-attributes '{"priority" : { "DataType":"String", "StringValue":"high"}}'
aws sns publish --topic-arn $topicarn --message 'Low Priority message 1' --message-attributes '{"priority" : { "DataType":"String", "StringValue":"low"}}'
aws sns publish --topic-arn $topicarn --message 'Low Priority message 2' --message-attributes '{"priority" : { "DataType":"String", "StringValue":"low"}}'

# Invoke Lambda
aws lambda invoke --function-name nautilus-priorities-queue-function --payload '{}' response.json && cat response.json
```

---


## 🎯 Key Takeaways & Best Practices

- 📨 **Pub/Sub Messaging:** Amazon SNS easily "fans out" published messages to multiple subscribed SQS queues based on clever Filter Policies.
- 🏗️ **Decoupling Systems:** SQS allows massive backlogs of tasks to safely sit in a highly durable queue until a consumer (like Lambda) is ready to process them.
- 📜 **Infrastructure as Code (IaC):** AWS CloudFormation securely provisions dozens of resources (SNS, SQS, Lambda, IAM) perfectly from a single YAML template.

---

## 💡 Real-World Scenario

> **E-Commerce Orders:** VIP customer orders are immediately separated into a 'High Priority' queue to be processed by shipping logic instantly, while regular orders fall into the 'Low Priority' queue gracefully.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon SQS (Simple Queue Service):** A fully managed message queuing service that fundamentally enables you to decouple and scale microservices, distributed systems, and serverless applications flawlessly.
- **Amazon SNS (Simple Notification Service):** A highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices and immediately "fan out" messages to multiple endpoints simultaneously.
- **AWS Lambda:** A massively scalable serverless compute service that runs your precise code logic synchronously or asynchronously in response to triggers (events). It automatically provisions and manages all underlying servers, charging only for active execution time.
- **AWS CloudFormation:** An Infrastructure as Code (IaC) service that intelligently provisions, cleanly updates, and predictably tears down vast architectures of AWS resources seamlessly using simple YAML or JSON templates.
- **AWS IAM (Identity and Access Management):** A foundational service enabling you to securely manage access to AWS resources via strict policies.
- **IAM Roles:** An identity that you can dynamically assume to temporarily grant specific permissions. Instead of sharing fragile access keys, services like Lambda assume execution roles seamlessly.
