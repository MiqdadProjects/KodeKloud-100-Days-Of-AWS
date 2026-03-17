<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 45: Configure NAT Gateway for Internet Access in a Private VPC</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=PP4pGQEUa3k">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Allow outbound internet access for essential resources in a private subnet (for updates/patches) while keeping them tightly hidden from unsolicited inbound internet traffic using a NAT Gateway.

---

## 🎯 Key Takeaways & Best Practices

- 🌉 **One-Way Traffic:** NAT Gateways allow private subnets to talk Out to the web, but strictly blocks the web from initiating connections internally.
- 💰 **Cost Considerations:** Managed NAT Gateways incur a baseline hourly charge plus a data processing charge.

---

## 💡 Real-World Scenario

> **Secure OS Patches:** A private backend database server regularly reaches out via the NAT Gateway safely to `apt-get` system security patches.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
