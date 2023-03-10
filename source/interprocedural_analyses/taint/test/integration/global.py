# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from builtins import _test_sink, _test_source

obj1 = object()


def obj1_source():
    obj1.x = _test_source()


def obj1_sink():
    _test_sink(obj1.x)


def obj1_flow():
    # TODO(T145247918): False negative
    obj1_source()
    obj1_sink()


def obj1_no_flow():
    obj1_sink()
    obj1_source()


obj2 = object()


def obj2_sink():
    _test_sink(obj2)


obj3 = object()


def obj3_return():
    return obj3


def obj3_set(x):
    obj3.x = x


def obj3_flow():
    # TODO(T145247918): False negative
    obj3_set(_test_source())
    y = obj3_return()
    _test_sink(y.x)


obj4 = _test_source()


def obj4_flow():
    # TODO(T145247918): False negative
    _test_sink(obj4)