import asyncio
import websockets
import json
import ssl
import pprint
from secrets import username,password

async def connect():
    uri = "wss://api.tradeville.eu:443"
    async with websockets.client.connect(uri, subprotocols=['apitv']) as websocket:
        credentials = {
                "cmd": "login",
                "prm": {
                    "coduser": username,
                    "parola": password,
                    "demo": False
                }      
        }

        jcred = json.dumps(credentials)

        await websocket.send(jcred)
        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(connect())
