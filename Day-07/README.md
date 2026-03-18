<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 07: Change EC2 Instance Type</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=On3gvj7CVNo">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

**Vertical Scaling (Scaling Up/Down)** is a core cloud computing feature. Unlike a physical on-premise data center where adding more RAM or CPU to a server requires scheduling downtime and physically installing hardware, AWS allows you to completely resize a virtual server in minutes via an API call or console click.

In this task, you learn how to identify when an instance is struggling or over-provisioned, and dynamically modify its CPU and Memory configuration by transitioning it to a completely different instance type.

---

## 🎯 Key Takeaways & Best Practices

- 🛑 **Instance State:** You **cannot** change the instance type of a running instance. You must first transition the instance to the *Stopped* state, modify the type, and then Start it again.
- 📉 **Right-Sizing:** If a `c5.xlarge` instance is only using 15% CPU, it is a waste of money. Use CloudWatch metrics to identify "Over-Provisioned" servers and scale them down to save costs immediately.
- 🖧 **Hardware Limitations:** Some heavily modified or older applications may break if moved to radically different CPU architectures (like moving from Intel `x86_64` to ARM `Graviton`). Be cautious when entirely shifting Instance Families.
- ⏳ **IP Change Warning:** Unless your instance has an **Elastic IP** attached, stopping and starting it will result in the instance receiving a completely new Public IPv4 address.

---

## 💡 Real-World Scenario

> **The Spiky Traffic Trap:** Assume you run an e-commerce platform anticipating a massive marketing push on Friday. To survive the surge, you stop your `t3.small` web server on Thursday night, scale it aggressively up to an `m5.4xlarge`, and start it back up. However, leaving it at `m5.4xlarge` forever will bankrupt the project. In the professional world, manual instance type changes are rarely used for traffic spikes; teams instead rely on **Horizontal Scaling** via Auto Scaling Groups to automatically launch *multiple* small servers as needed. Manual resizing is strictly used for baseline right-sizing of long-lived, un-scalable legacy workloads.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Elastic IPs (EIP):** A static, public IPv4 address designed for dynamic cloud computing. Unlike dynamic IPs that change upon restarts, an EIP remains fixed. If an instance fails, you can rapidly remap the EIP to another healthy instance.
- **Amazon CloudWatch:** A monitoring and observability service. It collects operational data in the form of logs, metrics, and events. We use **CloudWatch Alarms** to continually monitor resources and automatically trigger actions when thresholds are breached.
- **Auto Scaling Groups (ASG):** Intelligently and automatically dynamically adjusts the number of EC2 instances serving your application based on actual demand rules and health checks, guaranteeing continuous high availability and dramatically optimized costs.
