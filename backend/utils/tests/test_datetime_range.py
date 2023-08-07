#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_datetime_range.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubset', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual',
 'assertIdentical', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
 'assertIsNot', 'assertIsNotInstance', 'assertIsNotNone', 'assertItemsEqual',
 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMethodsMatch',
 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals',
 'assertNotApproximates', 'assertNotEndsWith', 'assertNotEqual',
 'assertNotEquals', 'assertNotIdentical', 'assertNotIn', 'assertNotIsInstance',
 'assertNotRegexpMatches', 'assertNotStartsWith', 'assertRaises',
 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual',
 'assertSetEqual', 'assertStartsWith', 'assertTrue', 'assertTupleEqual', ]

['failIf', 'failIfAlmostEqual', 'failIfApproximates', 'failIfEndsWith',
 'failIfEqual', 'failIfIdentical', 'failIfIn', 'failIfIs', 'failIfIsInstance',
 'failIfStartsWith', 'failUnless', 'failUnlessAlmostEqual',
 'failUnlessApproximates', 'failUnlessEndsWith', 'failUnlessEqual',
 'failUnlessIdentical', 'failUnlessIn', 'failUnlessIs', 'failUnlessIsInstance',
 'failUnlessMethodsMatch', 'failUnlessRaises', 'failUnlessRaisesRegexp',
 'failUnlessStartsWith', 'failureException', ]

"""
import datetime

from django.test import TestCase
from utils.datetime_range import DateTimeRange


class TestDateTimeRange(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.start_datetime = datetime.datetime(year=2020, month=1, day=1)
        self.end_datetime = datetime.datetime(year=2020, month=2, day=1)
        self.daterange = DateTimeRange(self.start_datetime, self.end_datetime)

    def test_is_between(self, ):
        self.assertTrue(self.daterange.is_between(datetime.datetime(year=2020, month=1, day=2)))
        self.assertFalse(self.daterange.is_between(datetime.datetime(year=2019, month=12, day=1)))
        self.assertFalse(self.daterange.is_between(datetime.datetime(year=2020, month=3, day=1)))

    def test_iter_range(self, ):
        expects = [datetime.datetime(year=2020, month=1, day=1),
                   datetime.datetime(year=2020, month=1, day=2),
                   datetime.datetime(year=2020, month=1, day=3),
                   datetime.datetime(year=2020, month=1, day=4),
                   datetime.datetime(year=2020, month=1, day=5),
                   datetime.datetime(year=2020, month=1, day=6),
                   datetime.datetime(year=2020, month=1, day=7),
                   datetime.datetime(year=2020, month=1, day=8),
                   datetime.datetime(year=2020, month=1, day=9),
                   datetime.datetime(year=2020, month=1, day=10),
                   datetime.datetime(year=2020, month=1, day=11),
                   datetime.datetime(year=2020, month=1, day=12),
                   datetime.datetime(year=2020, month=1, day=13),
                   datetime.datetime(year=2020, month=1, day=14),
                   datetime.datetime(year=2020, month=1, day=15),
                   datetime.datetime(year=2020, month=1, day=16),
                   datetime.datetime(year=2020, month=1, day=17),
                   datetime.datetime(year=2020, month=1, day=18),
                   datetime.datetime(year=2020, month=1, day=19),
                   datetime.datetime(year=2020, month=1, day=20),
                   datetime.datetime(year=2020, month=1, day=21),
                   datetime.datetime(year=2020, month=1, day=22),
                   datetime.datetime(year=2020, month=1, day=23),
                   datetime.datetime(year=2020, month=1, day=24),
                   datetime.datetime(year=2020, month=1, day=25),
                   datetime.datetime(year=2020, month=1, day=26),
                   datetime.datetime(year=2020, month=1, day=27),
                   datetime.datetime(year=2020, month=1, day=28),
                   datetime.datetime(year=2020, month=1, day=29),
                   datetime.datetime(year=2020, month=1, day=30),
                   datetime.datetime(year=2020, month=1, day=31),
                   datetime.datetime(year=2020, month=2, day=1),
        ]
        t_lsdatetimes = list(self.daterange.iter_range(datetime.timedelta(days=1)))
        for expect in expects:
            self.assertTrue(expect in t_lsdatetimes)
            self.assertEqual(len(expects), len(t_lsdatetimes))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_datetime_range.py ends here
