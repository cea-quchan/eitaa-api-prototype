"""In‑memory mock transport for development and testing.

This transport simulates Eitaa operations without any real network calls.
It stores channel memberships and fake post view counts in memory, making it
suitable for unit tests and prototyping.
"""

from typing import Dict, Tuple

from .base_transport import BaseTransport


class MockTransport(BaseTransport):
    """Simple in‑memory transport that fakes Eitaa operations."""

    def __init__(self) -> None:
        self._channels: set[str] = set()
        # Using a dict keyed by (channel_id, post_id) to store view counts
        self._posts: Dict[Tuple[str, str], int] = {}

    def join_channel(self, channel_id: str) -> None:
        self._channels.add(channel_id)

    def leave_channel(self, channel_id: str) -> None:
        self._channels.discard(channel_id)

    def cleanup_account(self) -> None:
        self._channels.clear()
        self._posts.clear()

    def get_post_views(self, channel_id: str, post_id: str) -> int:
        return self._posts.get((channel_id, post_id), 0)

    # Additional helper to set a fake view count (not part of the transport API)
    def _set_post_views(self, channel_id: str, post_id: str, views: int) -> None:
        self._posts[(channel_id, post_id)] = views