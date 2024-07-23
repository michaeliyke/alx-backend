#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
from typing import Tuple, List, Dict, Any
import csv
import math
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        The init method for Server class
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset, loaded only once, but for multiple paging requests
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_data(self, start: int, end: int) -> List[List]:
        """
        Safely return the appropriate page of the dataset
        Takes care of the end of the list to return an empty list
        """
        if end > len(self.dataset()):
            end = len(self.dataset())

        if start > len(self.dataset()):
            return []

        return self.dataset()[start:end]

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page with the given page number and page size"""
        msg = "page and page_size must be int and greater than 0"
        assert type(page) == int and type(
            page_size) == int and page > 0 and page_size > 0, msg
        start, end = index_range(page, page_size)
        return self.get_data(start, end)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get hypermedia pagination"""
        # self: Server = Server()
        data = self.get_page(page, page_size)
        total = len(self.dataset())
        total_pages = math.ceil(total / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

    def get_hyper_index(self, index: int = None, page_size=10) -> Dict[str, Any]:
        """
        Get hypermedia pagination with index

        Args:
            index: int - the current start index of the return page
            page_size: int - number of items per page
        """
        # Use assert to verify that index is in a valid range.
        assert index in self.indexed_dataset(), "index out of range"
        data = self.get_page(index, page_size)
        total = len(self.dataset())
        total_pages = math.ceil(total / page_size)
        next_index = index + page_size
        return {
            "index": index,
            "page_size": len(data),
            "next_index": next_index,
            "page": index,
            "data": data,
            "next_page": next_index if next_index < total else None
        }
