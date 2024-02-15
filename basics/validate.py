from re import search, IGNORECASE
email = input("What's your email?").strip()

if search(r"^\w+@(\w+\.)*\w+\.com$", email, IGNORECASE):
    print("valid")
else:
    print("invalid")
