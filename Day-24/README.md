<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 24: Application Load Balancer for an EC2 Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=dosDF3IUHtg">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

If you point a million users at a single web server, it will instantly crash. To achieve global scale and fault tolerance, you must hide fleets of EC2 instances behind an **Application Load Balancer (ALB)**.

The ALB is a Layer 7 (HTTP/HTTPS) traffic router. It sits between the user and your EC2 backend, inspecting requests, checking instance health, and smartly distributing the web traffic across multiple availability zones. In this task, you assemble the trio of modern scalable infrastructure: a Listener, a Target Group, and the ALB itself.

---

## 🎯 Key Takeaways & Best Practices

- 🗂️ **The ALB Trio:** To make an ALB work, you need a **Listener** (listens on Port 80/443), an **ALB Rule** (If path is `/images`, route to ImageServers), and a **Target Group** (the actual list of EC2 instances accepting the traffic).
- 🩺 **Health Checks:** An ALB continually pings your EC2 instances (e.g., requesting the `index.html` file). If an EC2 fails the ping repeatedly, the ALB identifies it as "Unhealthy" and automatically stops sending users to the broken server until it recovers.
- 🛡️ **The Security Group Shield:** In a production architecture, you never allow the internet (`0.0.0.0/0`) to access your EC2 instances directly. You set the EC2 Security Group to *only* accept Port 80/443 traffic from the **ALB's Security Group ID**, effectively hiding your servers behind an impenetrable shield.
- 🔒 **SSL Termination:** Don't waste EC2 compute cycles decrypting HTTPS traffic. The ALB is designed to hold your SSL/TLS certificates and seamlessly handle the massive mathematical overhead of SSL decryption before passing the raw HTTP request back to your instances.

---

## 💡 Real-World Scenario

> **The Path-Based Routing Trick:** A startup runs an e-commerce monolithic app, but they wanted to build a brand new, ultra-fast backend written in Go specifically for their `/cart` checkout process. Using an **Application Load Balancer**, they created a Listener Rule stating: "If the URL path is `/*`, send traffic to the old Monolith EC2 Target Group. But if the URL path is literally `/cart*`, perfectly route that traffic to the new Go-based EC2 Target Group." This Layer 7 intelligence allowed them to migrate the application piece-by-piece without users ever noticing the switch.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Security Groups:** Act as a stateful, instance-level functional firewall. They evaluate incoming and outgoing traffic at the resource layer, allowing you to selectively open ports like 22 (SSH) or 80 (HTTP).
- **Application Load Balancer (ALB):** Automatically distributes incoming layer-7 application traffic (HTTP/HTTPS) intelligently across multiple target resources, such as EC2 instances, ensuring no single server gets overloaded.
