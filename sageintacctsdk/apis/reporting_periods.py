"""
Sage Intacct reporting periods
"""
from .api_base import ApiBase


class ReportingPeriods(ApiBase):
    """Class for Projects APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='REPORTINGPERIOD')
