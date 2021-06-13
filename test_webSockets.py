from websocket import create_connection
import pytest
from cerberus import Validator

# TEST Setup - Before running the tests
@pytest.fixture(scope="module")
def setup():
    global ws, instrument_data_schema
    ws = create_connection("wss://api.dev.neontrading.com")
    instrument_data_schema = {"title": "InstrumentTopic", "type": "object", "properties":
        {"type": {"type": "string", "example": "instrument"},
         "id": {"type": "string", "description": "ISIN of the instrument", "example": "US36467W1099",
                "pattern": "^[A-Z]{2}[A-Z0-9]{10}$"}
         }, "required": ["type", "id"], "example": {"type": "instrument", "id": "US36467W1099"}}


#  TEST 1: Verify connection status with incorrect protocol
def test_failConnection(setup):
    ws.send('connect 12 {"locale": "de"}')
    result = ws.recv()
    print('Result is - %s' % result)
    assert 'failed' in result, "Connection didn't fail"

#  TEST 2: Verify connection status with correct protocol
def test_successfulConnection(setup):
    ws.send('connect 21 {"device": "FDF93099-8A6B-4C95-AC5C-463937AFF51D", "clientId": "cta", "clientVersion": '
            '"1.0.1", "platformId": "ios", "platformVersion": "10.2", "locale": "de"}')
    response_message = ws.recv()
    assert response_message == 'connected', "Connection Failed"

#  TEST 3: Verify connection status with correct protocol
def test_instrumentData(setup):
    ws.send('sub 2 {"type":"instrument","id":"US36467W1099"}')
    response_message = ws.recv()
    print('instrument data %s' % response_message)
    # assert response_message[1] == b'connected', "Connection was not successful"

    # data_validator = Validator(instrument_data_schema)
    print('parsed message %s' % response_message.split(' ')[2])
    is_valid = Validator.validate(dict(sorted(response_message.split(' ')[2])), instrument_data_schema)
    assert is_valid.is_true(), "Response doesn't resemble schema"
    ws.close()

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
