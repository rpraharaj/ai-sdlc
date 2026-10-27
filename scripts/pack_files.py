"""Shared filename policy for portable pack payloads, using the standard library."""

from pathlib import Path


def is_secret_filename(path: Path) -> bool:
    name = path.name.lower()
    return (
        (name == ".env" or name.startswith(".env.")) and name != ".env.example"
        or path.suffix.lower() in {".pem", ".p12", ".pfx", ".key", ".keystore"}
        or name in {"id_rsa", "id_ed25519", "id_ecdsa", "id_dsa", "credentials",
                    "credentials.json", "secrets.json", "keystore"}
    )
