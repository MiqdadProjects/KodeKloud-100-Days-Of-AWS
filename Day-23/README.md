<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 23: Data Migration Between S3 Buckets Using AWS CLI</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=SZQ0Glyb0pU">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Clicking through the AWS web console is perfectly adequate for learning, but true cloud engineering happens in the terminal. The **AWS Command Line Interface (CLI)** allows you to script, heavily automate, and rapidly execute API commands against your infrastructure.

In this task, you install the AWS CLI and learn how to wield its high-level S3 commands. You will execute a data migration, rapidly moving datasets from a source S3 bucket to a destination S3 bucket without ever opening a web browser.

---

## 🎯 Key Takeaways & Best Practices

- 🔀 **CP vs SYNC:** The `aws s3 cp` command copies specific files one-by-one. The vastly more powerful `aws s3 sync` command analyzes the source and destination buckets simultaneously, and only transfers the files that are new or updated.
- 🏎️ **Serverless Data Hose:** When you execute an S3 transfer via the CLI, the heavy lifting isn't happening on your computer's internet connection. AWS S3 executes a highly-parallel, backend-to-backend data transfer across their massive fiber-optic backbone in seconds.
- 🗑️ **The Danger of --delete:** Using the command `aws s3 sync s3://source s3://dest --delete` forces the destination bucket to be a perfect mirror of the source. If a file exists in the destination but *not* in the source, the CLI will ruthlessly delete it. Use this flag with extreme caution.
- 🔒 **IAM Permissions:** The IAM User credential running the CLI must be authorized with `s3:GetObject` on the source bucket and `s3:PutObject` on the destination bucket.

---

## 💡 Real-World Scenario

> **The Big Data Migration:** A massive healthcare analytics company needed to migrate 150 Terabytes of raw medical imagery from a badly configured `us-east-1` bucket to a securely encrypted, compliant `us-west-2` bucket. Downloading 150TB to an office server and re-uploading it would take months. By spinning up a powerful EC2 instance internally and running a background `aws s3 sync` command with increased concurrent threads, they moved all 150 Terabytes reliably via AWS's internal network over a single weekend.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
