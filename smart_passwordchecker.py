import re, math, secrets, string, random

# Simple word list for memorable combinations
WORDS = ["Tiger", "Sky", "River", "Mountain", "Jump", "Book", "Cloud", "Tree", "Stone", "Fire", "Wind", "Light"]

def password_entropy(password: str) -> float:
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 33
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

def crack_time(password: str, guesses_per_sec=1e9) -> str:
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

def suggest_strong_password(length=14) -> str:
    """Strong random password with letters and digits only."""
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

def suggest_memorable_password(username: str) -> str:
    """Generate a memorable but strong password using the user's name and word combos."""
    word1 = random.choice(WORDS)
    word2 = random.choice(WORDS)
    number = str(secrets.randbelow(90) + 10)  # Two-digit number
    return f"{username.title()}{word1}{number}{word2}"

def check_password(username: str, password: str) -> None:
    print(f"\nHello {username.title()}, let's check your password strength.")

    if len(password) < 8:
        print("Your password is too short. It should be at least 8 characters.")
    elif not re.search(r"[A-Z]", password):
        print("Your password should include at least one uppercase letter.")
    elif not re.search(r"[a-z]", password):
        print("Your password should include at least one lowercase letter.")
    elif not re.search(r"[0-9]", password):
        print("Your password should include at least one number.")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Your password should include at least one special character.")
    else:
        print("Great job, your password meets all the basic requirements!")

    entropy = password_entropy(password)
    print(f"Password Entropy: {entropy:.2f} bits")
    print(f"Estimated Time to Crack: {crack_time(password)}")

    if entropy < 50:
        print(f"\n{username.title()}, your password could be stronger.")
        print("Here are some suggested password formats you can try:")
        print("- Memorable: ", suggest_memorable_password(username))
        print("- Random (letters & numbers):", suggest_strong_password(14))
    else:
        print("Your password is reasonably strong.")

if __name__ == "__main__":
    username = input("Enter your name: ")
    pwd = input("Enter your password: ")
    check_password(username.strip(), pwd)
