from websocket import create_connection

if __name__ == "__main__":
    ws = create_connection("wss://api.dev.neontrading.com")
    print("Sending 'Hello, World'...")
    ws.send('connect 21 {"device": "FDF93099-8A6B-4C95-AC5C-463937AFF51D", "clientId": "cta", "clientVersion": '
            '"1.0.1", "platformId": "ios", "platformVersion": "10.2", "locale": "de"}')
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received 1 - '%s'" % result)

    ws.send('sub 2 {"type":"instrument","id":"US36467W1099"}')
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received 2 - '%s'" % result)

    count = 0
    print("Sent")
    print("Receiving...")
    ws.send('sub 4 {"type":"ticker","id":"US36467W1099.LSX"}')
    print(ws.recv())
    # print("Received 3 - '%s'" % result)

    ws.send('unsub 4')
    print("Sent")
    print("Receiving...")
    print(ws.recv())

    ws.close()
