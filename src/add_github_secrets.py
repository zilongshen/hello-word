#!/usr/bin/env python3

import os
import sys
import base64
import requests
from nacl import encoding, public
from getpass import getpass

def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a secret using the repository's public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return base64.b64encode(encrypted).decode("utf-8")

def get_public_key(owner: str, repo: str, token: str) -> tuple:
    """Get the repository's public key."""
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/secrets/public-key"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["key"], response.json()["key_id"]

def add_secret(owner: str, repo: str, token: str, secret_name: str, secret_value: str) -> None:
    """Add a secret to the repository."""
    public_key, key_id = get_public_key(owner, repo, token)
    encrypted_value = encrypt(public_key, secret_value)
    
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/secrets"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}"
    }
    data = {
        "encrypted_value": encrypted_value,
        "key_id": key_id
    }
    
    response = requests.put(f"{url}/{secret_name}", headers=headers, json=data)
    response.raise_for_status()
    print(f"Successfully added secret: {secret_name}")

def read_secrets_file(file_path: str) -> dict:
    """Read secrets from a file in key=value format."""
    secrets = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    secrets[key.strip()] = value.strip()
        return secrets
    except FileNotFoundError:
        print(f"Error: Secrets file '{file_path}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid format in secrets file. Each line should be in 'key=value' format.")
        sys.exit(1)

def main():
    # Repository information
    owner = "cityark"
    repo = "cityark-test-platform-service"
    
    # Get GitHub token
    token = getpass("Enter your GitHub Personal Access Token: ")
    
    # Read secrets from file
    secrets_file = os.path.join(os.path.dirname(__file__), "secrets.txt")
    secrets = read_secrets_file(secrets_file)
    
    if not secrets:
        print("No secrets found in the file.")
        sys.exit(1)
    
    try:
        for secret_name, secret_value in secrets.items():
            add_secret(owner, repo, token, secret_name, secret_value)
        print("\nAll secrets have been added successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 