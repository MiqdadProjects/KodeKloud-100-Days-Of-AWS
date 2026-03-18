<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 16: Create IAM User</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=coqZ9mxEP_E">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Security in AWS starts with Identity and Access Management (IAM). By default, the email address you used to create your AWS account is the **Root User**, holding absolute, unrestricted power to delete the entire account and rack up infinite bills. It is a critical best practice to lock the root user away immediately. 

In this task, you learn how to provision a dedicated **IAM User** with restricted permissions for day-to-day administrative tasks, an essential step in enforcing the principle of least privilege.

---

## 🎯 Key Takeaways & Best Practices

- 🛂 **The Two Keys:** There are two distinct ways for an IAM User to interact with AWS. **Console Access** uses a typical username and password. **Programmatic Access** uses an Access Key ID and Secret Access Key (designed for the AWS CLI, SDKs, or automation scripts).
- 🔐 **Never Share Root:** AWS strongly recommends configuring Multi-Factor Authentication (MFA) on the Root Account, then locking the credentials away in a physical safe, and never using it for daily engineering work.
- 🗂️ **Global Service:** IAM is a **global** service. You don't create users in `us-east-1` or `eu-west-2`. The users and permissions you create apply across all AWS regions seamlessly.
- 🤖 **Enforce Resets:** When creating a user for a teammate, always check the box to require them to create a new password upon their first successful login.

---

## 💡 Real-World Scenario

> **The Root Panic:** A startup founder gave the AWS Root Account credentials to an intern to let them practice launching EC2 instances. The intern was phished online, granting attackers complete root access. Because the attackers logged in as "Root", they deleted the founder's IAM accounts, locked out the entire engineering team, spun up massive crypto-mining servers, and deleted the organization's S3 backups. Had the founder followed best practices and issued the intern a restricted **IAM User** with only "EC2-Launch" permissions, the damage would have been isolated and cheaply reversible.

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
