import os

glossary = """
## 🧠 Core AWS Concepts Explained (Glossary)

To help you get a crystal-clear understanding of the architecture built over these 100 days, here is a detailed breakdown of every major AWS concept and service used.

### 🖥️ Compute Services

**Amazon EC2 (Elastic Compute Cloud)**
EC2 provides resizable compute capacity in the cloud. Instead of buying physical hardware, you rent virtual servers (Instances), on which you can run Linux or Windows.
*   **Key Pairs:** AWS uses public-key cryptography to secure the login information for your instance. The public key is kept by AWS, and you keep the private key (`.pem` or `.ppk`).
*   **AMIs (Amazon Machine Images):** A master template for your EC2 instances. It contains the OS, application server, and applications.
*   **ENI (Elastic Network Interface):** A logical networking component in a VPC that represents a virtual network card.
*   **Elastic IPs:** A static, public IPv4 address designed for dynamic cloud computing. If your instance fails, you can rapidly remap the Elastic IP to another instance.
*   **User Data:** Scripts (like bash) that you pass to your EC2 instance at launch to automate boot tasks (like installing Nginx).

**AWS Lambda**
A serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you. You don't manage any servers; you just pay for the milliseconds your code executes.

**Amazon ECS (Elastic Container Service) & ECR**
ECS is a highly scalable container orchestration service. It allows you to run, stop, and manage Docker containers on a cluster. ECR (Elastic Container Registry) is where you store those Docker images securely.

**Amazon EKS (Elastic Kubernetes Service)**
A managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.

**Auto Scaling Groups (ASG)**
Automatically adjusts the number of EC2 instances in your application based on demand rules you define, ensuring high availability and optimized costs.

---

### 🌐 Networking & Content Delivery

**Amazon VPC (Virtual Private Cloud)**
A logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.
*   **Subnets:** Sub-sections of a VPC. A **Public Subnet** has a direct route to the Internet via an Internet Gateway. A **Private Subnet** has no direct Internet access, keeping resources highly secure.
*   **Internet Gateway (IGW):** A highly available VPC component that allows communication between instances in your VPC and the open internet.
*   **NAT Gateway / NAT Instance:** Allows resources in a private subnet to access the internet (e.g., to download OS updates) while preventing the internet from initiating a connection with those resources.
*   **VPC Peering:** A networking connection between two VPCs that enables routing traffic between them using private IPv4 addresses, as if they were in the same network.

**Security Groups & Network ACLs**
*   **Security Groups:** Act as a stateful, instance-level functional fireball. They evaluate traffic at the resource layer.
*   **NACLs (Network Access Control Lists):** Act as a stateless, subnet-level firewall. They provide an explicitly numbered rule list for inbound/outbound subnets.

**Elastic Load Balancing (Application Load Balancer - ALB)**
Automatically distributes incoming application traffic (HTTP/HTTPS) across multiple targets, such as EC2 instances, in multiple Availability Zones. This prevents any single server from getting overloaded.

---

### 🗄️ Storage & Databases

**Amazon S3 (Simple Storage Service)**
An object storage service offering industry-leading scalability, data availability, security, and performance. You can use S3 to store back-ups, hold application assets, or directly host a static HTML website!
*   **Versioning:** Keeping multiple variants of an object in the same bucket to protect against accidental overwrites or deletions.

**Amazon EBS (Elastic Block Store)**
Provides block level storage volumes (like hard drives) for use with EC2 instances. GP3 is a general-purpose SSD volume type.
*   **Snapshots:** Point-in-time incremental backups of an EBS volume stored securely in S3.

**Amazon RDS (Relational Database Service)**
A managed service that makes it easy to set up, operate, and scale a relational database (like MySQL or PostgreSQL) in the cloud. We place RDS exclusively in private subnets for maximum security.

**Amazon DynamoDB**
A fully managed, serverless, fast and flexible NoSQL database service for all applications that need consistent, single-digit millisecond latency at any scale.

---

### 🔒 Security, Identity & Compliance

**AWS IAM (Identity and Access Management)**
Enables you to manage access to AWS services and resources securely. You create **Users** (people), organize them in **Groups**, assign **Roles** (temporary permissions dynamically attached to services like EC2), and strictly govern access using JSON **Policies**.

**AWS KMS (Key Management Service)**
A managed service that makes it easy to create and control cryptographic keys. It supports **Symmetric Encryption** (using the exact same key to encrypt and decrypt) and Envelope Encryption to protect highly sensitive data files.

---

### 📊 Management & Governance

**Amazon CloudWatch**
A monitoring and observability service. We use **CloudWatch Alarms** to continually monitor EC2 CPU utilization and automatically trigger actions (like sending an email alert or scaling our ASG) when thresholds are breached.
"""

def inject_glossary():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    target = "## 🚀 Project Goal"
    
    # Check if glossary is already added
    if "## 🧠 Core AWS Concepts Explained (Glossary)" in content:
        print("Glossary already exists.")
        return

    parts = content.split(target)
    if len(parts) == 2:
        new_content = parts[0] + glossary + "\n\n" + target + parts[1]
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected glossary into README.md")
    else:
        print("Target string '## 🚀 Project Goal' not found exactly once.")

inject_glossary()
