# Day 18 - Create Read-Only IAM Policy for EC2 Console Access

**YouTube Video Link:**  
[Watch the solution here](https://www.youtube.com/watch?v=fwAVCMSFzcM)

**Task Summary:**  
In this task, you learn how to create a custom IAM Policy in AWS that grants read-only access to the EC2 console. Rather than using broad AWS managed policies, a custom policy lets you precisely control which EC2 actions a user can perform. This demonstrates the principle of least privilege — granting only the minimum permissions required to do a job.

**What you will learn:**  
- What an IAM Policy is and how JSON-based policy documents define permissions.  
- How to create a custom inline or managed IAM policy using the AWS Console's visual or JSON editor.  
- How to interpret policy elements: `Effect`, `Action`, `Resource`, and `Sid`.  
- Best practice: Use specific `Action` lists instead of wildcards (e.g., `ec2:*`) to minimize the blast radius of a compromised credential.

**IAM Policy Used:**  

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadOnlyEC2Console",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeSnapshots",
                "ec2:DescribeTags",
                "ec2:GetConsoleOutput",
                "ec2:GetConsoleScreenshot"
            ],
            "Resource": "*"
        }
    ]
}
```

**Policy Breakdown:**  
| Field | Value | Meaning |
|-------|-------|---------|
| `Effect` | `Allow` | Grants the listed actions |
| `Action` | `ec2:Describe*`, `ec2:Get*` | Read-only EC2 describe and get operations |
| `Resource` | `*` | Applies to all EC2 resources |
| `Sid` | `ReadOnlyEC2Console` | A human-readable statement identifier |

**Support the content:**  
If you found this video helpful, please **like**, **subscribe**, and **star** this repository:  
[GitHub Repo Link](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
