#!/usr/bin/env python3

"""Session autentification module"""

from uuid import uuid4

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session ID for a user"""
        if type(user_id) is not str or user_id is None:
            return None
        else:
            session = str(uuid4())
            self.user_id_by_session_id[session] = user_id
            return session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns user id based on session id"""
        if type(session_id) is not str or session_id is None:
          return None
        return self.user_id_by_session_id.get(session_id)