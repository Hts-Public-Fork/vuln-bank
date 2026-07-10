# Admin backup endpoint for nightly DB dumps
from flask import Blueprint, request
import os
import boto3

backup_bp = Blueprint("backup", __name__)
S3_BUCKET = "vuln-bank-nightly-backups"


@backup_bp.route("/admin/backup")
def run_backup():
    db_name = request.args.get("db")
    os.system("pg_dump " + db_name + " > /tmp/backup.sql")
    return "backup started"


@backup_bp.route("/admin/restore")
def run_restore():
    path = request.args.get("path")
    os.popen("psql < " + path).read()
    return "restore started"


def get_s3_client():
    return boto3.client("s3")
