#!/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2014 H1d3r (http://breakchan.tk)
Mail:H1d3r[at]foxmail.com
"""

import sys

from comm.printer import *
from conf.config import START_STR
from core.controller import start


def main(args=None):
    print_line(START_STR)
    try:
        start()
    except Exception,e:
        print_error(str(e))
        import traceback;traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

