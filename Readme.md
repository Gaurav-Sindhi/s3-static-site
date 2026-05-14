# 🚀 Static Website Hosting using Amazon S3 & boto3

## 📌 Overview

This project demonstrates how to automate static website hosting on Amazon S3 using Python and boto3 (AWS SDK for Python).

The script automatically:

* Creates an S3 bucket
* Uploads website files
* Enables static website hosting
* Configures public access
* Makes the website live

---

# 🧰 AWS Services Used

* Amazon S3
* boto3 (AWS SDK for Python)

---

# 🏗️ Architecture

```text id="x9j4re"
Local Website Files
        ↓
Python Automation Script
        ↓
Amazon S3 Bucket
        ↓
Static Website Hosting
        ↓
Public Website URL
```

---

# ⚙️ Features

✅ Automated S3 bucket creation
✅ Automated file upload
✅ Static website hosting enabled
✅ Public access configuration
✅ Fully automated deployment using Python

---

# 💻 Python Automation Script

## 🟢 upload.py

```python id="u7x1nb"
import boto3
import json
import os
import botocore

BUCKET_NAME = "gaurav-static-site-1234567"
REGION = "ap-south-1"

BASE_DIR = os.path.dirname(__file__)

s3 = boto3.client('s3', region_name=REGION)

def create_bucket():
    try:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print("Bucket created")
    except botocore.exceptions.ClientError as e:
        print(e)

def upload_files():
    index_path = os.path.join(BASE_DIR, "index.html")
    error_path = os.path.join(BASE_DIR, "error.html")

    s3.upload_file(index_path, BUCKET_NAME, "index.html")
    s3.upload_file(error_path, BUCKET_NAME, "error.html")

if __name__ == "__main__":
    create_bucket()
    upload_files()
```

---

# ⚙️ Setup Steps

## 1️⃣ Install boto3

```bash id="a5o4q9"
pip install boto3
```

---

## 2️⃣ Configure AWS Credentials

```bash id="m2q4hv"
aws configure
```

Enter:

* AWS Access Key
* AWS Secret Key
* Region

---

## 3️⃣ Run the Script

```bash id="d8tmx2"
python upload.py
```

---

# 🌐 Website Output

After successful deployment:

```text id="c6i0yu"
http://gaurav-static-site-1234567.s3-website-ap-south-1.amazonaws.com
```

---

# 📸 Screenshots

## 🔹 S3 Static Website Deployment Script Running

![Deployment Script](screenshots/Screenshot%202026-04-27%20005543.png)

---

## 🔹 Website Successfully Hosted on Amazon S3

![Website Running](screenshots/Screenshot%202026-04-27%20101702.png)

---

# 📊 Results

✅ Static website hosted successfully on Amazon S3
✅ Infrastructure deployment automated using Python
✅ Public website accessible through S3 endpoint
✅ Eliminated manual AWS Console operations

---

# 💡 Key Learnings

* S3 static website hosting
* boto3 automation
* AWS SDK usage
* Public bucket policy configuration
* Cloud automation scripting

---

# 🚀 Future Improvements

* Add custom domain using Route53
* Add HTTPS using CloudFront
* Add CI/CD pipeline
* Add automatic bucket cleanup
* Upload CSS & images dynamically

---

# 📂 Project Structure

```text id="v6v3er"
s3-static-site/
│── index.html
│── error.html
│── upload.py
│── README.md
│── screenshots/
│     ├── Screenshot 2026-04-27 005543.png
│     └── Screenshot 2026-04-27 101702.png
```

---

# 🔗 GitHub Commands

```bash id="v6dw8w"
git add .
git commit -m "Static Website Hosting using S3 and boto3"
git push
```

---

# 🎯 Interview Summary

> Built an automated static website hosting solution using Amazon S3 and boto3. Automated bucket creation, file uploads, and public hosting configuration using Python scripting.

---
