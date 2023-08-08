#!/usr/bin/env python3
''' basic authentication file'''
import base64
from .auth import Auth


class BasicAuth(Auth):
    ''' Basic Auth class '''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        ''' extract base64 authorization header'''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split()[-1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        ''' decodes base64 string'''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header).decode('utf-8')
            return decoded
        except Exception:
            return None
