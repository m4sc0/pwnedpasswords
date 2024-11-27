# pwnedpasswords

## Description

This is a simple demonstration of the [haveibeenpwned.com](https://haveibeenpwned.com) API.

If you run it you are prompted for a password (or anything else), the program will then hash your password and send a request with the first 5 characters of the hash to a dynamic API endpoint. The API will return a list of hashes that match the first 5 characters of your hash. The program will then check if your hash is in the list and tell you if it has been pwned and how many times.

It's a very simple program and was done just for fun. Check it out if you're interested!

## Usage

```bash
git clone https://github.com/m4sc0/pwnedpasswords
cd pwnedpasswords
python main.py
```
