"""TEMPORARY test fixture for HTSOne PR-delta verification.

Four deliberate, high-confidence SAST findings so the PR "Introduced" count is
exactly predictable. Delete this file after the PR flow is verified.
"""
import hashlib
import sqlite3
import subprocess

API_TOKEN = "AKIAIOSFODNN7EXAMPLE"  # 1. hardcoded credential


def lookup_user(conn: sqlite3.Connection, user_id: str):
    cur = conn.cursor()
    # 2. SQL injection — unsanitised concatenation
    cur.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
    return cur.fetchall()


def run_report(expr: str):
    # 3. code injection — eval on caller-controlled input
    return eval(expr)


def fingerprint(password: str) -> str:
    # 4. weak hash
    return hashlib.md5(password.encode()).hexdigest()


def ping(host: str):
    # 5. command injection — shell=True with interpolation
    return subprocess.check_output("ping -c 1 " + host, shell=True)
