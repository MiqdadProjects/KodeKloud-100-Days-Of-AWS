<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 09: Enable Termination Protection for EC2 Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=rPQwA2W5mC8">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Terminating an EC2 instance is irreversible. The moment it occurs, AWS securely scrubs the physical host memory and permanently deletes the attached root Elastic Block Store (EBS) volume (by default), vaporizing your data. 

**Termination Protection** is the ultimate safety net for your most critical digital assets. By enabling it, an instance simply cannot be destroyed via the console, CLI, or API without an administrator first deliberately unchecking a security box. In this task, you learn to deploy this essential fail-safe layer.

---

## 🎯 Key Takeaways & Best Practices

- 🔒 **Data Lifesaver:** When enabled, the AWS console "Terminate Instance" button is greyed out or fails with an error, preventing accidental catastrophic data loss.
- ⚙️ **The "Delete on Termination" Trap:** By default, when an EC2 instance is terminated, the root EBS volume attached to it is automatically destroyed too. If you haven't taken a snapshot, the OS and data are gone forever.
- 📉 **Spot Instances Exception:** Termination protection does **not** stop Amazon from terminating Spot Instances when the spot price spikes or capacity is reclaimed. Spot instances are ephemeral by nature.
- 🤖 **Auto Scaling Considerations:** If an instance is part of an Auto Scaling Group, the ASG *can* still terminate instances to scale down or replace unhealthy nodes, even if termination protection is on. Rely on ASG Scale-In Protection for those workloads instead.

---

## 💡 Real-World Scenario

> **The API Key Leak:** An employee at a startup accidentally committed a highly privileged AWS Access Key to a public GitHub repository. Within 120 seconds, automated malicious bots found the key, logged in, and attempted to delete all existing infrastructure before spinning up Crypto-mining EC2 instances. Because the startup had enforced **Termination Protection** on their core database server, the bots' API requests to delete the database were rejected by AWS. This simple checkbox bought the team the crucial time needed to revoke the compromised IAM key and save the company.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **EBS Snapshots:** Point-in-time incremental backups of an EBS volume stored securely in S3. They allow you to instantly restore a hard drive exactly as it was when the backup was taken.
- **AWS IAM (Identity and Access Management):** A foundational service enabling you to securely manage access to AWS resources. You create Users (people), Groups, Roles (temporary service permissions), and govern access using JSON Policies.
- **Auto Scaling Groups (ASG):** Intelligently and automatically dynamically adjusts the number of EC2 instances serving your application based on actual demand rules and health checks, guaranteeing continuous high availability and dramatically optimized costs.
