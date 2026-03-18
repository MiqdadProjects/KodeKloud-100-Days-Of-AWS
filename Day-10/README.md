<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 10: Attach Elastic IP to EC2 Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=CKd9LqGeRlY">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

By default, the Public IPv4 address assigned to a newly launched EC2 instance is highly volatile. If you stop the instance (for maintenance or resizing) and start it back up, AWS returns the old IP to its public pool and assigns your instance a completely new, random public IP address.

An **Elastic IP (EIP)** solves this problem. An EIP is a static, persistent public IPv4 address that belongs to *your account*, not the instance. In this task, you learn how to allocate an EIP and map it securely to a virtual server to provide a permanent public endpoint.

---

## 🎯 Key Takeaways & Best Practices

- 📌 **Static Persistence:** An Elastic IP remains exactly the same even if the EC2 instance it's attached to is stopped or restarted.
- 🔀 **Rapid Failover:** If a primary web server crashes, you can rapidly remap its associated Elastic IP to a backup standby EC2 instance. The internet (and your customers) won't even realize the underlying server hardware was completely swapped out!
- 💸 **The Cost Trap:** AWS charges an hourly penalty fee for Elastic IPs that are *allocated to your account but NOT attached to a running instance*. Always **Release** unused EIPs immediately to avoid ghost charges.
- 📏 **Account Limits:** By default, new AWS accounts are strictly limited to just 5 Elastic IPs per region to prevent the exhaustion of the global IPv4 address space.

---

## 💡 Real-World Scenario

> **The DNS Nightmare:** A small company launched their corporate blog on an EC2 instance without an Elastic IP. They mapped their domain name (`blog.company.com`) to the EC2's default dynamic public IP using an A Record in their DNS hosting. A month later, an administrator restarted the EC2 instance to apply an urgent security patch. The server came back online with a brand new IP address, immediately breaking the blog globally because the domain's DNS was still pointing to a randomly reassigned IP owned by someone else. Attaching an **Elastic IP** entirely prevents this scenario.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Elastic IPs (EIP):** A static, public IPv4 address designed for dynamic cloud computing. Unlike dynamic IPs that change upon restarts, an EIP remains fixed. If an instance fails, you can rapidly remap the EIP to another healthy instance.
