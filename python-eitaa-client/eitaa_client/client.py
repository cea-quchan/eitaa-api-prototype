"""High‑level client for interacting with Eitaa via a transport layer."""

from __future__ import annotations

from typing import Optional

from .base_transport import BaseTransport
from .mock_transport import MockTransport


class EitaaClient:
    """A user‑friendly wrapper around a transport implementation."""

    def __init__(self, transport: Optional[BaseTransport] = None) -> None:
        # If no transport is provided, fall back to an in‑memory mock
        self.transport: BaseTransport = transport or MockTransport()

    def join_channel(self, channel_id: str) -> None:
        """Join a channel via the underlying transport."""
        self.transport.join_channel(channel_id)

    def leave_channel(self, channel_id: str) -> None:
        """Leave a channel via the underlying transport."""
        self.transport.leave_channel(channel_id)

    def cleanup_account(self) -> None:
        """Clean up the account via the underlying transport."""
        self.transport.cleanup_account()

    def get_post_views(self, channel_id: str, post_id: str) -> int:
        """Return the view count for a post via the underlying transport."""
        return self.transport.get_post_views(channel_id, post_id)