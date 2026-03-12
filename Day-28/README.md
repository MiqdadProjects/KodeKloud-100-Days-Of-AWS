<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 28: Create Private ECR Repository</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=pHDLDZVqQb4">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

To run modern, containerized applications on AWS platforms like ECS (Elastic Container Service) or EKS (Elastic Kubernetes Service), you need high-speed, secure access to your Docker images.

**Amazon Elastic Container Registry (ECR)** is a fully managed, highly available Docker container registry. Rather than relying on public DockerHub limits or hosting your own vulnerable registry, ECR allows you to tightly lock your proprietary application code within your AWS account's IAM boundary. In this task, you learn how to provision a secure ECR vault.

---

## 🎯 Key Takeaways & Best Practices

- 🔐 **IAM Authentication:** You cannot simply `docker login` to ECR with a password. You must use the AWS CLI to securely request a temporary, 12-hour authentication token (via `aws ecr get-login-password`), and pipe that token directly into the Docker CLI.
- 🏷️ **Immutability Matters:** By default, you can push a modified Docker image with the tag `latest` and it will overwrite your old `latest` image. **Best Practice:** Enable "Image Tag Mutability: IMMUTABLE" inside the ECR repository settings. This strictly prevents developers from accidentally overwriting production tags, forcing them to use distinct version numbers (e.g., `v1.2.4`).
- 🩺 **Image Scanning:** Always enable "Scan on Push". ECR utilizes the open-source Clair project behind the scenes to deeply scan your newly pushed Docker images for known CVE (Common Vulnerabilities and Exposures) operating system vulnerabilities before you deploy them.
- 🧹 **Lifecycle Policies:** Containers pile up fast. Write an ECR Lifecycle Rule to automatically delete any "Untagged" images older than 14 days, saving you from quietly accumulating massive storage bills over the course of a year.

---

## 💡 Real-World Scenario

> **The DockerHub Rate Limit Outage:** On November 2nd, 2020, DockerHub unexpectedly introduced strict download rate limit caps for anonymous pull requests. Suddenly, tens of thousands of automated enterprise CI/CD pipelines and Kubernetes clusters across the globe instantly fractured, unable to aggressively pull public images like `node:alpine` or `nginx:latest`. Companies relying on external registries lost hours of deployment productivity. Businesses that utilized **Amazon ECR** as a central, private caching mechanism for their base images completely ignored the global outage, as their ECS clusters quietly and securely pulled images from AWS's internal network backbone at lightning speed.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
