<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 44: Implementing Auto Scaling for High Availability in AWS</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=DRoWmAzOMBw">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Leverage Auto Scaling Groups (ASG) combined with a Load Balancer to dynamically expand or reduce the number of EC2 instances based on traffic spikes.

---

### 🛠️ User Data Script

```bash
#!/bin/bash
dnf update -y
dnf install -y nginx
systemctl start nginx
systemctl enable nginx
```

---


## 🎯 Key Takeaways & Best Practices

- 📈 **ElasticITY:** Instantly match computing capacity strictly to the demand curve using Target Tracking scaling policies.
- 🎯 **Launch Templates:** Centralize instance configurations (AMI, Type, KeyPair, Security groups) perfectly for ASG usage.

---

## 💡 Real-World Scenario

> **Black Friday Scaling:** Your website flawlessly scales out ahead of a major sale event to handle millions of shoppers, and dramatically scales-in afterward to save massive costs.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
