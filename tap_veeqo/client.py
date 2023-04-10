"""REST client handling, including VeeqoStream base class."""

from __future__ import annotations

from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.streams import RESTStream

from tap_veeqo.pagination import VeeqoPaginator


class VeeqoStream(RESTStream):
    """Veeqo stream class."""

    url_base = "https://api.veeqo.com"
    primary_keys = ["id"]
    page_size = 100

    @property
    def authenticator(self):
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="x-api-key",
            value=self.config.get("api_key"),
            location="header",
        )

    def get_new_paginator(self):
        return VeeqoPaginator(self.page_size)

    def get_url_params(self, context, next_page_token):
        return {
            "page_size": self.page_size,
            "page": next_page_token,
        }
