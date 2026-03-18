<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 06: Launch EC2 Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=RX1CnLWS6nc">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Amazon Elastic Compute Cloud (EC2) is the heart of AWS compute. Mastering how to deploy an EC2 instance efficiently is the defining skill of a cloud engineer. 

In this task, we bring all previous foundational components together—mixing AMIs (Operating Systems), Instance Types (CPU/RAM sizing), Key Pairs (Security), Security Groups (Firewalls), and VPC Subnets (Networking) to launch a fully functioning virtual server in the cloud.

---

## 🎯 Key Takeaways & Best Practices

- 🖥️ **AMI Selection:** The Amazon Machine Image decides the operating system. **Amazon Linux 2023** is heavily optimized for AWS environments and includes the AWS CLI pre-installed.
- ⚖️ **Instance Sizing:** Sizes like `t2.micro` or `t3.micro` dictate compute power. The letters indicate the instance *family* (`t` for general burstable, `c` for compute-heavy, `m` for memory) and the word dictates the size `micro, small, large`.
- 💵 **Free Tier Awareness:** To avoid unexpected bills while learning, strictly stick to instances labeled **Free Tier Eligible** (typically `t2.micro` or `t3.micro` depending on region).
- 🔄 **Ephemeral Nature:** By default, EC2 public IPv4 addresses change if you stop and start the server. Never rely on the default public IP for permanent DNS mapping. 

---

## 💡 Real-World Scenario

> **Compute Sizing Mistakes:** Junior engineers often launch overly large instances (like `m5.2xlarge`) just "to be safe," burning through budget rapidly when the CPU sits at 2% utilization. Cloud-native architecture embraces the concept of **horizontal scaling**: launching many tiny, cheap instances (like `t3.small`) handled by an Auto Scaling Group, rather than one giant, expensive instance. Always design around small, predictable compute blocks.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Amazon VPC (Virtual Private Cloud):** A logically isolated virtual network defined by you. It is the foundational networking layer where you launch AWS resources safely.
- **AMIs (Amazon Machine Images):** A master template for your EC2 instances. It contains the OS configuration, application server, and necessary startup applications.
- **Auto Scaling Groups (ASG):** Intelligently and automatically dynamically adjusts the number of EC2 instances serving your application based on actual demand rules and health checks, guaranteeing continuous high availability and dramatically optimized costs.
