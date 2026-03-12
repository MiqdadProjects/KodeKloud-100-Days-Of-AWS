<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 03: Create Subnet</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=UStuUoop4WY&t">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

A **Subnet** (sub-network) is a logical subdivision of an AWS Virtual Private Cloud (VPC) that allows you to slice a large network into smaller, manageable chunks. Specifically, subnets map to a single AWS **Availability Zone (AZ)**, tying your cloud resources directly to physical data centers.

In this task, you learn how to carve out an IP address space using CIDR blocks and allocate it to a specific Availability Zone. This is the foundation of network routing, high availability, and resource isolation.

---

## 🎯 Key Takeaways & Best Practices

- 📍 **One AZ per Subnet:** A subnet must live entirely within one Availability Zone. It cannot span multiple AZs, though your VPC spans all AZs in the region.
- 🔢 **CIDR Blocks:** Subnets use CIDR (Classless Inter-Domain Routing) notation to define how many IP addresses it can hold (e.g., a `/24` subnet holds 256 IPs). 
- 🔒 **AWS Reserved IPs:** AWS automatically reserves the **first 4** and **last 1** IP addresses in every subnet for routing, DNS, and broadcast. A `/24` gives you 251 usable IPs, not 256.
- 🛣️ **Public vs. Private:** A subnet isn't inherently "public" or "private" upon creation. It only becomes "public" if its route table has a route `0.0.0.0/0` pointing to an **Internet Gateway (IGW)**.

---

## 💡 Real-World Scenario

> **High Availability Architecture:** In a professional, fault-tolerant web architecture, engineers never rely on a single subnet. They deploy application servers across at least two subnets in two different Availability Zones (e.g., `us-east-1a` and `us-east-1b`). If an unseasonable storm or power failure takes down the `us-east-1a` data center, the Application Load Balancer automatically shifts all traffic to the servers surviving in the `us-east-1b` subnet.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
