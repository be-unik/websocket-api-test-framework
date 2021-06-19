from websocket import create_connection
import pytest

@pytest.fixture(scope="module")
def setup():
    ws = create_connection("wss://api.dev.neontrading.com")

def test_failConnection(setup):
    ws.send('connect 21 {"clientId": "cta", "clientVersion": '
            '"1.0.1", "platformId": "ios", "platformVersion": "10.2", "locale": "de"}')
    result = ws.recv()
    assert result.contains('error'), "Connection was not successful"

def test_successfulConnection(setup):
    ws.send('connect 21 {"device": "FDF93099-8A6B-4C95-AC5C-463937AFF51D", "clientId": "cta", "clientVersion": '
            '"1.0.1", "platformId": "ios", "platformVersion": "10.2", "locale": "de"}')
    result = ws.recv()
    assert result == 'connected', "Connection was not successful"
    ws.close()

    # ws.send('sub 2 {"type":"instrument","id":"US36467W1099"}')
    # print("Sent")
    # print("Receiving...")
    # result = ws.recv()
    # print("Received 2 - '%s'" % result)

    # count = 0
    # ws.send('sub 4 {"type":"ticker","id":"US36467W1099.LSX"}')
    # while count < 2:
    #     try:
    #         result = ws.recv()
    #         print("Received 3 - '%s'" % result)
    #         count = count + 1
    #     except Exception as e:
    #         print(e)
    #         break

    # ws.send('unsub 4')
    # print("Sent")
    # print("Receiving...")
    # # result = ws.recv()
    # # print("Received 4 -  '%s'" % result)
    # ws.close()
