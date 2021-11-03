# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import black

from lab_black import BlackFormatter, black_formatter, unload_ipython_extension


def load_ipython_extension(ip, line_length=88):
    
    global black_formatter
    
    mode = black.FileMode(
        target_versions={black.TargetVersion.PY37}, line_length=line_length,
    )
    
    if black_formatter is None:
        black_formatter = BlackFormatter(ip, is_lab=False, mode=mode)
        ip.events.register("post_run_cell", black_formatter.format_cell)
