<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 21: Setting Up an EC2 Instance with an Elastic IP</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=ULkoZZEnBB8">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Hosting a web application requires absolute network stability. If a customer bookmarks your site or your DNS provider points `www.yourcompany.com` to a specific IP address, that address cannot change randomly in the middle of the night.

In this practical, capstone-style task, we synthesize several AWS concepts. You will launch a fresh EC2 instance, deploy a web server, allocate a static **Elastic IP (EIP)**, and bind that permanent public IP address to your server to establish a reliable, unmoving internet endpoint for application hosting.

---

## 🎯 Key Takeaways & Best Practices

- 🏗️ **Architectural Assembly:** Building a public host requires the harmony of 4 core services: EC2 (compute), Security Groups (firewall allowing HTTP 80), IGW (internet gateway routing), and the Elastic IP (static identity).
- 📌 **The Reassignment Trick:** If your specific EC2 instance requires a reboot or replacement due to underlying hardware degradation, you simply spin up a new EC2 instance and reassign the EIP to the new box. The internet remains entirely unaware of the downtime.
- 🪟 **Public DNS Names:** When you assign an EIP to an instance, AWS automatically updates the instance’s Public DNS hostname (e.g., `ec2-54-20-10-5.compute-1.amazonaws.com`) to match the new Elastic address.
- 🌐 **Modern Evolution:** While hosting a single site on an EC2 with an EIP is great for learning and small projects, modern enterprise architectures rarely use raw Elastic IPs for web hosting. Instead, they point their DNS to highly available **Application Load Balancers (ALBs)**.

---

## 💡 Real-World Scenario

> **The Legacy App Migration:** A local government agency needed to migrate a 15-year-old monolithic application into the cloud. The application was notoriously fragile, and hundreds of remote state systems had the application's IPv4 address hardcoded deeply into their codebases instead of using a domain name. By utilizing AWS **Elastic IPs**, the cloud architects could perform a "Lift and Shift" migration to an EC2 instance, map the EIP to mimic the old system, and allow the hardcoded remote systems to connect to the AWS cloud immediately without rewriting any legacy code.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Internet Gateway (IGW):** A highly available, horizontally scaled VPC component that allows communication between instances in your VPC and the open internet.
- **Elastic IPs (EIP):** A static, public IPv4 address designed for dynamic cloud computing. Unlike dynamic IPs that change upon restarts, an EIP remains fixed. If an instance fails, you can rapidly remap the EIP to another healthy instance.
