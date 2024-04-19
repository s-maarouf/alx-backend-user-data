#!/usr/bin/env python3

"""Basic authentification module"""

from flask import request
from typing import List, TypeVar
import re
import base64

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentification class"""

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded64 = base64.b64decode(base64_authorization_header)
            return decoded64.decode("utf-8")
        except base64.binascii.Error:
            return None
