from singer_sdk.pagination import BasePageNumberPaginator


class VeeqoPaginator(BasePageNumberPaginator):
    def __init__(self, page_size: int):
        super().__init__(1)
        self.page_size = page_size

    def has_more(self, response):
        total_pages = response.headers.get("x-total-pages-count")
        if total_pages:
            return self._page_count < int(total_pages)

        total_count = response.headers.get("x-total-count")
        if total_count:
            return self._page_count * self.page_size < int(total_count)

        return False
