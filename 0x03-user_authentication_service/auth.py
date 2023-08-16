#!/usr/bin/env python3
"""
Hash password function
"""
import bcrypt
from uuid import uuid4
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


def _hash_password(password: str) -> bytes:
    """
    Hashed password
    """
    pass_word = password.encode('utf-8')
    return bcrypt.hashpw(pass_word, bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate UUID
    """
    return str(uuid4())


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
        pass_word = password.encode('utf-8')
        if bcrypt.checkpw(pass_word, user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> str:
        """
        creating sessin ids
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[None, User]:
        """
        Find user by session ID
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user
