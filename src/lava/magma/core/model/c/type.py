# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier:  BSD-3-Clause
from dataclasses import dataclass


@dataclass
class LavaCType:
    d_type: str
    precision: int = None  # If None, infinite precision is assumed
