from gym_derk import DerkSession, DerkAgentServer, DerkAppInstance
import asyncio
import logging
logging.basicConfig(level = logging.INFO)

async def run_session(env: DerkSession):
  while True:
    await env.reset()
    while not env.done:
      action_n = [env.action_space.sample() for i in range(env.n_agents)]
      await env.step(action_n)

async def main():
  server = DerkAgentServer(run_session, port=8788)
  await server.start()
  app = DerkAppInstance(browser_logs=True)
  await app.start()
  await app.run_session()

asyncio.get_event_loop().run_until_complete(main())
