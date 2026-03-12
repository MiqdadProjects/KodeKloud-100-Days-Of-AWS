<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 26: Configure EC2 as Web Server with Nginx</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=hIcVEcykDzA">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Clicking "Launch EC2" gives you a blank operating system, not a web server. To host a website, you need web server software like Nginx or Apache.

In this task, instead of manually logging into the server via SSH and typing installation commands one-by-one, you learn the art of **EC2 User Data**. User Data allows you to inject a bash script into the EC2 instance during its very first boot cycle, automatically installing and configuring Nginx before you even login.

---

## 📜 User Data Automation Script

In the tutorial, we inject this vital bash script during the instance configuration:

```bash
#!/bin/bash
sudo apt-get update -y
sudo apt-get install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

---

## 🎯 Key Takeaways & Best Practices

- 🤖 **Root Execution:** User Data scripts run natively as the `root` user. You actually do not need the `sudo` prefix for the bash commands inside the script, though leaving them in won't hurt.
- ⏱️ **Run Once Only:** The User Data script is executed exactly **once**—at the end of the very first boot cycle. If you stop and restart the EC2 instance the next day, the script will *not* run again.
- 🕵️ **Debugging Logs:** If your server boots up but Nginx isn't running, you don't need to guess why. You can read the exact output and errors of your User Data script by SSH'ing in and checking the log file located at `/var/log/cloud-init-output.log`.
- 🌐 **Security Group Blockage:** Your Nginx server might be running perfectly, but if your EC2 Security Group does not explicitly contain an Inbound Rule allowing **Port 80 (HTTP)** from `0.0.0.0/0`, your web browser will just endlessly load until it times out.

---

## 💡 Real-World Scenario

> **The Auto-Scaling Illusion:** A novice team wanted to use an Auto Scaling Group (ASG) to handle highly variable website traffic. Their plan was to have the ASG launch blank Amazon Linux EC2 instances, and then an engineer would quickly SSH in and manually install the Node.js website code every time a server spun up. This defeated the entire purpose of automation—traffic spiked in seconds, not minutes! By heavily utilizing **EC2 User Data scripts** (or custom AMIs), they ensured that the ASG could autonomously launch, configure, and serve traffic from a new EC2 instance in 90 seconds flat, with absolutely zero human intervention.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
