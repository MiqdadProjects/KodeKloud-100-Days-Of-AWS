<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 32: RDS Snapshot and Restore</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=xfu6OR96uQ4">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Even a fully managed Amazon RDS cluster relies on underlying EBS storage volumes that can fail, or worse, human administrators who execute catastrophic `DROP TABLE` SQL queries.

In AWS, the definitive data safety net is the **RDS Snapshot**. While AWS provides automated nightly backups out-of-the-box for RDS, taking a manual, on-demand snapshot allows you to capture a permanent, point-in-time copy of your entire database architecture and data. In this task, you learn how to take a snapshot and, crucially, how to rapidly restore that snapshot into a brand-new database instance to recover from disaster.

---

## 🎯 Key Takeaways & Best Practices

- 📸 **Manual vs Automated:** Automated Backups are deleted by AWS the very second you choose to terminate the RDS instance. A **Manual Snapshot** is kept forever in AWS S3 until you explicitly decide to press "Delete" in the console. Always, always take a manual snapshot before shutting down an environment!
- 🏗️ **Restoration Mechanics:** When you restore an RDS snapshot, AWS does **not** overwrite the existing, broken database. It provisions an entirely brand-new database instance with a brand-new hostname endpoint. Your application code will need to be updated to point to the new string.
- ⏸️ **The I/O Suspension:** Taking a manual snapshot of a Single-AZ RDS instance may result in a brief I/O suspension lasting up to a minute (meaning the DB briefly freezes and cannot process queries while the snapshot initiates). For Multi-AZ instances, the snapshot is cleanly taken from the hidden Standby instance, completely eliminating downtime.
- 🔄 **The Developer Sandbox:** Snapshots aren't just for disasters! A brilliant use-case is taking a snapshot of the Production database on Friday night, and restoring it on Monday morning as a "Staging Database" so the QA developers have fresh, real-world data to test against all week.

---

## 💡 Real-World Scenario

> **The Ransomware Reality Check:** A company's junior DBA was phished, giving attackers access to the internal network. The attackers logged into the RDS MySQL database, encrypted the customer tables, and demanded $50,000 in Bitcoin to unlock it. The Lead DBA simply laughed. Because the team had AWS automated backups configured with a 35-day retention window, she navigated to the RDS console, selected the automated backup from exactly 1 hour prior to the attack, clicked "Restore to Point in Time", and had a pristine, unencrypted replica of the database running 15 minutes later. The attackers were locked out, and no ransom was paid.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
