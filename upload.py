import boto3
import json
import os
import botocore

# ---------------- CONFIG ----------------
BUCKET_NAME = "gaurav-static-site-1234567"   # must be globally unique
REGION = "ap-south-1"

# Get current folder path (fix file path issue)
BASE_DIR = os.path.dirname(__file__)

s3 = boto3.client('s3', region_name=REGION)

# ---------------- CREATE BUCKET ----------------
def create_bucket():
    try:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print("✅ Bucket created")
    except botocore.exceptions.ClientError as e:
        print("⚠️ Bucket may already exist:", e)

# ---------------- DISABLE BLOCK PUBLIC ACCESS ----------------
def disable_block_public():
    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
    )
    print("✅ Public access block disabled")

# ---------------- UPLOAD FILES ----------------
def upload_files():
    try:
        index_path = os.path.join(BASE_DIR, "index.html")
        error_path = os.path.join(BASE_DIR, "error.html")

        s3.upload_file(index_path, BUCKET_NAME, "index.html",
                       ExtraArgs={'ContentType': 'text/html'})

        s3.upload_file(error_path, BUCKET_NAME, "error.html",
                       ExtraArgs={'ContentType': 'text/html'})

        print("✅ Files uploaded")
    except Exception as e:
        print("❌ File upload error:", e)

# ---------------- ENABLE STATIC HOSTING ----------------
def enable_static_hosting():
    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            'IndexDocument': {'Suffix': 'index.html'},
            'ErrorDocument': {'Key': 'error.html'}
        }
    )
    print("✅ Static hosting enabled")

# ---------------- MAKE BUCKET PUBLIC ----------------
def make_public():
    policy_dict = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
            }
        ]
    }

    policy = json.dumps(policy_dict)

    s3.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=policy
    )

    print("✅ Bucket made public")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("🚀 Deploying Static Website...\n")

    create_bucket()
    disable_block_public()
    upload_files()
    enable_static_hosting()
    make_public()

    print("\n🌐 Website URL:")
    print(f"http://{BUCKET_NAME}.s3-website-{REGION}.amazonaws.com")