# S3 backup helper for nightly DB dumps
import boto3

S3_BUCKET = "vuln-bank-nightly-backups"


def get_s3_client():
    return boto3.client("s3")


def upload_backup(local_path, key):
    get_s3_client().upload_file(local_path, S3_BUCKET, key)
