"""REST client handling, including VeeqoStream base class."""

from __future__ import annotations

from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_veeqo.pagination import VeeqoPaginator


class VeeqoStream(RESTStream):
    """Veeqo stream class."""

    url_base = "https://api.veeqo.com"
    primary_keys = ("id",)
    page_size = 100

    @property
    @override
    def authenticator(self):
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="x-api-key",
            value=self.config.get("api_key"),
            location="header",
        )

    @override
    def get_new_paginator(self):
        return VeeqoPaginator(self.page_size)

    @override
    def get_url_params(self, context, next_page_token):
        params = {
            "per_page": self.page_size,
            "page": next_page_token,
        }

        last_updated = self.get_context_state(context).get("replication_key_value")

        if last_updated and next_page_token == 1:
            params["updated_at_min"] = last_updated

        return params

    @override
    def backoff_max_tries(self):
        return 8
