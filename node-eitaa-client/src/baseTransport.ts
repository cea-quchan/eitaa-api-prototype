/**
 * Transport interface that defines Eitaa operations.
 *
 * Different implementations may communicate via HTTP, web automation or other
 * mechanisms. Each method returns a Promise to support asynchronous flows.
 */
export interface BaseTransport {
  /** Join a channel by its identifier. */
  joinChannel(channelId: string): Promise<void>;
  /** Leave a channel by its identifier. */
  leaveChannel(channelId: string): Promise<void>;
  /** Clean up the account by removing all memberships and clearing state. */
  cleanupAccount(): Promise<void>;
  /** Retrieve the number of views for a given post. */
  getPostViews(channelId: string, postId: string): Promise<number>;
}