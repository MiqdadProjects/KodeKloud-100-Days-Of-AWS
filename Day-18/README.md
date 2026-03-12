<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 18: Create Read-Only IAM Policy for EC2 Console</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=fwAVCMSFzcM">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Policies are the brains of AWS security. They are rigidly formatted JSON documents defining precisely what API actions are permitted or denied against specific resources. While AWS provides hundreds of "AWS Managed Policies" out of the box, real-world security requires high precision granularity.

In this task, you learn how to craft a **Customer Managed Policy** granting exactly the minimum permissions an auditor or junior developer needs: the ability to *view* the EC2 console and server configurations without the destructive power to terminate, stop, or modify them.

---

## 📜 Custom Policy JSON

In the tutorial, we create this highly-targeted JSON policy document.

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

### 🧩 Policy Anatomy Breakdown

Understanding this JSON is mandatory for the AWS Certified Solutions Architect exams:
| Policy Field | Expected Value | Real-World Translation |
|--------------|----------------|------------------------|
| `Version` | `2012-10-17` | The current syntax rules engine used by AWS. Always leave this as `2012-10-17`. |
| `Statement` | `[...]` | An array that holds one or more individual rules (allow/deny blocks). |
| `Sid` | `ReadOnlyEC2Console` | The "Statement ID". An optional, human-readable label you invent for readability. |
| `Effect` | `Allow` | The verdict. Can strictly be either `Allow` or `Deny`. |
| `Action` | `ec2:Describe*`, etc. | The exact API calls permitted. Notice the prefix `ec2:` defining the parent service. |
| `Resource` | `*` | The targets of the action. `*` means "allow all EC2 resources in the account". |

---

## 🎯 Key Takeaways & Best Practices

- 🚷 **Implicit Deny:** In IAM logic, if an action isn't explicitly defined as an `Allow` in a policy, a user's request will be immediately blocked. AWS defaults to "trust no one."
- 🛡️ **Explicit Deny Override:** If one policy grants `Allow` and an overlapping policy explicitly grants `Deny`, the **Deny always wins**. This is used to create unbreachable security boundaries.
- 🎯 **Avoid Wildcards:** While using `"Action": "ec2:*"` is tempting, it fundamentally violates the Principle of Least Privilege by giving away immense destructive power. Take the time to identify only the precise `Describe` or `Get` actions needed.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
