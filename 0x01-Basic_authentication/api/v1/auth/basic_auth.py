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
            d = base64.b64decode(base64_authorization_header).decode('utf-8')
            return d
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        ''' returns the user email and password from the Base64 decoded value.
        '''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email, password = decoded_base64_authorization_header.split(":")
        return (email, password)
