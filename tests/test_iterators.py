from anytree import LevelGroupOrderIter
from anytree import LevelOrderGroupIter
from anytree import LevelOrderIter
from anytree import Node
from anytree import PostOrderIter
from anytree import PreOrderIter
from anytree import ZigZagGroupIter
import pytest


def test_preorder():
    """PreOrderIter."""
    f = Node("f")
    b = Node("b", parent=f)
    a = Node("a", parent=b)
    d = Node("d", parent=b)
    c = Node("c", parent=d)
    e = Node("e", parent=d)
    g = Node("g", parent=f)
    i = Node("i", parent=g)
    h = Node("h", parent=i)

    assert list(PreOrderIter(f)) == [f, b, a, d, c, e, g, i, h]
    assert list(PreOrderIter(f, maxlevel=0)) == []
    assert list(PreOrderIter(f, maxlevel=3)) == [f, b, a, d, g, i]
    assert list(PreOrderIter(f, filter_=lambda n: n.name not in ('e', 'g'))) == [f, b, a, d, c, i, h]
    assert list(PreOrderIter(f, stop=lambda n: n.name == 'd')) == [f, b, a, g, i, h]

    it = PreOrderIter(f)
    assert next(it) == f
    assert next(it) == b
    assert list(it) == [a, d, c, e, g, i, h]


def test_postorder():
    """PostOrderIter."""
    f = Node("f")
    b = Node("b", parent=f)
    a = Node("a", parent=b)
    d = Node("d", parent=b)
    c = Node("c", parent=d)
    e = Node("e", parent=d)
    g = Node("g", parent=f)
    i = Node("i", parent=g)
    h = Node("h", parent=i)

    assert list(PostOrderIter(f)) == [a, c, e, d, b, h, i, g, f]
    assert list(PostOrderIter(f, maxlevel=0)) == []
    assert list(PostOrderIter(f, maxlevel=3)) == [a, d, b, i, g, f]
    assert list(PostOrderIter(f, filter_=lambda n: n.name not in ('e', 'g'))) == [a, c, d, b, h, i, f]
    assert list(PostOrderIter(f, stop=lambda n: n.name == 'd')) == [a, b, h, i, g, f]

    it = PostOrderIter(f)
    assert next(it) == a
    assert next(it) == c
    assert list(it) == [e, d, b, h, i, g, f]


def test_levelorder():
    """LevelOrderIter."""
    f = Node("f")
    b = Node("b", parent=f)
    a = Node("a", parent=b)
    d = Node("d", parent=b)
    c = Node("c", parent=d)
    e = Node("e", parent=d)
    g = Node("g", parent=f)
    i = Node("i", parent=g)
    h = Node("h", parent=i)

    assert list(LevelOrderIter(f)) == [f, b, g, a, d, i, c, e, h]
    assert list(LevelOrderIter(f, maxlevel=0)) == []
    assert list(LevelOrderIter(f, maxlevel=3)) == [f, b, g, a, d, i]
    assert list(LevelOrderIter(f, filter_=lambda n: n.name not in ('e', 'g'))) == [f, b, a, d, i, c, h]
    assert list(LevelOrderIter(f, stop=lambda n: n.name == 'd')) == [f, b, g, a, i, h]

    it = LevelOrderIter(f)
    assert next(it) == f
    assert next(it) == b
    assert list(it) == [g, a, d, i, c, e, h]


def test_levelgrouporder():
    """LevelGroupOrderIter."""
    f = Node("f")
    b = Node("b", parent=f)
    a = Node("a", parent=b)
    d = Node("d", parent=b)
    c = Node("c", parent=d)
    e = Node("e", parent=d)
    g = Node("g", parent=f)
    i = Node("i", parent=g)
    h = Node("h", parent=i)

    assert list(LevelGroupOrderIter(f)) == [(f,), (b, g), (a, d, i), (c, e, h)]
    assert list(LevelGroupOrderIter(f, maxlevel=0)) == []
    assert list(LevelGroupOrderIter(f, maxlevel=3)) == [(f,), (b, g), (a, d, i)]
    assert list(LevelGroupOrderIter(f, filter_=lambda n: n.name not in ('e', 'g'))) == [(f,), (b,), (a, d, i), (c, h)]
    assert list(LevelGroupOrderIter(f, stop=lambda n: n.name == 'd')) == [(f,), (b, g), (a, i), (h, )]

    it = LevelGroupOrderIter(f)
    assert next(it) == (f, )
    assert next(it) == (b, g)
    assert list(it) ==  [(a, d, i), (c, e, h)]


def test_levelordergroup():
    """LevelOrderGroupIter."""
    f = Node("f")
    b = Node("b", parent=f)
    a = Node("a", parent=b)
    d = Node("d", parent=b)
    c = Node("c", parent=d)
    e = Node("e", parent=d)
    g = Node("g", parent=f)
    i = Node("i", parent=g)
    h = Node("h", parent=i)

    assert list(LevelOrderGroupIter(f)) == [(f,), (b, g), (a, d, i), (c, e, h)]
    assert list(LevelOrderGroupIter(f, maxlevel=0)) == []
    assert list(LevelOrderGroupIter(f, maxlevel=3)) == [(f,), (b, g), (a, d, i)]
    assert list(LevelOrderGroupIter(f, filter_=lambda n: n.name not in ('e', 'g'))) == [(f,), (b,), (a, d, i), (c, h)]
    assert list(LevelOrderGroupIter(f, stop=lambda n: n.name == 'd')) == [(f,), (b, g), (a, i), (h, )]

    it = LevelOrderGroupIter(f)
    assert next(it) == (f, )
    assert next(it) == (b, g)
    assert list(it) == [(a, d, i), (c, e, h)]


def test_zigzaggroup():
    """ZigZagGroupIter."""
    f = Node("f")
    b = Node("b", parent=f)
    a = Node("a", parent=b)
    d = Node("d", parent=b)
    c = Node("c", parent=d)
    e = Node("e", parent=d)
    g = Node("g", parent=f)
    i = Node("i", parent=g)
    h = Node("h", parent=i)

    assert list(ZigZagGroupIter(f)) == [(f,), (g, b), (a, d, i), (h, e, c)]
    assert list(ZigZagGroupIter(f, maxlevel=0)) == []
    assert list(ZigZagGroupIter(f, maxlevel=3)) == [(f,), (g, b), (a, d, i)]
    assert list(ZigZagGroupIter(f, filter_=lambda n: n.name not in ('e', 'g'))) == [(f,), (b,), (a, d, i), (h, c)]
    assert list(ZigZagGroupIter(f, stop=lambda n: n.name == 'd')) == [(f,), (g, b), (a, i), (h, )]

    it = ZigZagGroupIter(f)
    assert next(it) == (f, )
    assert next(it) == (g, b)
    assert list(it) == [(a, d, i), (h, e, c)]
