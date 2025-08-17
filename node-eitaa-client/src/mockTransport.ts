import { BaseTransport } from './baseTransport';

/**
 * A simple in‑memory transport for development and testing.
 *
 * Stores channel membership and fake post view counts in memory.
 */
export class MockTransport implements BaseTransport {
  private channels: Set<string> = new Set();
  private posts: Map<string, number> = new Map();

  async joinChannel(channelId: string): Promise<void> {
    this.channels.add(channelId);
  }

  async leaveChannel(channelId: string): Promise<void> {
    this.channels.delete(channelId);
  }

  async cleanupAccount(): Promise<void> {
    this.channels.clear();
    this.posts.clear();
  }

  async getPostViews(channelId: string, postId: string): Promise<number> {
    const key = `${channelId}:${postId}`;
    return this.posts.get(key) ?? 0;
  }

  /**
   * Helper to set a fake view count (not part of the public API).
   */
  _setPostViews(channelId: string, postId: string, views: number): void {
    const key = `${channelId}:${postId}`;
    this.posts.set(key, views);
  }
}