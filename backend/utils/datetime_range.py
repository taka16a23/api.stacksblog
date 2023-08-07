#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""datetime_range -- DateTime range class

"""
import datetime
import pytz


class DateTimeRange(object):
    """DateTimeRange

    DateTimeRange is a object.
    Responsibility:
    """
    def __init__(self, a_start, a_end):
        """

        @Arguments:
        - `a_start`: (datetime.datetime) start of datetime range.
        - `a_end`: (datetime.datetime) end of datetime range.
        """
        if not isinstance(a_start, (datetime.datetime, )):
            raise TypeError(
                'a_start must be datetime.datetime type. got({0})'
                .format(a_start))
        if not isinstance(a_end, (datetime.datetime, )):
            raise TypeError(
                'a_end must be datetime.datetime type. got({0})'
                .format(a_end))
        self.__start = a_start
        self.__end = a_end
        if self.__start.tzinfo is None or self.__start.tzinfo.utcoffset(self.__start) is None:
            self.__start = self.__start.replace(tzinfo=pytz.utc)
        if self.__end.tzinfo is None or self.__end.tzinfo.utcoffset(self.__end) is None:
            self.__end = self.__end.replace(tzinfo=pytz.utc)
        if self.__end < self.__start:
            self.__start, self.__end = self.__end, self.__start

    def is_between(self, a_datetime):
        """Is between range start and end.

        is_between_range(a_datetime)

        @Arguments:
        - `a_datetime`: (datetime.datetime) compable datetime.

        @Return: True if a_datetime is between start and end.

        @Error: TypeError
        """
        if not isinstance(a_datetime, (datetime.datetime, )):
            raise TypeError(
                'a_datetime must be datetime.datetime type. got({0})'
                .format(a_datetime))
        if a_datetime < self.__start:
            return False
        if self.__end < a_datetime:
            return False
        return True

    def iter_range(self, a_timedelta):
        """Iterate datetime from start to end.

        iter_range(a_timedelta)

        @Arguments:
        - `a_timedelta`: (datetime.timedelta)

        @Return: (datetime.datetime) each datetime from start to end by timedelta.

        @Error: TypeError
        """
        if not isinstance(a_timedelta, (datetime.timedelta, )):
            raise TypeError(
                'a_timedelta must be datetime.timedelta type. got({0})'
                .format(a_timedelta))
        t_datetime = self.__start
        while t_datetime <= self.__end:
            yield t_datetime
            t_datetime = t_datetime + a_timedelta

    def __repr__(self):
        return ('{0.__class__.__name__}<start={1}, end={2}>'
                .format(self, str(self.__start), str(self.__end)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# datetime_range.py ends here
