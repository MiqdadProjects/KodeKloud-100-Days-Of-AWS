<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 02: Create Security Group</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=oKdO60QNFlQ&t">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

A **Security Group** acts as a virtual, stateful firewall for your AWS EC2 instances, controlling both incoming (inbound) and outgoing (outbound) traffic on a port-by-port, IP-by-IP basis. 

If Key Pairs are the lock on the door, Security Groups are the high concrete wall surrounding the entire perimeter. Misconfiguring them is one of the leading causes of cloud data breaches. In this task, you learn how to secure an instance by allowing only the exact traffic needed to function.

---

## 🎯 Key Takeaways & Best Practices

- 🛡️ **Stateful by Design:** If you allow an incoming request (like SSH on Port 22), the response traffic is automatically allowed out, regardless of outbound rules.
- 🚷 **Default Deny:** By default, a new Security Group denies *all* inbound traffic, but allows *all* outbound traffic. You must explicitly add inbound rules.
- 🎯 **Principle of Least Privilege:** Never use `0.0.0.0/0` (everyone) for SSH (Port 22). Always restrict administrative ports to your specific static IP address or an internal corporate VPN IP block.
- 🌐 **Common Web Ports:** To host a public website, you will need to open Port 80 for `HTTP` and Port 443 for `HTTPS` to the world (`0.0.0.0/0` for IPv4 and `::/0` for IPv6).

---

## 💡 Real-World Scenario

> **The Ransomware Reality:** A widespread mistake in cloud deployments is leaving databases (like MySQL on Port 3306 or Redis on 6379) open to `0.0.0.0/0`. Attackers run automated internet-wide scanners specifically looking for exposed databases. Within hours of misconfiguring this rule, bots will attempt to brute-force the password or drop ransomware. **Never expose databases to the public web** — restrict their Security Group inbound rules to only accept traffic from the Web Server's Security Group ID.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **Amazon EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows. It is the backbone of compute on AWS.
- **Security Groups:** Act as a stateful, instance-level functional firewall. They evaluate incoming and outgoing traffic at the resource layer, allowing you to selectively open ports like 22 (SSH) or 80 (HTTP).
