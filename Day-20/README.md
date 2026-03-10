# Day 20 - Create IAM Role for EC2 with Policy Attachment

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=DpGBRUtfzn0)

**Task Summary:**  
In this task, you learn how to create an IAM Role in AWS and attach a policy to it, then associate the role with an EC2 instance. IAM Roles allow AWS services (like EC2) to assume permissions without needing long-term credentials such as access keys. This is the recommended and most secure way to grant AWS service-to-service access.

**What you will learn:**  
- What an IAM Role is and how it differs from an IAM User (no long-term credentials; uses temporary STS tokens).  
- How to create an IAM Role with EC2 as the trusted entity and attach a policy (e.g., `AmazonS3ReadOnlyAccess`).  
- How to attach an IAM Role to an EC2 instance (Instance Profile) via the AWS Console.  
- Best practice: Never hardcode AWS Access Keys inside EC2 instances — always use IAM Roles with Instance Profiles to securely grant permissions to EC2 workloads.

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
