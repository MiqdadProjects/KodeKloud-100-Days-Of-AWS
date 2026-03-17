<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 40: Troubleshooting Internet Accessibility for an EC2-Hosted Application</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=mUPTItE4xHk">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Diagnose and fix common connectivity issues such as Security Group rules, Network ACLs, and Internet Gateway misconfigurations when an EC2 web application is unreachable.

---

## 🎯 Key Takeaways & Best Practices

- 🔍 **Methodical Debugging:** Check Security Groups strictly for the right ports, and ensure Subnets have route-table access to an IGW.
- 🚪 **Stateful vs Stateless:** Security groups are stateful (auto-allow return traffic); NACLs are stateless (both directions must be permitted).

---

## 💡 Real-World Scenario

> **The Midnight Outage:** An on-call engineer quickly determines that a mistakenly deleted Internet Gateway route broke the main production application.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
