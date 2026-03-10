# Day 14 - Terminate EC2 Instance

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=nNOIw0O-SXA)

**Task Summary:**  
In this task, you learn how to safely terminate an EC2 instance in AWS, which permanently deletes the instance and (by default) its root EBS volume. The video walks through the termination process via the AWS Console and explains the difference between stopping and terminating an instance. Understanding this distinction is critical to avoid unintended data loss in production environments.

**What you will learn:**  
- The key difference between **stopping** (temporary shutdown) and **terminating** (permanent deletion) an EC2 instance.  
- How to terminate an EC2 instance via the AWS Management Console.  
- What happens to attached EBS volumes, Elastic IPs, and ENIs upon termination.  
- Best practice: Enable Termination Protection (Day 09) on production instances and always take an AMI snapshot (Day 13) before terminating important instances.

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
