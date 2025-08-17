import { BaseTransport } from './baseTransport';

/**
 * Skeleton implementation for a real HTTP transport.
 *
 * A production transport would make HTTP requests to the Eitaa API, handle
 * authentication tokens, and implement retries and error handling. This
 * placeholder throws errors for all methods to indicate that it is not
 * yet implemented.
 */
export class HttpTransport implements BaseTransport {
  constructor(private baseUrl: string, private authToken: string) {}

  async joinChannel(channelId: string): Promise<void> {
    throw new Error('HttpTransport.joinChannel is not implemented');
  }

  async leaveChannel(channelId: string): Promise<void> {
    throw new Error('HttpTransport.leaveChannel is not implemented');
  }

  async cleanupAccount(): Promise<void> {
    throw new Error('HttpTransport.cleanupAccount is not implemented');
  }

  async getPostViews(channelId: string, postId: string): Promise<number> {
    throw new Error('HttpTransport.getPostViews is not implemented');
  }
}