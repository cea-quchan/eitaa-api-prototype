# Node.js Eitaa Client

This directory contains a simple TypeScript prototype client for interacting with the Eitaa messaging platform.
It mirrors the Python client in functionality and structure, exposing a high‑level `EitaaClient` class built on top of a transport abstraction.

## Key features

* **joinChannel(channelId)** – join a channel by ID.
* **leaveChannel(channelId)** – leave a channel by ID.
* **cleanupAccount()** – remove all channel memberships and clear state.
* **getPostViews(channelId, postId)** – fetch the number of views for a post.

The default transport is a simple in‑memory `MockTransport` for development and testing. A skeleton `HttpTransport` is included for future integration with real network APIs.

## Getting started

Install dependencies, build and run the example:

```bash
npm install
npm run build
node dist/examples/sample.js
```

The example demonstrates how to create a client, join a channel, read a post's views and clean up the account.