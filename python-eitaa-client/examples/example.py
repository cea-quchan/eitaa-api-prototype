"""Example usage of the Eitaa client prototype."""

from eitaa_client.client import EitaaClient


def main() -> None:
    # Use the default mock transport
    client = EitaaClient()
    # Join a sample channel
    client.join_channel("example_channel")
    # Retrieve post views (will be zero in the mock)
    views = client.get_post_views("example_channel", "1")
    print(f"Views: {views}")
    # Clean up the account
    client.cleanup_account()


if __name__ == "__main__":
    main()