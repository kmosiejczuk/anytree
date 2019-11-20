# -*- coding: utf-8 -*-
import pytest

import anytree as at

from helper import assert_raises


def test_get():
    """Get."""
    top = at.Node("top", parent=None)
    sub0 = at.Node("sub0", parent=top)
    sub0sub0 = at.Node("sub0sub0", parent=sub0)
    sub0sub1 = at.Node("sub0sub1", parent=sub0)
    sub1 = at.Node("sub1", parent=top)
    r = at.Resolver('name')
    assert r.get(top, "sub0/sub0sub0") == sub0sub0
    assert r.get(sub1, "..") == top
    assert r.get(sub1, "../sub0/sub0sub1") == sub0sub1
    assert r.get(sub1, ".") == sub1
    assert r.get(sub1, "") == sub1
    with assert_raises(at.ChildResolverError,
                       "Node('/top') has no child sub2. Children are: 'sub0', 'sub1'."):
        r.get(top, "sub2")
    assert r.get(sub0sub0, "/top") == top
    assert r.get(sub0sub0, "/top/sub0") == sub0
    with assert_raises(at.ResolverError, "root node missing. root is '/top'."):
        r.get(sub0sub0, "/")
    with assert_raises(at.ResolverError, "unknown root node '/bar'. root is '/top'."):
        r.get(sub0sub0, "/bar")


def test_glob():
    """Wildcard."""
    top = at.Node("top", parent=None)
    sub0 = at.Node("sub0", parent=top)
    sub0sub0 = at.Node("sub0", parent=sub0)
    sub0sub1 = at.Node("sub1", parent=sub0)
    sub0sub1sub0 = at.Node("sub0", parent=sub0sub1)
    at.Node("sub1", parent=sub0sub1)
    sub1 = at.Node("sub1", parent=top)
    sub1sub0 = at.Node("sub0", parent=sub1)
    r = at.Resolver()
    assert r.glob(top, "*/*/sub0") == [sub0sub1sub0]

    assert r.glob(top, "sub0/sub?") == [sub0sub0, sub0sub1]
    assert r.glob(sub1, ".././*") == [sub0, sub1]
    assert r.glob(top, "*/*") == [sub0sub0, sub0sub1, sub1sub0]
    assert r.glob(top, "*/sub0") == [sub0sub0, sub1sub0]
    with assert_raises(at.ChildResolverError,
                       "Node('/top/sub1') has no child sub1. Children are: 'sub0'."):
        r.glob(top, "sub1/sub1")


def test_glob_cache():
    """Wildcard Cache."""
    root = at.Node("root")
    sub0 = at.Node("sub0", parent=root)
    sub1 = at.Node("sub1", parent=root)
    r = at.Resolver()
    # strip down cache size
    at.resolver._MAXCACHE = 2
    at.Resolver._match_cache.clear()
    assert len(at.Resolver._match_cache) == 0
    assert r.glob(root, "sub0") == [sub0]
    assert len(at.Resolver._match_cache) == 1
    assert r.glob(root, "sub1") == [sub1]
    assert len(at.Resolver._match_cache) == 2
    assert r.glob(root, "sub*") == [sub0, sub1]
    assert len(at.Resolver._match_cache) == 1


def test_same_name():
    """Same Name."""
    root = at.Node("root")
    sub0 = at.Node("sub", parent=root)
    sub1 = at.Node("sub", parent=root)
    r = at.Resolver()
    assert r.get(root, "sub") == sub0
    assert r.glob(root, "sub") == [sub0, sub1]
