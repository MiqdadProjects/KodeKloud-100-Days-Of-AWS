<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 17: Create IAM Group</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=EV5wSSqRQpo">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Imagine clicking hundreds of checkboxes to grant 50 individual developers identical permissions to read from an S3 bucket—and doing it again when they change teams. This is an administrative nightmare.

**IAM Groups** solve this exact problem. Groups are logical collections of IAM Users. By attaching permission policies directly to the group instead of the user, any user added to the group automatically inherits those permissions. In this task, you learn the enterprise-standard method for scaling secure access control.

---

## 🎯 Key Takeaways & Best Practices

- 🗂️ **Identity, not Policy:** An IAM Group is not an identity in itself. It is merely a container for users. Furthermore, an IAM Group **cannot** be assigned as a "Principal" in resource-based policies (like an S3 Bucket Policy).
- 🎯 **Role-Based Engineering:** Mature AWS environments structure groups strictly by business roles. Examples include `DatabaseAdmins`, `JuniorDevs`, `DataAnalysts`, and `BillingTeam`.
- 🔐 **Zero To Hero:** An IAM User can belong to multiple IAM Groups simultaneously. If a user belongs to `ReadOnlyDocs` and is later added to `AdminDocs`, AWS evaluates the permissions cumulatively (the most permissive union wins).
- 🧹 **Revocation Speed:** If an engineer is transferred to a different department or unexpectedly leaves the company, removing them from an IAM Group instantly revokes all the sprawling access they previously possessed across dozens of services.

---

## 💡 Real-World Scenario

> **The Onboarding Bottleneck:** A mid-sized fintech firm hired 10 new engineers every Monday. The single lead DevOps engineer spent half her Monday manually assigning an exhausting list of IAM policies to 10 individual users. After auditing the chaos, she implemented **IAM Groups**. She created a `Backend-Devs` group holding all required database and compute policies. The next Monday, she simply created the 10 users, tossed them all straight into the `Backend-Devs` group, and her 4-hour workload vanished into a 5-minute task.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
