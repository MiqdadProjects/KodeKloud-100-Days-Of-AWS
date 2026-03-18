<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 35: Deploy App with EC2 and Private RDS (MySQL)</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=MWMS8ryCzQ8">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Set up a highly secure two-tier architecture by placing the web server (EC2) in a public subnet and the database (RDS) securely in a private subnet.

---

## 🎯 Key Takeaways & Best Practices

- 🛡️ **Private Subnets:** Placing RDS databases in private subnets strictly prevents direct attacks from the internet.
- 🌐 **Two-Tier Architecture:** Properly separating the frontend and backend layers enhances reliability and security.

---

## 💡 Real-World Scenario

> **E-Commerce Storefront:** Web applications face the public user base, but user-data and financial transactions are kept safely entirely offline in a Private RDS cluster.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Subnets:** A logically isolated sub-section of a VPC. A **Public Subnet** has a direct route to the Internet via an Internet Gateway, while a **Private Subnet** has no direct Internet access, keeping resources highly secure.
- **Amazon RDS (Relational Database Service):** A robust managed service that makes it remarkably easy to set up, operate, and effortlessly scale a relational database (like MySQL, PostgreSQL) in the cloud.
