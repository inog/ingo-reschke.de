#!/usr/bin/env python3
import os
import sys
import ftplib
import ssl
from pathlib import Path

def main():
    server = os.environ.get("FTP_SERVER")
    username = os.environ.get("FTP_USERNAME")
    password = os.environ.get("FTP_PASSWORD")

    if not server or not username or not password:
        print("Error: FTP_SERVER, FTP_USERNAME, and FTP_PASSWORD must be set.", file=sys.stderr)
        sys.exit(1)

    print(f"Connecting to {server} via FTPS...")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    ftp = ftplib.FTP_TLS(context=ctx)
    ftp.connect(server, 21, timeout=30)
    ftp.login(username, password)
    ftp.prot_p()

    print(f"Logged in successfully! Root directory: {ftp.pwd()}")
    try:
        root_items = ftp.nlst()
        print(f"Contents of root directory: {root_items}")
    except Exception as e:
        print(f"Could not list root directory: {e}")

    # Determine target directory
    candidate_paths = [
        "ingo-reschke.de/httpdocs/website",
        "httpdocs/website",
        "httpdocs",
        "."
    ]
    target_dir = None
    for cand in candidate_paths:
        try:
            ftp.cwd("/")
            ftp.cwd(cand)
            print(f"Found target directory: '{cand}' (current pwd: {ftp.pwd()})")
            target_dir = cand
            break
        except Exception:
            continue

    if not target_dir:
        print("Error: Could not find suitable target directory on server!", file=sys.stderr)
        sys.exit(1)

    print(f"\nDeploying website files to: {ftp.pwd()}...")

    repo_root = Path(__file__).resolve().parent.parent
    ignored_patterns = {".git", ".github", ".idea", "scripts", "README.md", ".gitignore"}

    def upload_dir(local_path: Path):
        for item in sorted(local_path.iterdir()):
            if item.name in ignored_patterns or item.name.startswith("."):
                continue
            if item.is_dir():
                try:
                    ftp.mkd(item.name)
                except Exception:
                    pass  # Directory already exists
                ftp.cwd(item.name)
                upload_dir(item)
                ftp.cwd("..")
            elif item.is_file():
                rel_path = item.relative_to(repo_root)
                print(f"  -> Uploading: {rel_path}")
                with open(item, "rb") as f:
                    ftp.storbinary(f"STOR {item.name}", f)

    upload_dir(repo_root)
    ftp.quit()
    print("\n✓ Deployment completed successfully!")

if __name__ == "__main__":
    main()
