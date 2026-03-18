<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 25: Setting Up an EC2 Instance and CloudWatch Alarm</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=pUEtwLQE5ZI">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

You cannot manage what you do not measure. In AWS, **Amazon CloudWatch** is the native nervous system that continuously monitors the health and performance of your infrastructure.

In this task, you learn how to actively monitor an EC2 instance's CPU utilization and create a **CloudWatch Alarm**. This alarm acts as an automated tripwire, designed to alert you via email (or trigger automated scaling events) the second a server's performance metrics breach a dangerous threshold.

---

## 🎯 Key Takeaways & Best Practices

- 📊 **Standard vs Detailed:** By default, EC2 instances send metrics to CloudWatch every **5 minutes** (Standard Monitoring, free). If you enable Detailed Monitoring, metrics are sent every **1 minute** (charges apply), which is crucial for production auto-scaling.
- 🔔 **The Alarm States:** A CloudWatch Alarm is always existing in one of three states: `OK`, `ALARM`, or `INSUFFICIENT_DATA`. 
- 📢 **SNS Integration:** An alarm by itself is silent. You must connect the CloudWatch Alarm's "action" to an **Amazon SNS (Simple Notification Service)** topic to actually send an email or SMS text to your phone when the threshold breaks.
- 🧠 **Missing Metrics:** Out-of-the-box, CloudWatch can only see "Hypervisor Level" metrics like CPU, Network, and Disk I/O. It **cannot** see internal OS metrics like "Available RAM" or "Disk Space Used" unless you manually install the CloudWatch Agent inside the EC2 instance.

---

## 💡 Real-World Scenario

> **The Silent Memory Crash:** A junior developer set up a robust CloudWatch CPU alarm at 85% for an EC2 backend server. However, the server kept crashing silently in the middle of the night without the alarm ever triggering. Why? The Python application suffered from a severe memory leak, consuming 100% of the RAM without ever heavily utilizing the CPU. Because RAM is an "OS-level" metric invisible to standard CloudWatch, the CPU alarm never noticed the crisis. The developer learned the hard way to install the **CloudWatch Agent** to track the critical `mem_used_percent` metric and build alarms around that.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Amazon CloudWatch:** A monitoring and observability service. It collects operational data in the form of logs, metrics, and events. We use **CloudWatch Alarms** to continually monitor resources and automatically trigger actions when thresholds are breached.
