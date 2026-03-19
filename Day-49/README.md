<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 49: Secure SCP Log Transfer and Cron Jobs via Jump Server</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=VEsk18wg3Cw">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Establish a secure mechanism to continuously transfer log files from a Private EC2 instance to a Public Jump Server using strict `ssh-keygen` identities, `scp`, and scheduled `cron` jobs, before uploading to S3.

---

### 🛠️ Hands-On Linux Commands

```bash
# 1) Access the Public EC2 and secure identity
scp -i /root/.ssh/KEY.pem /root/.ssh/KEY.pem ubuntu@PUBLIC_IP:/home/ubuntu/.ssh/KEY.pem
ssh -i /root/.ssh/KEY.pem ubuntu@PUBLIC_IP
chmod 400 /home/ubuntu/.ssh/KEY.pem

# 2) Jump to the Private EC2 and create a dedicated transfer key
ssh -i /home/ubuntu/.ssh/KEY.pem ubuntu@PRIVATE_IP
ssh-keygen -t ed25519 -f ~/.ssh/log_transfer_key -C "log-transfer" -N ""
cat ~/.ssh/log_transfer_key.pub

# 3) Exit back to Public EC2, Authorize the new targeted Key
echo 'ssh-ed25519 PASTE_PUBLIC_KEY_HERE log-transfer' >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# 4) On Private EC2, Set up SCP Cron task (Every Minute)
crontab -e
* * * * * /usr/bin/scp -i /home/ubuntu/.ssh/log_transfer_key -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /var/log/boots.log ubuntu@PUBLIC_IP_INTERNAL:/tmp/boots.log >> ~/scp-transfer.log 2>&1

# 5) On Public EC2, Set up S3 Upload Cron task
sudo apt update && sudo snap install aws-cli --classic
crontab -e
* * * * * /snap/bin/aws s3 cp /tmp/boots.log s3://YOUR_BUCKET/boot/boots.log >> ~/s3-upload.log 2>&1
```

---


## 🎯 Key Takeaways & Best Practices

- 🔑 **Secure File Transfer:** Using `scp` (Secure Copy Protocol) tightly integrates with SSH keys (`ed25519`) to move files across the network completely encrypted.
- ⏱️ **Cron Scheduling:** The Linux `crontab` daemon automates repetitive tasks infinitely (like log uploads) without manual intervention.

---

## 💡 Real-World Scenario

> **Compliance Logging:** Financial audit logs generated deep within a highly secure private database subnet are safely scheduled for extraction to a resilient central S3 bucket nightly.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **SCP (Secure Copy Protocol):** A standardized network protocol, heavily integrated with SSH authentication keys (`ed25519` or `RSA`), used to securely and encrypted-ly transfer computer files between a local host and remote host or between two remote hosts.
- **Cron Jobs:** In Unix-like operating systems, the `crontab` daemon facilitates the rigid scheduling of periodic background jobs (scripts, commands) to execute automatically at exact intervals infinitely.
- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud.
