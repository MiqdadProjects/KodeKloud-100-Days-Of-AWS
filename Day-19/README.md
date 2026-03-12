<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 19: Attach IAM Policy to IAM User</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=u8AWmV9D2Is">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Having IAM Users and isolated JSON IAM Policies is useless until you connect them. Policy Attachment is the mechanism that binds a set of permissions directly to an identity (a User, Group, or Role), thereby granting them the authority to execute AWS API calls.

In this task, you walk through the AWS IAM Console to securely attach an AWS Managed Policy (like `AmazonEC2ReadOnlyAccess`) or a custom-built Customer Managed Policy directly to a specific IAM User.

---

## 🎯 Key Takeaways & Best Practices

- 🔗 **Direct User Attachment:** While attaching policies directly to a user is fast and easy in the console, it is heavily frowned upon in enterprise environments. It leads to "permission sprawl"—a nightmare where 100 developers have 100 uniquely mixed permission sets that are impossible to audit.
- 🏢 **The Enterprise Way:** Always attach policies to **IAM Groups** (e.g., `DevTeamA`) and place the IAM Users into those groups. If a direct user attachment is ever used, it should be highly temporary (e.g., granting a 1-hour emergency debug permission).
- AWS **Managed vs Customer Managed:** AWS provides hundreds of pre-built "Managed" policies (denoted by a little AWS icon). While convenient, they are often dangerously broad. When possible, write precise "Customer Managed" policies.
- 🧮 **Evaluation Logic:** If an identity has 5 policies attached that grant access, but just **1** attached policy explicitly denies access, the Deny unconditionally wins the evaluation.

---

## 💡 Real-World Scenario

> **The Audit Nightmare:** An intern at an agency was directly assigned the `AdministratorAccess` policy to help fix a weekend deployment issue. After the weekend, everyone forgot to remove the policy. Six months later, a disgruntled ex-employee logged into that lingering intern account and deleted production databases. Because the team didn't use **IAM Groups** to standardize their access, the direct policy attachment slipped past entirely unnoticed during routine permission audits.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
