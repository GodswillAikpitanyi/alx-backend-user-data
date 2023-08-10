#!/usr/bin/env python3
''' SessionAuth class
'''
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    ''' creating a new authentication mechanism
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        creates a Session ID for a user_id
        '''
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        s_id = str(uuid4())
        SessionAuth.user_id_by_session_id[s_id] = user_id
        return s_id
