import re, math, secrets, string

def password_entropy(password: str) -> float:
    """Calculate password entropy in bits."""
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 33  # Approx special chars

    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

def crack_time(password: str, guesses_per_sec=1e9) -> str:
    """Estimate time to crack password with brute force."""
    entropy = password_entropy(password)
    attempts = 2 ** entropy
    seconds = attempts / guesses_per_sec

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31557600:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31557600:.2f} years"

def suggest_password(length=12) -> str:
    """Generate a strong password suggestion."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def check_password(password: str) -> None:
    """Check strength and give AI suggestions."""
    print(f"🔎 Checking password: {password}")
    
    if len(password) < 8:
        print("❌ Weak: Too short (min 8 characters).")
    elif not re.search(r"[A-Z]", password):
        print("❌ Weak: Add an uppercase letter.")
    elif not re.search(r"[a-z]", password):
        print("❌ Weak: Add a lowercase letter.")
    elif not re.search(r"[0-9]", password):
        print("❌ Weak: Add a number.")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("❌ Weak: Add a special character.")
    else:
        print("✅ Strong password!")

    entropy = password_entropy(password)
    print(f"🔐 Entropy: {entropy:.2f} bits")
    print(f"⏳ Estimated crack time: {crack_time(password)}")

    if entropy < 50:
        print("💡 Suggested strong password:", suggest_password(14))

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    check_password(pwd)
