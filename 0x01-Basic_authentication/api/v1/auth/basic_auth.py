#!/usr/bin/env python3

"""Basic authentification module"""

from flask import request
from typing import List, TypeVar
import re

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
