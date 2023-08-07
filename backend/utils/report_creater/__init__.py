#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
import os
import sys
import subprocess

__all__ = [

]


class ReportCreater(object):
    """ReportCreater

    ReportCreater is a object.
    Responsibility:
    """
    COMMAND_PATH = '/usr/bin/chromium'

    VIRTUAL_TIME_BUDGET = 10000

    COMMAND_PARAMS = [
        '--no-sandbox',
        '--headless',
        '--disable-gpu',
        '--disable-translate',
        '--hide-scrollbars',
        '--disable-sync',
    ]

    def __init__(self, outputpath, url):
        """

        @Arguments:
        - `outputpath`:
        - `url`:
        """
        self._outputpath = outputpath
        self._url = url

    def get_outputpath(self, ):
        """SUMMARY

        get_outputpath()

        @Return:

        @Error:
        """
        return self._outputpath

    def set_outputpath(self, path):
        """SUMMARY

        set_outputpath(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        self._outputpath = path
        return self

    def get_url(self, ):
        """SUMMARY

        get_url()

        @Return:

        @Error:
        """
        return self._url

    def set_url(self, url):
        """SUMMARY

        set_url(url)

        @Arguments:
        - `url`:

        @Return:

        @Error:
        """
        self._url = url
        return self

    def create(self, ):
        """SUMMARY

        create()

        @Return:

        @Error:
        """
        if os.path.exists(self._outputpath):
            os.remove(self._outputpath)
        commands = [ReportCreater.COMMAND_PATH, ]
        commands.extend(ReportCreater.COMMAND_PARAMS)
        commands.append('--run-all-compositor-stages-before-draw')
        commands.append('--virtual-time-budget=' + str(ReportCreater.VIRTUAL_TIME_BUDGET))
        commands.append('--print-to-pdf=' + self._outputpath)
        commands.append(self._url)
        ret = subprocess.run(' '.join(commands), shell=True,
                             # timeout=200000
                             )
        print(ret)


def _main():
    creater = ReportCreater(os.path.join('/root/work/webapp/frontend/public/reports', '1' + '.pdf'), 'http://taka16a23.com/reports/mitsumori')
    creater.create()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
