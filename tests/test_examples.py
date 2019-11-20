# -*- coding: utf-8 -*-

import pytest

from anytree import Node
from anytree import RenderTree


def test_stackoverflow():
    """Example from stackoverflow."""
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    Node("Jet", parent=dan)
    Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)

    assert str(udo) == "Node('/Udo')"
    assert str(joe) == "Node('/Udo/Dan/Joe')"

    assert ["%s%s" % (pre, node.name) for pre, fill, node in RenderTree(udo)] == [
        u"Udo",
        u"├── Marc",
        u"│   └── Lian",
        u"└── Dan",
        u"    ├── Jet",
        u"    ├── Jan",
        u"    └── Joe",
    ]
    assert str(dan.children) == "(Node('/Udo/Dan/Jet'), Node('/Udo/Dan/Jan'), Node('/Udo/Dan/Joe'))"
