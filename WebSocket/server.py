import asyncio
import datetime
import websockets


async def time(websocket, path):

    while True:
            now = datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
            await websocket.send(now)
            await asyncio.sleep(1)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

