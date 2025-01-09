"""
Sage Intacct account balances
"""
from datetime import date
from typing import Dict

from .api_base import ApiBase


class AccountBalances(ApiBase):
    """Class for Account Balance APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='UNUSED')

    def get_by_dimensions(self, account_number: str, start_date: date, end_date: date):
        data = {
            'get_accountbalancesbydimensions': {
                'startdate': {
                    'year': start_date.year,
                    'month': start_date.month,
                    'day': start_date.day
                },
                'enddate': {
                    'year': end_date.year,
                    'month': end_date.month,
                    'day': end_date.day
                },
                'glaccountno': account_number,
            }
        }

        response = self.format_and_send_request(data)['data']

        return response
