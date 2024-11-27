from getpass import getpass
from hashlib import sha1
import requests

ADDRESS = "https://api.pwnedpasswords.com/range/"

# ask for password
pw = getpass("Enter password: ")

# hash password
pw_hash = sha1(pw.encode()).hexdigest().upper()
pw_hash_prefix = pw_hash[:5]
pw_hash_suffix = pw_hash[5:]
print("Your hash: " + pw_hash)

# get results from API
print("Getting hashes from API: " + str(ADDRESS + pw_hash_prefix))
try:
    response = requests.get(str(ADDRESS + pw_hash_prefix))
    response.raise_for_status()
    hashes = response.text
except requests.RequestException as e:
    print(f"Error fetching data from API: {e}")
    exit(1)

# check each hash
found = False
for line in hashes.splitlines():
    hash_suffix, count = line.split(":")
    if pw_hash_suffix == hash_suffix:
        print(f"Password found and pwned {count} times!")
        found = True
        break

if not found:
    print("Password not found and safe!")
