#!/usr/bin/env python3

from hashlib import pbkdf2_hmac
import string

chars = string.digits + string.ascii_letters + string.punctuation
salt = 'pepper'

def convert_bytes_to_password(hashed_bytes, length):
    number = int.from_bytes(hashed_bytes, byteorder="big")
    password = ""
    while number > 0 and len(password) <length:
        password = password + chars[number % len(chars)]
        number = number // len(chars)
    return password

def convert_hash_string_to_password(hash_string):
    hashed_bytes = pbkdf2_hmac("sha512", hash_string.encode("utf-8"), salt.encode("utf-8"), 4096)
    password = convert_bytes_to_password(hashed_bytes, 10)
    return password

if __name__ == '__main__':
    hash_string = input('Hash String >>>')

    while len(hash_string) < 1:
        hash_string = input('Hash String >>>')

    print(F'Hashed Passphrase >>> {hash_string}')