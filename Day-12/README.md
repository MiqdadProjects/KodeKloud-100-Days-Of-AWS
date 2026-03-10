# Day 12 - Attach Volume to EC2 Instance

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=dL_hN-BH1OE)

**Task Summary:**  
In this task, you learn how to create an EBS (Elastic Block Store) volume and attach it to a running EC2 instance in AWS. Attaching an additional volume allows you to expand storage capacity without modifying the root volume. The video covers the full workflow from volume creation to attachment and verifying it from within the OS.

**What you will learn:**  
- How to create a new EBS volume in a specific Availability Zone using the AWS Console.  
- How to attach an EBS volume to a running EC2 instance and identify it inside the OS (e.g., as `/dev/xvdf`).  
- Steps to mount and use the new volume on Linux: `lsblk`, `mkfs`, `mount`.  
- Best practice: Always create the EBS volume in the same Availability Zone as your EC2 instance — volumes cannot be attached across AZs.

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
