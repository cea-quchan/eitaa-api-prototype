# Python Eitaa Client

This directory contains a simple prototype client library for interacting with the Eitaa messaging platform.

The goal of this project is to provide a clean, extensible interface for programmatically managing an Eitaa account.
It currently includes a high‑level `EitaaClient` class along with transport abstractions for different communication backends.

## Key features

* **Join a channel** – programmatically join an Eitaa channel by its ID.
* **Leave a channel** – leave any channel previously joined.
* **Clean up an account** – remove all channel and group memberships and clear stored data.
* **Get post views** – retrieve a post's view count from a channel.

The default transport is a simple in‑memory mock transport used for development and testing. A `HttpTransport` skeleton is included for future integration with a real API or automation layer.

## Getting started

Install the package in editable mode and run the example:

```bash
pip install -e .
python examples/example.py
```

The example script demonstrates how to instantiate the client, join a channel, read a post's views and clean up the account.
