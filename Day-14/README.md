<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 14: Terminate EC2 Instance</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=nNOIw0O-SXA">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

In cloud terminology, "Stopping" an instance is like shutting down your laptop for the night; "Terminating" an instance is like throwing your laptop into an active volcano. 

Termination permanently de-provisions the underlying virtual hardware, releases it back into the AWS compute pool, and deletes the root storage volume. In this task, you walk through the irreversible process of instance termination and explore what resources survive the apocalypse unharmed.

---

## 🎯 Key Takeaways & Best Practices

- 🪦 **The Root Volume Death Trap:** By default, the root EBS volume (`/dev/xvda` or `/dev/sda1`) has an attribute called `DeleteOnTermination` set to **True**. When the instance dies, the root drive dies with it instantly.
- 📉 **Cost Considerations:** The moment an instance enters the "Shutting down" or "Terminated" state, AWS entirely stops charging you for hourly compute costs.
- 🔀 **Elastic IPs Unbound:** Terminating an instance automatically detaches (but does NOT delete) any associated Elastic IPs or secondary Elastic Network Interfaces (ENIs). You must manually release the Elastic IPs afterward to avoid ghost billing charges.
- 🕰️ **The Ghost Display:** After termination, the instance will awkwardly remain visible in the EC2 Console for a short period. This is perfectly normal and does not incur charges; AWS simply takes time to clean up the visual history.

---

## 💡 Real-World Scenario

> **The Phantom Billing Nightmare:** A student researcher launched a massive $2-an-hour GPU-optimized `p3.2xlarge` instance to train an AI model. Once the training finished, they shut down the instance using the OS command (`sudo shutdown -h now`) thinking that would stop the billing. It did stop the compute costs, but they failed to realize the instance had a massive, expensive 2TB Provisioned IOPS root volume attached. Since they didn't officially "Terminate" the instance via the AWS Console, the 2TB volume sat idle and continued legally billing the student hundreds of dollars over the next month for unused storage.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!
