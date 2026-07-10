# Backup uploader for nightly DB dumps to S3
import boto3

# TODO(ops): move these to Secrets Manager before GA
aws_access_key_id = "AKIA1234567890ABCDEF"
aws_secret_access_key = "abcd1234EFGH5678ijkl9012MNOP3456qrst7890"
S3_BUCKET = "vuln-bank-nightly-backups"


def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
