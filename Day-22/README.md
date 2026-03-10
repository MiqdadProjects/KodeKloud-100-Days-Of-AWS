# Day 22 - Configuring Secure SSH Access to an EC2 Instance

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=iEP9Dyz_V6U)

**Task Summary:**  
In this task, you learn how to securely configure SSH access to an AWS EC2 instance using a Key Pair and a properly configured Security Group. The video walks through the full connection flow — from setting correct key file permissions to using the `ssh` command to connect — and highlights common mistakes that prevent successful connections. Secure SSH access is a foundational operational skill for managing Linux-based EC2 instances.

**What you will learn:**  
- How to connect to a Linux EC2 instance using SSH with a `.pem` private key file.  
- The correct command format: `ssh -i "key.pem" ec2-user@<public-ip>`.  
- How to fix the "Permissions 0644 for key.pem are too open" error by setting `chmod 400 key.pem`.  
- Best practice: Restrict SSH access in your Security Group to your own IP address only (e.g., `MY_IP/32`) instead of `0.0.0.0/0` to prevent unauthorized access attempts.

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
