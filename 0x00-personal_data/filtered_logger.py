#!/usr/bin/env python3

"""Personnal data module"""

import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
) -> str:
    """Replace sensitive information in a message with redaction."""
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]+',
                         f'{field}={redaction}', message)
    return message
