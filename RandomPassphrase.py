#!/usr/bin/env python3

import secrets
import string

chars = string.digits + string.ascii_letters + string.punctuation

if __name__ == '__main__':
    print(''.join(secrets.choice(chars) for _ in range(40)))