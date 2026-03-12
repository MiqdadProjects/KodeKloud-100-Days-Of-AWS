<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 30: Enable Internet Access for Private EC2 Using NAT Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=PkPvXAMJUCw">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

In a secure AWS architecture, your application servers and databases live in **Private Subnets**, entirely cut off from the public internet. However, those private servers still need to download OS updates, pull Docker images, and contact third-party APIs (like Stripe or Twilio).

How does a server without a Public IP reach the internet? It uses **Network Address Translation (NAT)**. In this advanced networking task, you manually build a NAT Instance—a specialized EC2 server sitting in a Public Subnet that acts as a secure, outbound-only proxy for your private servers.

---

## 📜 NAT Configuration Commands

To turn a standard Amazon Linux 2 EC2 instance into a functional NAT router, you must execute the following commands to manipulate the Linux kernel and `iptables` firewall:

```bash
# 1. Enable IP forwarding in the Linux kernel
sudo sysctl net.ipv4.ip_forward=1

# 2. Configure IP masquerading to hide the private IPs
sudo /sbin/iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# 3. Install the iptables service to persist rules across reboots
sudo yum install -y iptables-services

# 4. Save the iptables rules and enable the service on boot
sudo service iptables save
sudo systemctl enable iptables

# 5. Verify the iptables rules were applied successfully
sudo iptables -t nat -L -n -v
```

---

## 🎯 Key Takeaways & Best Practices

- 🛑 **Source/Destination Check:** By default, every EC2 instance drops network packets if it isn't the final destination. Because a NAT instance's entire job is to forward packets for *other* servers, you **must disable** the "Source/Destination Check" flag on the NAT EC2 instance network interface in the AWS console.
- 🔀 **The Private Route Table:** You must edit the Private Subnet's Route Table. Add a default route `0.0.0.0/0` and point the target specifically to the `eni-xxxxxx` (Elastic Network Interface) of your NAT EC2 instance.
- 🛡️ **Outbound Only:** The beauty of NAT is that it is strictly a one-way street. Your private servers can initiate connections *out* to the internet to download updates, but hackers on the internet cannot initiate connections *in* through the NAT to attack your private servers.
- 💰 **NAT Gateway vs NAT Instance:** While we built a **NAT Instance** here (which is extremely cheap and great for learning/startups), enterprise production environments strictly use **AWS Managed NAT Gateways**. A NAT Gateway is fully managed by AWS, scales automatically to 45 Gbps, and never requires you to SSH in or run `iptables`.

---

## 💡 Real-World Scenario

> **The Cost-Optimization Hero:** A scrappy startup was horrified to receive a $300/month AWS bill for their development environment. They discovered that AWS charges roughly $32/month just for a Managed NAT Gateway to *exist* idly in an AZ, even if no data is flowing through it. By tearing down the three Managed NAT Gateways in their non-production DEV VPCs and replacing them with three `t3.nano` self-managed **NAT Instances** running the script above, the DevOps intern slashed the company's AWS dev-environment network bill by 90% in an afternoon.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
