# Day 23 - Data Migration Between S3 Buckets Using AWS CLI

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=SZQ0Glyb0pU)

**Task Summary:**  
In this task, you learn how to migrate data between two Amazon S3 buckets using the AWS CLI. The video covers using the `aws s3 cp` and `aws s3 sync` commands to efficiently transfer objects from a source bucket to a destination bucket, including handling of large datasets. This is a practical skill widely used for bucket reorganization, cross-region replication setup, and disaster recovery.

**What you will learn:**  
- How to use `aws s3 cp` to copy individual objects and `aws s3 sync` to sync entire buckets or prefixes.  
- Key CLI commands:  
  - `aws s3 sync s3://source-bucket s3://destination-bucket`  
  - `aws s3 cp s3://source-bucket/file.txt s3://destination-bucket/file.txt`  
- How to handle permissions and ensure the IAM user/role has `s3:GetObject` on the source and `s3:PutObject` on the destination.  
- Best practice: Use `aws s3 sync` with `--delete` flag carefully — it removes objects in the destination that don't exist in the source.

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
