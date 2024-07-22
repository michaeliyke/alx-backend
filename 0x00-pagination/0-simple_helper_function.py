#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, pageSize: int) -> Tuple[int, int]:
    """Returns a tuple with start and end indexes

    Args:
        page: int - page number i.e the number of pages
        pageSize: int - number of items per page

    Returns:
        Tuple[int, int] - a tuple with start and end indexes

    Examples:
        index_range(1, 7) -> (0, 7)
        index_range(3, 15) -> (30, 45)
    """
    startIndex = (page - 1) * pageSize
    endIndex = page * pageSize
    return (startIndex, endIndex)
