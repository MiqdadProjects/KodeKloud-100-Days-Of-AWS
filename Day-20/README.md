<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 20: Create IAM Role for EC2 with Policy Attachment</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=DpGBRUtfzn0">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

How does an EC2 instance securely grab a file from an S3 bucket or write logs to CloudWatch? Historically, engineers would hardcode an IAM User's Access Keys directly into the EC2 server's code or environment variables—a practice that leads to catastrophic data breaches when those keys are accidentally leaked.

The modern, secure solution is the **IAM Role**. An IAM Role allows an AWS service (like EC2) to temporarily "assume" permissions without ever using long-term passwords or access keys. In this task, you learn how to configure an IAM Role and map it securely to an EC2 instance.

---

## 🎯 Key Takeaways & Best Practices

- 🎭 **Temporary Trust:** Unlike an IAM User, a Role has absolutely no permanent credentials. Behind the scenes, the AWS Security Token Service (STS) constantly rotates temporary cryptographic keys to the EC2 server every few hours.
- 🤝 **Trust Policies:** An IAM Role requires two policies: a **Permission Policy** (what the role is allowed to do, e.g., read S3) and a **Trust Policy** (who is allowed to "wear" the role, e.g., the `ec2.amazonaws.com` service). 
- 🔄 **Instance Profiles:** You don't attach a Role directly to an EC2 instance; you attach an **Instance Profile**, which acts as a special IAM container carrying the Role. The AWS Console handles this automatically, but you must know the difference for Terraform/CLI work.
- 🛑 **Never Hardcode Keys:** It cannot be overstated: never, ever put `AWS_ACCESS_KEY_ID` inside an EC2 instance configuration file. Always assign an IAM Role.

---

## 💡 Real-World Scenario

> **The Hardcoded Key Hack:** A prominent mobile app company once hardcoded an IAM User's access keys directly into their backend web application running on EC2. A hacker found a vulnerability in the web app, downloaded the configuration file, stole the permanent AWS keys, and pulled the entire customer database from S3. Had the company utilized an **IAM Role for EC2** instead, the hacker would only have found temporary session tokens that expire rapidly, rendering the breach entirely toothless outside of the server environment itself.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
