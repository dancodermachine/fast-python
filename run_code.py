import asyncio

# run a command in a subprocess
process = await asyncio.create_subprocess_shell('sleep 3')

# wait for the subprocess to terminate
await process.wait()