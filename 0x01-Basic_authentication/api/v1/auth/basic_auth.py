#!/usr/bin/env python3
''' basic authentication file'''
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
