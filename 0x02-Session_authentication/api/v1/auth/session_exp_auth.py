#!/usr/bin/env puthon3

"""Session expiration module"""

import os
import datetime

from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session expiration class"""

    def __init__(self) -> None:
        """initializes a new SessionExpAuth instance"""
        session_duration = int(os.getenv('SESSION_DURATION'))
        if not int(session_duration):
            session_duration = 0

    def create_session(self, user_id=None):
        """returns created session"""
        session = super().create_session(user_id)
        if not session:
            return None
        self.user_id_by_session_id[session] = {
            'user_id': user_id,
            'created_at': datetime.datetime.now()
        }
        return session

    def user_id_for_session_id(self, session_id=None):
        """returns userid assosiated with sessionid"""
        session_dict = self.user_id_by_session_id[session_id]
        if session_id is None:
            return None
        if not self.user_id_by_session_id[session_id]:
            return None
        if self.session_duration <= 0:
            return session_dict['user_id']
        if 'created_at' not in session_dict:
            return None
        curr_time = datetime.datetime.now()
        span = datetime.timedelta(seconds=self.session_duration)
        exp_time = session_dict['created_at'] + span
        if exp_time < curr_time:
            return None
        return session_dict['user_id']
