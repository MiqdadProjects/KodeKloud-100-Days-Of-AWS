<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 15: Create Volume Snapshot</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=ME7TKp77rQ4">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

You never appreciate backups until the catastrophic moment you realize you don't have one. In AWS, the gold standard for block storage backup is an **EBS Snapshot**. 

Snapshots capture the state of your Elastic Block Store (EBS) volume incrementally and store that data highly durably in Amazon S3 hidden behind the scenes. In this task, you learn how to manually trigger a snapshot backup, which is a critical disaster recovery operations skill for any systems administrator.

---

## 🎯 Key Takeaways & Best Practices

- 📈 **Incremental Magic:** EBS Snapshots are incremental. The first snapshot is a slow, full copy. But the second snapshot only copies the tiny data blocks that changed since the first one. This heavily optimizes storage costs and speed.
- 🕰️ **Point-In-Time Restoration:** A snapshot is asynchronous. You can trigger it and immediately use your volume normally. If your database corrupts tomorrow, you can create a brand new EBS volume restoring exactly from today's snapshot.
- 🔄 **AZ Migration Trick:** Unlike an EBS Volume (which is permanently locked to a single Availability Zone like `us-east-1a`), a Snapshot is tied to the whole Region. You can create a snapshot in AZ-A, and restore it into a new volume sitting in AZ-B!
- 🤖 **Data Lifecycle Manager:** Instead of manually clicking "Create Snapshot", mature organizations utilize **Amazon DLM (Data Lifecycle Manager)** to schedule automated nightly or hourly backups.

---

## 💡 Real-World Scenario

> **The Corrupted Update Recovery:** A senior systems administrator accidentally executed a poorly tested database migration script that irreversibly dropped crucial production tables on the master MySQL server. Panic ensued as the website went down. Fortunately, the team had an automated process taking hourly **EBS Snapshots**. The administrator simply stopped the server, detached the corrupted volume, restored a brand new volume from the snapshot taken 15 minutes prior, attached it, and rebooted. While 15 minutes of user data was lost, the business was entirely saved from total collapse.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
