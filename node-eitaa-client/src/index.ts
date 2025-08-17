import { BaseTransport } from './baseTransport';
import { MockTransport } from './mockTransport';

/**
 * High‑level client wrapper around a transport implementation.
 */
export class EitaaClient {
  constructor(private transport: BaseTransport = new MockTransport()) {}

  /** Join a channel via the underlying transport. */
  async joinChannel(channelId: string): Promise<void> {
    await this.transport.joinChannel(channelId);
  }

  /** Leave a channel via the underlying transport. */
  async leaveChannel(channelId: string): Promise<void> {
    await this.transport.leaveChannel(channelId);
  }

  /** Clean up the account via the underlying transport. */
  async cleanupAccount(): Promise<void> {
    await this.transport.cleanupAccount();
  }

  /** Retrieve the view count for a post via the underlying transport. */
  async getPostViews(channelId: string, postId: string): Promise<number> {
    return this.transport.getPostViews(channelId, postId);
  }
}