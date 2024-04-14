#!/usr/bin/env python3

"""Password hashing module"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypts a password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
