# -*- coding: utf-8 -*-
import pytest

from anytree.util import commonancestors, leftsibling, rightsibling
from anytree import Node


def test_commonancestors():
    """commonancestors."""
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    joe = Node("Joe", parent=dan)

    assert commonancestors(jet, joe) == (udo, dan)
    assert commonancestors(jet, marc) == (udo,)
    assert commonancestors(jet) == (udo, dan)
    assert commonancestors() == ()
    assert commonancestors(jet, lian) == (udo, )


def test_leftsibling():
    """leftsibling."""
    dan = Node("Dan")
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
    assert leftsibling(dan) == None
    assert leftsibling(jet) == None
    assert leftsibling(jan) == jet
    assert leftsibling(joe) == jan


def test_rightsibling():
    """rightsibling."""
    dan = Node("Dan")
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
    assert rightsibling(dan) == None
    assert rightsibling(jet) == jan
    assert rightsibling(jan) == joe
    assert rightsibling(joe) == None
