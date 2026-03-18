<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 37: Managing EC2 Access with S3 Role-Based Permissions</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=pKS2mBBXYBE">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Securely grant an EC2 instance access to an S3 bucket using IAM Roles instead of insecurely hardcoding AWS credentials.

---

### 🛠️ IAM Policy Setup

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::nautilus-s3-795180432757",
                "arn:aws:s3:::nautilus-s3-795180432757/*"
            ]
        }
    ]
}
```

---


## 🎯 Key Takeaways & Best Practices

- 🚫 **No Hardcoded Keys:** Using IAM Roles completely avoids the leakage risks associated with hardcoding `aws_access_key_id`.
- 🔄 **Temporary Credentials:** Roles auto-rotate short-lived credentials behind the scenes via the metadata service.

---

## 💡 Real-World Scenario

> **Data Processing:** A script running securely on an EC2 instance processes nightly log files stored securely in S3 without managing explicit secret keys.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Amazon S3 (Simple Storage Service):** An object storage service offering scalable data availability and security. You can use S3 to store back-ups, hold application assets, or directly host static HTML websites.
- **AWS IAM (Identity and Access Management):** A foundational service enabling you to securely manage access to AWS resources. You create Users (people), Groups, Roles (temporary service permissions), and govern access using JSON Policies.
