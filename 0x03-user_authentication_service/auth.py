#!/usr/bin/env python3
"""
Hash password function
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    hashed password
    """
    pass_word = password.encode('utf-8')
    return bcrypt.hashpw(pass_word, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user
        """
        user = self._db.find_user_by(email=email)
        hashed_password = _hash_password(password)
        if user is not None:
            raise ValueError(f"User {email} already exists")
        return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        validate credentials
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False
        if user:
            password = password.encode('utf-8')
            return bcrypt.checkpw(password, user.hashed_password)
