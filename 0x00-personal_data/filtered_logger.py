#!/usr/bin/env python3

"""Personnal data module"""

import re
import os
from typing import List
import logging
import mysql.connector


PII_FIELDS = ("name", "phone", "ssn", "password", "email")


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
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))
    log.setLevel(logging.INFO)
    log.propagate = False
    log.addHandler(stream)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connects to the database and returns a MySQLConnection object."""
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_pass = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    connector = mysql.connector.connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_pass,
        database=db_name
    )
    return connector
