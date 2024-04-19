#!/usr/bin/env python3

"""Basic authentification module"""

from flask import request
from typing import List, TypeVar
import re
import base64

from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """returns the decoded user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        mail, passwd = decoded_base64_authorization_header.split(":", 1)
        return mail, passwd

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if type(user_email) is not str or user_email is None:
            return None
        if type(user_pwd) is not str or user_pwd is None:
            return None
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance for a request"""
        header = self.authorization_header(request)
        extract = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(extract)
        email, passwd = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(email, passwd)
