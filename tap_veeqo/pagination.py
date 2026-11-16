# Copyright (c) 2026 Meltano.

"""Pagination classes for tap-veeqo."""

from singer_sdk.pagination import PageNumberPaginator
from typing_extensions import override


class VeeqoPaginator(PageNumberPaginator):
    """Base API paginator."""

    def __init__(self, page_size: int) -> None:
        """Create a new paginator.

        Args:
            page_size: Number of records in each page.
        """
        super().__init__(1)
        self.page_size = page_size

    @override
    def has_more(self, response):
        total_pages = response.headers.get("x-total-pages-count")
        if total_pages:
            return self._page_count < int(total_pages)

        total_count = response.headers.get("x-total-count")
        if total_count:
            return self._page_count * self.page_size < int(total_count)

        return False
