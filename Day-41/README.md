<div align="center">
  <img src="https://img.shields.io/badge/AWS-100%20Days%20Challenge-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="100 Days of AWS Challenge"/>
  <h1>☁️ Day 41: Securing Data with AWS KMS</h1>
</div>

---

## 🎥 Video Tutorial

<p align="center">
  <a href="https://www.youtube.com/watch?v=9Jwq3Kr3-uw">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Solution-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube"/>
  </a>
</p>

---

## 🧠 Task Overview

Encrypt and decrypt sensitive information using symmetric encryption keys managed seamlessly by AWS Key Management Service (KMS).

---

### 🛠️ Hands-On Commands

```bash
KEY_ID=$(aws kms create-key \
  --description "xfusion symmetric encryption key" \
  --key-usage ENCRYPT_DECRYPT \
  --customer-master-key-spec SYMMETRIC_DEFAULT \
  --query 'KeyMetadata.KeyId' \
  --output text)

# Create the required alias
aws kms create-alias \
  --alias-name alias/xfusion-KMS-Key \
  --target-key-id $KEY_ID

echo "Key created and aliased as: alias/xfusion-KMS-Key"
echo "Key ID: $KEY_ID"

aws kms encrypt \
  --key-id alias/xfusion-KMS-Key \
  --plaintext fileb:///root/SensitiveData.txt \
  --output text \
  --query CiphertextBlob \
  | base64 --decode > /root/EncryptedData.bin

# Decrypt to a temporary file
aws kms decrypt \
  --ciphertext-blob fileb:///root/EncryptedData.bin \
  --output text \
  --query Plaintext \
  | base64 --decode > /root/DecryptedData.txt

# Compare files (no output = identical)
diff /root/SensitiveData.txt /root/DecryptedData.txt

# Quick success message
[ $? -eq 0 ] && echo "Verification successful - files match" || echo "Mismatch detected"

# Clean up
rm -f /root/DecryptedData.txt
```

---


## 🎯 Key Takeaways & Best Practices

- 🔐 **Symmetric vs Asymmetric:** AWS KMS heavily leverages fast, symmetric AES-256 keys by default for general encryption.
- 🔑 **Envelope Encryption:** KMS primarily encrypts your data-keys, which in turn are used to encrypt the actual bulky payloads.

---

## 💡 Real-World Scenario

> **Database Passwords:** Storing API keys or sensitive user PII in a configuration file? Wrap it with KMS encryption so hackers steal only illegible cipher-blobs.

---

## 🤝 Support the Content

If this breakdown helped you simplify AWS, please support the journey!
- ⭐ **Star this Repository:** [KodeKloud-100-Days-Of-AWS](https://github.com/MiqdadProjects/KodeKloud-100-Days-Of-AWS.git)
- 🔔 **Subscribe on YouTube:** Enable notifications so you never miss a day of the challenge!

## 📚 AWS Concepts & Services Covered

Here is a crystal-clear explanation of the AWS concepts and services actively used in this day's task:

- **AWS KMS (Key Management Service):** A critical security service that securely generates, stores, and strictly controls cryptographic keys used to transparently encrypt your data (using Symmetric AES-256 keys by default).
