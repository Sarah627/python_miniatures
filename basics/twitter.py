from re import sub
url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# we are going to imporve this using regex
url = input("URL: ").strip()
username = sub(r"^(https?://)?(www\.)?twitter.com/", "", url)
print(f"Username: {username}")
