#!/usr/bin/python3
'''Auth class'''
from typing import List, TypeVar
from flask import request


class Auth():
    """
        Manages API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            -path
            -excluded path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        returns none
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return none
        """
        return None
