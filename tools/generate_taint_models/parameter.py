# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from enum import auto, Enum
from typing import NamedTuple, Optional


class Parameter(NamedTuple):
    class Kind(Enum):
        # pyre-fixme[20]: Argument `value` expected.
        ARG = auto()
        # pyre-fixme[20]: Argument `value` expected.
        VARARG = auto()
        # pyre-fixme[20]: Argument `value` expected.
        KWARG = auto()

    name: str
    annotation: Optional[str]
    kind: Kind

    def __eq__(self, other: "Parameter") -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.name == other.name
