# passwordchecker.py

import re

def check_password_strength(password: str) -> str:
    """Check the strength of the given password and return result."""

    # Rule 1: Minimum length
    if len(password) < 8:
        return "❌ Weak: Password must be at least 8 characters long."

    # Rule 2: Use regex to check conditions
    if not re.search(r"[A-Z]", password):
        return "❌ Weak: Add at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "❌ Weak: Add at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "❌ Weak: Add at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "❌ Weak: Add at least one special character."

    return "✅ Strong: Your password looks good!"

if __name__ == "__main__":
    pwd = input("Enter your password to check: ")
    result = check_password_strength(pwd)
    print(result)
