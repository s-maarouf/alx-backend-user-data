#!/usr/bin/env python3

"""Authentification module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authentification class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return None
