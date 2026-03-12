<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 04: Enable Versioning for S3 Bucket</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=bK-EOPipqMs">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Amazon S3 (Simple Storage Service) is an object storage service offering industry-leading durability. However, durable storage doesn't protect against human error. 

By enabling **S3 Versioning**, AWS automatically retains multiple variants of an object within the same bucket. If you accidentally overwrite or delete an important file, versioning allows you to seamlessly "undo" the mistake by restoring the previous version ID. This task walks through enabling this critical data-protection feature.

---

## 🎯 Key Takeaways & Best Practices

- ⏪ **Accidental Deletion Protection:** If you delete a file in a version-enabled bucket, AWS actually inserts a "Delete Marker" over it instead of permanently erasing the data. You can just delete the marker to recover the file.
- 🗂️ **Immutable State:** Once a bucket is version-enabled, it cannot be returned to an "unversioned" state. It can only be "Suspended", leaving existing versions intact while stopping new ones.
- 💰 **Cost Implication:** You pay for every version of a stored object. Uploading a 1GB file five times means you are billed for 5GB of storage.
- MFA **Delete:** For ultra-sensitive buckets, you can combine Versioning with Multi-Factor Authentication (MFA) Delete, requiring a physical hardware token code to permanently delete an object layer.

---

## 💡 Real-World Scenario

> **The Ransomware Defense:** S3 Versioning is a key defense against ransomware that targets object storage. If malicious actors compromise credentials and cryptographically alter all your S3 images or logs (the "overwrite" attack vector), they are actually just creating "Version 2" of the files. The underlying clean, unencrypted "Version 1" data is still sitting right there beneath the surface, waiting to be trivially restored. Combine this with **S3 Object Lock** for true immutability.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
