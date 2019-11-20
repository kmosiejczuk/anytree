from contextlib import contextmanager

import six
import pytest


# hack own assert_raises, because py26 has a different impelmentation
@contextmanager
def assert_raises(exccls, msg):
    try:
        yield
        assert False, "%r not raised" % exccls
    except Exception as exc:
        assert isinstance(exc, exccls), "%r is not a %r" % (exc, exccls)
        assert str(exc) == msg


def eq_str(value, expected):
    if six.PY2:
        assert value.decode('utf-8') == expected
    else:
        assert value == expected
