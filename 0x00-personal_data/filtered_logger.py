#!/usr/bin/env python3

"""Personnal data module"""

import re
from typing import List
import logging


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
) -> str:
    """Replace sensitive information in a message with redaction."""
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]+',
                         f'{field}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt
