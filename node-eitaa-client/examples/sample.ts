import { EitaaClient } from '../src';

async function main(): Promise<void> {
  const client = new EitaaClient();
  await client.joinChannel('example_channel');
  const views = await client.getPostViews('example_channel', '1');
  console.log(`Views: ${views}`);
  await client.cleanupAccount();
}

main().catch((err) => {
  console.error(err);
});