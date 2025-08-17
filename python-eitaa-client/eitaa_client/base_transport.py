"""Abstract base transport for network communications.

Transports encapsulate the actual mechanism used to talk to the Eitaa service,
such as HTTP requests, browser automation or a local mock. Subclasses must
implement all abstract methods defined here.
"""

from abc import ABC, abstractmethod


class BaseTransport(ABC):
    """Abstract base transport for Eitaa operations."""

    @abstractmethod
    def join_channel(self, channel_id: str) -> None:
        """Join a channel by its identifier."""
        raise NotImplementedError

    @abstractmethod
    def leave_channel(self, channel_id: str) -> None:
        """Leave a channel by its identifier."""
        raise NotImplementedError

    @abstractmethod
    def cleanup_account(self) -> None:
        """Perform a comprehensive clean‑up of the account.

        This should remove all channel and group memberships and clear any
        stored state.
        """
        raise NotImplementedError

    @abstractmethod
    def get_post_views(self, channel_id: str, post_id: str) -> int:
        """Return the number of views for a post in a channel."""
        raise NotImplementedError