#!/usr/bin/env python3
"""
Hash password function
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hashed password
    """
    pass_word = password.encode('utf-8')
    return bcrypt.hashpw(pass_word, bcrypt.gensalt())
