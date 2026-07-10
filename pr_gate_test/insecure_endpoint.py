# PR-gate matrix test: intentionally-insecure endpoint (authorized security test).
# Introduces NEW high/critical SAST findings ONLY on the PR head to prove the gate
# blocks net-new vulnerabilities (fail-closed on the head). Safe to revert.
import os
import subprocess
import sqlite3

from flask import request


def run_network_diagnostics():
    # Command injection: user-controlled input concatenated into a shell command.
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
    subprocess.Popen("nslookup " + host, shell=True)


def lookup_account():
    # SQL injection: user input concatenated directly into a raw SQL query.
    account = request.args.get("account")
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id = '" + account + "'")
    return cursor.fetchall()


def evaluate_expression():
    # Code injection: eval() on user-controlled data.
    expr = request.args.get("expr")
    return eval(expr)
