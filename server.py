#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A simple websocket server for sending client one of the sample JSONs randomly and periodically."""

__author__ = "Seyit Kaya"
__copyright__ = "Copyright 2020, Seyit Kaya"

import argparse
import asyncio
import datetime
import json
import random
import websockets

def event():
    return json.dumps(
      {"event": random.choice(["2365260", "1034912", "1904345", "4456235", "4045914"]),
       "startTime": random.randint(16 * (10 ** 8), 17 * (10 ** 8))
      }
    )

def outcome():
    return json.dumps(
      {"outcome": random.choice([
        "1818321", "1818322", "1818323", "5818321", "5818322", "5818323", "5128324", "4328321", "4328322"
      ]),
       "price": "%s%s" % (random.choice(["+", "-"]), random.randint(0, 500))
      }
    )

async def echo(websocket, path):
    print("Client connection received: {}".format(path))
    while True:
        text = random.choice([event, outcome])()
        await websocket.send(text)
        print("Sent: {}".format(text))
        await asyncio.sleep(3.0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, help="port number")

    args = parser.parse_args()
    args.host = "0.0.0.0"

    print("Started websocket server at {}:{}\n".format(args.host, args.port))

    server = websockets.serve(echo, args.host, args.port)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
