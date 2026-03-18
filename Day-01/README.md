<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 01: Create EC2 Key Pair</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=v8p7aZbGQ-4">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Authentication is the first line of defense in cloud security. In this task, you learn how to create and manage an **EC2 Key Pair**, the cryptographic key mechanism AWS uses to securely prove your identity when connecting to an EC2 instance via SSH. 

Without a secure key pair, launching a Linux server in the cloud is like building a vault but leaving the door wide open. 

---

## 🎯 Key Takeaways & Best Practices

- 🔑 **Asymmetric Cryptography:** AWS relies on public-key cryptography. AWS stores the **public key** on the instance, while you safely hold the **private key** (`.pem` or `.ppk`).
- 🛡️ **Zero Recovery:** AWS does **not** keep a copy of your private key. If you lose it after downloading, you lose access to the instance permanently.
- 🪟 **Format Matters:** Download as `.pem` for OpenSSH (macOS/Linux/modern Windows) or `.ppk` if you prefer using PuTTY.
- 🔒 **Permissions are Crucial:** Your private key file must be heavily restricted. On Linux/Mac, always run `chmod 400 keypair.pem` to ensure only the owner can read it, or AWS will reject the connection outright.

---

## 💡 Real-World Scenario

> **The "Lost Key" Incident:** In enterprise environments, losing access to an EC2 instance because a developer lost the `.pem` file is a surprisingly common disaster. To avoid this, modern teams often use **AWS Systems Manager (SSM) Session Manager** instead of SSH keys, which allows secure shell access via IAM roles without managing physical key files at all!

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **AWS Key Pairs:** AWS uses public-key cryptography to secure the login information for your instance. The public key is safely stored by AWS, and you keep the private key (`.pem` or `.ppk`) to authenticate via SSH.
- **AWS IAM (Identity and Access Management):** A foundational service enabling you to securely manage access to AWS resources. You create Users (people), Groups, Roles (temporary service permissions), and govern access using JSON Policies.
