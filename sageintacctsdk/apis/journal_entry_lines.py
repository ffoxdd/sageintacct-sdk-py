"""
Sage Intacct Journal Entry Lines
"""
from typing import Dict

from .api_base import ApiBase


class JournalEntryLines(ApiBase):
    """Class for Journal Entry Lines APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLENTRY')
