import re

def check_url(address):

    if address.startswith("http://") or address.startswith("https://"):
        domain = address.split("://")[1]
        if "." in domain and re.fullmatch(r"[A-Za-z0-9.-]+", domain):
            return "valid"

    return "invalid"