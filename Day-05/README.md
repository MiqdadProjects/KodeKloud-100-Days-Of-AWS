<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 05: Create GP3 Volume</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=YhCbpobVnfA">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Amazon Elastic Block Store (EBS) provides block-level storage volumes for use with EC2 instances. The **GP3** (General Purpose SSD v3) volume type represents a significant evolution in AWS storage, uncoupling storage capacity from storage performance.

In this task, you learn to provision a GP3 volume. Understanding GP3 is critical for modern AWS cost optimization, as it is cheaper than its predecessor (GP2) while offering higher baseline performance metrics.

---

## 🎯 Key Takeaways & Best Practices

- 📈 **Decoupled Performance:** Unlike older GP2 volumes where performance (IOPS) was tied strictly to the gigabyte size of the drive, GP3 allows you to provision specific IOPS and throughput regardless of volume size.
- ⚡ **Baseline Power:** Every GP3 volume, whether it's 1 GB or 1000 GB, comes with a baseline performance of **3,000 IOPS** and **125 MiB/s throughput** out of the box at no extra charge.
- 💸 **Cost Efficiency:** GP3 volumes are up to **20% cheaper** per GB than GP2.
- 🔄 **Live Modification:** You can change an existing EC2 attached volume from GP2 to GP3 on the fly without instance downtime using the "Modify Volume" command in the Elastic Block Store console.

---

## 💡 Real-World Scenario

> **The Database Trap:** Historically, if engineers needed to handle heavy database web traffic, they often bought massive 2-Terabyte GP2 volumes strictly to get the necessary IOPS to handle the queries—even if their actual data was only 50 GB. They were throwing money away on empty storage just to buy speed. With **GP3**, that same team can provision a cheap 50 GB drive, slider the IOPS dial up to 10,000, and save hundreds of dollars a month on their database tier.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
