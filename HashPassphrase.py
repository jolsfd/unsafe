#!/usr/bin/env python3

from hashlib import pbkdf2_hmac
import string

chars = string.digits + string.ascii_letters + string.punctuation
salt = "pepper"


def convert_bytes_to_string(hashed_bytes, length):
    number = int.from_bytes(hashed_bytes, byteorder="big")
    string = ""
    while number > 0 and len(string) < length:
        string = string + chars[number % len(chars)]
        number = number // len(chars)
    return string


def convert_hash_string(hash_string):
    hashed_bytes = pbkdf2_hmac(
        "sha512", hash_string.encode("utf-8"), salt.encode("utf-8"), 4096
    )
    hashed_string = convert_bytes_to_string(hashed_bytes, 16)
    return hashed_string


if __name__ == "__main__":
    hash_string = input("Hash String >>>")

    while len(hash_string) < 1:
        hash_string = input("Hash String >>>")

    hashed_string = convert_hash_string(hash_string)

    print(f"Hashed Passphrase >>> {hashed_string}")
