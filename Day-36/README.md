<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 36: Load Balancing EC2 Instances with Application Load Balancer</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=lBxcfef1748">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Distribute incoming HTTP traffic across multiple EC2 instances using an Application Load Balancer to ensure high availability and structural redundancy.

---

### 🛠️ User Data Script

```bash
#!/bin/bash
apt-get update -y
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
```

---


## 🎯 Key Takeaways & Best Practices

- ⚖️ **Dynamic Load Balancing:** ALBs route Layer 7 (HTTP/HTTPS) traffic smartly based on path and host rules.
- 🏥 **Health Checks:** The ALB autonomously detects instance failures and stops routing traffic to bad nodes.

---

## 💡 Real-World Scenario

> **Traffic Surges:** A viral news site stays online because the ALB evenly spreads the massive flood of web requests across numerous backend web servers.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
