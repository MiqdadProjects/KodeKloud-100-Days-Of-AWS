# Day 15 - Create Volume Snapshot

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=ME7TKp77rQ4)

**Task Summary:**  
In this task, you learn how to create a snapshot of an EBS volume in AWS, which is a point-in-time backup stored durably in Amazon S3. Snapshots are incremental — only the data that has changed since the last snapshot is saved — making them both cost-effective and fast. This is a core data protection and disaster recovery technique for AWS workloads.

**What you will learn:**  
- What an EBS snapshot is and how incremental snapshots work to save storage costs.  
- How to create a volume snapshot from the AWS Console (EC2 → Volumes → Create Snapshot).  
- How to restore a new EBS volume from an existing snapshot for data recovery.  
- Best practice: Automate snapshot creation using **Amazon Data Lifecycle Manager (DLM)** policies to ensure regular, consistent backups without manual effort.

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
