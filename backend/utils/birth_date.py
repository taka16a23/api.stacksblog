#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""birth_date -- define birth date class

"""
import datetime

from .age import Age


class BirthDate(datetime.date):
    """BirthDate

    BirthDate is a datetime.date.
    Responsibility:
    """
    @classmethod
    def from_date(cls, date):
        """Create instance from date

        from_date(date)

        @Arguments:
        - `date`: datetime.date

        @Return:
            datetime.date
        @Error:
        """
        if date is None:
            return None
        if not isinstance(date, (datetime.datetime, datetime.date)):
            raise TypeError(
                'date is not datetime or date. got({0.__class__.__name__})'.format(date))
        return cls(date.year, date.month, date.day)

    def get_age(self, ):
        """Get age from birth date

        get_age()

        @Return:

        @Error:
        """
        nowYYYYmmdd = int(datetime.datetime.now().strftime('%Y%m%d'))
        birthYYYYmmdd = int(self.strftime('%Y%m%d'))
        return Age(int((nowYYYYmmdd - birthYYYYmmdd) / 10000))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# birth_date.py ends here
