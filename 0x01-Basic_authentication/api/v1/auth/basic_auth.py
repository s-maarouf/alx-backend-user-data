#!/usr/bin/env python3

"""Basic authentification module"""

from flask import request
from typing import List, TypeVar
import re

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentification class"""
    pass
