# Day 24 - Setting Up an Application Load Balancer for an EC2 Instance

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=dosDF3IUHtg)

**Task Summary:**  
In this task, you learn how to set up an Application Load Balancer (ALB) in AWS and route HTTP traffic to an EC2 instance through a Target Group. The video walks through creating the ALB, configuring a listener on port 80, registering the EC2 instance in a Target Group, and verifying that traffic reaches the instance via the ALB DNS name. ALBs are essential for building scalable, fault-tolerant web applications on AWS.

**What you will learn:**  
- What an Application Load Balancer (ALB) is and how it differs from a Classic or Network Load Balancer.  
- Key components of an ALB setup: **Listener** (port 80/443), **Target Group** (registered EC2 instances), and **Health Checks**.  
- How to create and configure an ALB and Target Group via the AWS Console step-by-step.  
- Best practice: Always use an ALB in front of your EC2 instances instead of exposing them directly — it enables path-based routing, SSL termination, and seamless auto-scaling integration.

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
