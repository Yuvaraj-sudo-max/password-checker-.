import hashlib
import requests
from colorama import Fore, Style

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in password): score += 1

    if score <= 2:
        return "Weak", Fore.RED
    elif score == 3 or score == 4:
        return "Moderate", Fore.YELLOW
    else:
        return "Strong", Fore.GREEN

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1[:5], sha1[5:]
    res = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count)
    return 0

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, color = check_strength(password)
    count = check_pwned(password)

    print(color + f"Password Strength: {strength}" + Style.RESET_ALL)
    if count:
        print(Fore.RED + f"⚠ Found in {count} breaches! Change it immediately." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "✅ Not found in known breaches. Good to go!" + Style.RESET_ALL)
