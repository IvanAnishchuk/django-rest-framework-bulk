from __future__ import print_function, unicode_literals
import rest_framework


# import schema generator only for DRF 3+
if not str(rest_framework.__version__).startswith('2'):
    from .drf3.schemas import *  # noqa
