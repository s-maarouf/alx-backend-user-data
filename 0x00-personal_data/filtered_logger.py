#!/usr/bin/env python3

"""Personnal data module"""

import re
from typing import List
import logging


PII_FIELDS = ("phone", "ssn", "password", "ip", "user_agent")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes a RedactingFormatter object."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record and applies redaction to sensitive data."""
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
) -> str:
    """Replace sensitive information in a message with redaction."""
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]+',
                         f'{field}={redaction}', message)
    return message


def get_logger() -> logging.Logger:
    """Returns a log object."""
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    return log
