<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 50: Resize EC2 EBS Volume on the Fly (Growpart)</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=nUJUjftQ1pg">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Increase the storage capacity of an actively running EC2 instance by resizing its attached Elastic Block Store (EBS) volume, then safely extending the Linux `xfs` filesystem partition using `growpart`.

---

### 🛠️ Hands-On Volume Commands

```bash
# 1. Confirm volume block size (e.g. shows 12G)
lsblk

# 2. Grow the partition on the physical drive
sudo growpart /dev/xvda 1

# 3. Expand the XFS filesystem to recognize the new blocks
sudo xfs_growfs /

# 4. Verify completion
df -h /
```

---


## 🎯 Key Takeaways & Best Practices

- 📈 **Zero Downtime Resize:** Modern AWS EBS allows increasing volume storage capacity on the fly while the instance remains entirely running and serving traffic.
- 💾 **Filesystem Extension:** Modifying hardware storage isn't enough; you must explicitly expand the OS partition (`growpart`) and filesystem (`xfs_growfs` / `resize2fs`) to recognize the new block size.

---

## 💡 Real-World Scenario

> **Database Nearing Capacity:** A production database warns that its `/var/lib/mysql` drive is at 98% utilization. The engineer scales the EBS drive from 10GB to 50GB and resizes the partition instantly during peak hours without crashing the app.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud.
- **Amazon EBS (Elastic Block Store):** High-performance block level storage volumes attached over the network specifically for use with EC2 instances. It can be dynamically resized entirely on the fly to accommodate scaling data limits.
