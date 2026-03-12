<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 13: Create AMI from EC2 Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=tSLQx_HeRlg">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

An **Amazon Machine Image (AMI)** acts as the foundational blueprint for launching identical EC2 instances. While AWS provides public AMIs (like Amazon Linux 2023 or Ubuntu 22.04), professional teams create custom, pre-configured AMIs. 

In this task, you learn how to take a running, fully-configured EC2 instance—complete with installed software, security hardening, and custom files—and immortalize it as a private AMI. This process, known as "Baking an AMI," is central to reducing server boot times and creating highly scalable cloud infrastructure.

---

## 🎯 Key Takeaways & Best Practices

- 🍞 **Golden Images:** A "Golden AMI" is an industry term for a highly secure, pre-configured OS template that an entire enterprise agrees to use as their baseline for all new servers.
- 🛑 **No Reboot vs Reboot:** When creating an AMI via the console, AWS strongly recommends a brief reboot. This ensures the operating system flushes cached memory to the disk, guaranteeing the snapshot captures a completely consistent, uncorrupted state.
- 📸 **EBS Snapshots Unseen:** Behind the scenes, creating an AMI automatically triggers an EBS Snapshot of the attached volumes. You pay for the storage of these underlying snapshots!
- 🌍 **Region Bound:** AMIs are heavily restricted to the AWS Region they were created in. If you bake an AMI in `us-east-1` (N. Virginia), you cannot simply launch it in `eu-west-1` (Ireland) without explicitly copying the AMI there first.

---

## 💡 Real-World Scenario

> **The Auto Scaling Lifesaver:** A digital news platform anticipates millions of visitors hitting their site during a major breaking news event. They use an Amazon Auto Scaling Group to automatically launch 50 new web servers. If their servers booted from a standard Ubuntu AMI, each instance would spend 10 minutes downloading Apache, PHP, and cloning the website repository via `apt-get`—meaning the site would crash before the scaling finished. By pre-baking a custom **AMI** containing all the necessary code and software, those 50 instances boot up and serve live traffic in under 60 seconds.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
