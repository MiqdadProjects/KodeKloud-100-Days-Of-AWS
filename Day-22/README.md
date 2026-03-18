<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 22: Configuring Secure SSH Access to an EC2 Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=iEP9Dyz_V6U">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

To manage a Linux EC2 instance, you must remotely access its terminal. Secure Shell (SSH) is the cryptographic network protocol used to safely execute CLI commands over an unsecured network like the public internet. 

Without understanding how to properly wield your `.pem` key pair, manage local file permissions, and format the SSH connect string, you will inevitably find yourself locked out of your own infrastructure. This task covers the vital operational steps to securely log into your cloud server.

---

## 🎯 Key Takeaways & Best Practices

- 💻 **The Connection String:** The standard format to connect from a Mac/Linux terminal is `ssh -i "MyKeyPair.pem" ec2-user@<public-ip-address>`.
- 🛑 **The Permissions Error:** The most common AWS beginner mistake is encountering the `Permissions 0644 for MyKeyPair.pem are too open` error. By design, SSH refuses to use a private key if other users on your local computer can read it. You **must** run `chmod 400 MyKeyPair.pem` (read-only for owner) to fix this.
- 👤 **The Default Usernames:** You don't log in as `root`. You must log in as the default user created by the AMI builder. For Amazon Linux it's `ec2-user`, for Ubuntu it's `ubuntu`, and for CentOS it's `centos`.
- 🚫 **Ban the 0.0.0.0/0:** Never leave port 22 open to the entire world in your Security Group. Within minutes of launching, automated bots will begin brutalizing your server with dictionary password attacks. Restrict SSH access to "My IP" only.

---

## 💡 Real-World Scenario

> **The Evolving Industry Standard:** While mastering SSH and Key Pairs is a mandatory rite of passage in cloud computing, modern enterprises are actually moving away from SSH entirely. Managing, rotating, and distributing physical `.pem` files to 500 developers is a massive security liability. Today, security-conscious teams use **AWS Systems Manager (SSM) Session Manager**, which establishes a secure terminal connection via the AWS Console entirely through your IAM identity—meaning no open inbound ports (no Port 22 required at all) and no physical key files are needed!

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **AWS Key Pairs:** AWS uses public-key cryptography to secure the login information for your instance. The public key is safely stored by AWS, and you keep the private key (`.pem` or `.ppk`) to authenticate via SSH.
- **Security Groups:** Act as a stateful, instance-level functional firewall. They evaluate incoming and outgoing traffic at the resource layer, allowing you to selectively open ports like 22 (SSH) or 80 (HTTP).
- **AMIs (Amazon Machine Images):** A master template for your EC2 instances. It contains the OS configuration, application server, and necessary startup applications.
- **AWS IAM (Identity and Access Management):** A foundational service enabling you to securely manage access to AWS resources. You create Users (people), Groups, Roles (temporary service permissions), and govern access using JSON Policies.
