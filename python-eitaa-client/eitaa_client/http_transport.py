"""Placeholder for a real HTTP transport.

This skeleton shows how an HTTP‑based transport might be structured. You would
likely use ``requests`` or ``httpx`` to perform API calls, handle
authentication and manage error handling, rate limiting and retries.
"""

from .base_transport import BaseTransport


class HttpTransport(BaseTransport):
    """HTTP transport skeleton for Eitaa operations."""

    def __init__(self, base_url: str, auth_token: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.auth_token = auth_token

    def join_channel(self, channel_id: str) -> None:
        raise NotImplementedError(
            "HttpTransport.join_channel is not yet implemented. "
            "Implement network requests to join a channel."
        )

    def leave_channel(self, channel_id: str) -> None:
        raise NotImplementedError(
            "HttpTransport.leave_channel is not yet implemented. "
            "Implement network requests to leave a channel."
        )

    def cleanup_account(self) -> None:
        raise NotImplementedError(
            "HttpTransport.cleanup_account is not yet implemented. "
            "Implement network requests to clean up the account."
        )

    def get_post_views(self, channel_id: str, post_id: str) -> int:
        raise NotImplementedError(
            "HttpTransport.get_post_views is not yet implemented. "
            "Implement network requests to fetch post view counts."
        )